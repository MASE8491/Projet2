// État du back-office : contenu chargé depuis GitHub, brouillon local, publication et historique.

import { GitHub, GitHubError } from "./github.js";

const clone = (v) => JSON.parse(JSON.stringify(v));
const serialize = (v) => JSON.stringify(v, null, 2) + "\n";

export class ConflictError extends Error {
  constructor(files) {
    super("Conflit de publication");
    this.files = files;
  }
}

export class Store {
  constructor(config) {
    this.config = config;
    this.gh = null;
    this.base = {};      // contenu publié (tel que chargé)
    this.shas = {};      // identifiants des fichiers publiés
    this.data = {};      // copie de travail (brouillon)
    this.log = [];       // journal lisible des modifications non publiées
    this.headSha = null;
    this.previews = {};  // aperçus locaux des images téléversées
    this.listeners = new Set();
  }

  get draftKey() { return `komori-admin-draft:${this.config.repo}`; }
  path(file) { return `${this.config.content_dir}/${file}.json`; }
  onChange(fn) { this.listeners.add(fn); }
  emit() { this.listeners.forEach((fn) => fn()); }

  // ---------------------------------------------------------------- Connexion et chargement
  async connect(token) {
    this.gh = new GitHub({ token, repo: this.config.repo, branch: this.config.branch });
    const [repo, user] = await Promise.all([this.gh.getRepo(), this.gh.getUser().catch(() => null)]);
    if (repo.permissions && repo.permissions.push === false) {
      throw new GitHubError(403, "Ce compte GitHub n'a pas le droit de modifier le dépôt.");
    }
    this.repoInfo = repo;
    this.user = user;
    await this.load();
    return { repo, user };
  }

  async load() {
    this.headSha = await this.gh.getHeadSha();
    const paths = this.config.content_files.map((f) => this.path(f));
    const { files } = await this.gh.readFiles(this.headSha, paths);
    for (const f of this.config.content_files) {
      const entry = files[this.path(f)];
      this.base[f] = JSON.parse(entry.text);
      this.shas[f] = entry.sha;
    }
    this.data = clone(this.base);
    this.log = [];
  }

  /** Brouillon enregistré dans ce navigateur : { data, log, shas, savedAt } ou null. */
  readDraft() {
    try {
      const raw = localStorage.getItem(this.draftKey);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  }

  /** Le brouillon a-t-il été préparé à partir de la version publiée actuelle ? */
  draftMatchesBase(draft) {
    return Object.entries(draft.shas || {}).every(([f, sha]) => !draft.data[f] || this.shas[f] === sha);
  }

  restoreDraft(draft) {
    for (const [f, value] of Object.entries(draft.data)) this.data[f] = value;
    this.log = draft.log || [];
    this.emit();
  }

  saveDraft() {
    const changed = this.dirtyFiles();
    try {
      if (!changed.length) localStorage.removeItem(this.draftKey);
      else {
        localStorage.setItem(this.draftKey, JSON.stringify({
          data: Object.fromEntries(changed.map((f) => [f, this.data[f]])),
          shas: Object.fromEntries(changed.map((f) => [f, this.shas[f]])),
          log: this.log,
          savedAt: new Date().toISOString(),
        }));
      }
    } catch (err) {
      console.warn("Brouillon non enregistré", err);
    }
  }

  discardDraft() {
    this.data = clone(this.base);
    this.log = [];
    this.saveDraft();
    this.emit();
  }

  // ---------------------------------------------------------------- Modifications
  dirtyFiles() {
    return this.config.content_files.filter((f) => serialize(this.data[f]) !== serialize(this.base[f]));
  }

  /** Applique une modification déjà confirmée par l'administrateur. */
  apply(text, mutate) {
    const before = serialize(this.data);
    mutate(this.data);
    if (serialize(this.data) !== before) {
      this.log.push({ at: new Date().toISOString(), text });
    }
    this.saveDraft();
    this.emit();
  }

  // ---------------------------------------------------------------- Publication
  async publish(message) {
    const files = this.dirtyFiles();
    if (!files.length) return null;
    const head = await this.gh.getHeadSha();
    if (head !== this.headSha) {
      // Le dépôt a bougé : on vérifie que les fichiers modifiés ici n'ont pas changé ailleurs.
      const { tree } = await this.gh.readFiles(head, []);
      const conflicts = files.filter((f) => tree[this.path(f)] !== this.shas[f]);
      if (conflicts.length) throw new ConflictError(conflicts);
    }
    const commitSha = await this.gh.commitFiles(message,
      files.map((f) => ({ path: this.path(f), text: serialize(this.data[f]) })), head);
    // Le contenu publié devient la nouvelle référence
    const { files: fresh } = await this.gh.readFiles(commitSha, files.map((f) => this.path(f)));
    files.forEach((f) => { this.base[f] = clone(this.data[f]); this.shas[f] = fresh[this.path(f)].sha; });
    this.headSha = commitSha;
    this.log = [];
    this.saveDraft();
    this.emit();
    return commitSha;
  }

  /** Téléverse une image tout de suite (elle n'apparaît sur le site qu'une fois utilisée et publiée). */
  async uploadImage(fileName, base64, objectUrl) {
    const path = `${this.config.uploads_dir}/${fileName}`;
    // Commit séparé : les fichiers de contenu ne changent pas, la publication suivante s'appuiera dessus.
    await this.gh.commitFiles(`Médiathèque : ajout de l'image ${fileName}`, [{ path, base64 }]);
    this.previews[`uploads/${fileName}`] = objectUrl;
    return `uploads/${fileName}`;
  }

  // ---------------------------------------------------------------- Historique
  history() {
    return this.gh.listCommits(this.config.content_dir, 30);
  }

  async restore(commitSha, label) {
    const paths = this.config.content_files.map((f) => this.path(f));
    // Certains fichiers peuvent ne pas avoir existé à cette date : on restaure ceux qui existaient.
    const { tree } = await this.gh.readFiles(commitSha, []);
    const { files } = await this.gh.readFiles(commitSha, paths.filter((p) => tree[p]));
    const entries = Object.entries(files).map(([path, f]) => ({ path, sha: f.sha }));
    const sha = await this.gh.commitFiles(`Restauration du contenu : ${label}`, entries);
    await this.load();
    this.saveDraft();
    this.emit();
    return sha;
  }

  buildStatus(sha) {
    return this.gh.findRun(sha);
  }
}

export { serialize, clone };
