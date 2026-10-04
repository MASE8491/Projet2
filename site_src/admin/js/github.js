// Client minimal de l'API REST de GitHub, utilisé par le back-office.
// Toutes les requêtes partent du navigateur de l'administrateur, avec son jeton personnel.

const API = "https://api.github.com";

export class GitHubError extends Error {
  constructor(status, message, details) {
    super(message);
    this.status = status;
    this.details = details;
  }
}

function utf8ToBase64(text) {
  const bytes = new TextEncoder().encode(text);
  let bin = "";
  for (let i = 0; i < bytes.length; i += 0x8000) {
    bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  }
  return btoa(bin);
}

export function base64ToUtf8(b64) {
  const bin = atob(b64.replace(/\n/g, ""));
  const bytes = Uint8Array.from(bin, (c) => c.charCodeAt(0));
  return new TextDecoder().decode(bytes);
}

export class GitHub {
  constructor({ token, repo, branch }) {
    this.token = token;
    this.repo = repo;
    this.branch = branch;
  }

  async request(method, path, body) {
    let res;
    try {
      res = await fetch(API + path, {
        method,
        headers: {
          Accept: "application/vnd.github+json",
          Authorization: `Bearer ${this.token}`,
          "X-GitHub-Api-Version": "2022-11-28",
          ...(body ? { "Content-Type": "application/json" } : {}),
        },
        body: body ? JSON.stringify(body) : undefined,
        cache: "no-store",
      });
    } catch (err) {
      throw new GitHubError(0, "Impossible de joindre GitHub. Vérifiez votre connexion Internet.", err);
    }
    if (res.status === 204) return null;
    const data = await res.json().catch(() => null);
    if (!res.ok) {
      const msg = {
        401: "Le jeton GitHub est invalide ou a expiré.",
        403: "Le jeton GitHub n'a pas les droits nécessaires (ou la limite d'appels est atteinte).",
        404: "Élément introuvable sur GitHub (dépôt, branche ou fichier). Vérifiez aussi les droits du jeton.",
        409: "Conflit : le dépôt a été modifié en même temps.",
        422: "GitHub a refusé la modification (données invalides ou conflit).",
      }[res.status] || `Erreur GitHub (${res.status}).`;
      throw new GitHubError(res.status, msg, data);
    }
    return data;
  }

  // ---------------------------------------------------------------- Lecture
  getRepo() {
    return this.request("GET", `/repos/${this.repo}`);
  }

  getUser() {
    return this.request("GET", "/user");
  }

  async getHeadSha() {
    const ref = await this.request("GET", `/repos/${this.repo}/git/ref/heads/${encodeURIComponent(this.branch)}`);
    return ref.object.sha;
  }

  getCommit(sha) {
    return this.request("GET", `/repos/${this.repo}/git/commits/${sha}`);
  }

  getTree(sha) {
    return this.request("GET", `/repos/${this.repo}/git/trees/${sha}?recursive=1`);
  }

  async getBlobText(sha) {
    const blob = await this.request("GET", `/repos/${this.repo}/git/blobs/${sha}`);
    return base64ToUtf8(blob.content);
  }

  /** Lit plusieurs fichiers d'un même commit : renvoie { chemin: { text, sha } }. */
  async readFiles(commitSha, paths) {
    const commit = await this.getCommit(commitSha);
    const tree = await this.getTree(commit.tree.sha);
    const byPath = Object.fromEntries(tree.tree.filter((e) => e.type === "blob").map((e) => [e.path, e.sha]));
    const out = {};
    await Promise.all(paths.map(async (p) => {
      if (!byPath[p]) throw new GitHubError(404, `Fichier absent du dépôt : ${p}`);
      out[p] = { sha: byPath[p], text: await this.getBlobText(byPath[p]) };
    }));
    return { files: out, treeSha: commit.tree.sha, tree: byPath };
  }

  listCommits(path, perPage = 30) {
    return this.request("GET", `/repos/${this.repo}/commits?sha=${encodeURIComponent(this.branch)}&path=${encodeURIComponent(path)}&per_page=${perPage}`);
  }

  async findRun(headSha) {
    const data = await this.request("GET", `/repos/${this.repo}/actions/runs?head_sha=${headSha}&per_page=5`);
    return (data.workflow_runs || [])[0] || null;
  }

  // ---------------------------------------------------------------- Écriture
  /**
   * Crée un commit unique sur la branche à partir de fichiers texte et binaires.
   * files : [{ path, text } | { path, base64 } | { path, sha } | { path, delete: true }]
   */
  async commitFiles(message, files, parentSha) {
    const parent = parentSha || (await this.getHeadSha());
    const parentCommit = await this.getCommit(parent);
    const entries = [];
    for (const f of files) {
      if (f.delete) {
        entries.push({ path: f.path, mode: "100644", type: "blob", sha: null });
        continue;
      }
      let sha = f.sha;
      if (!sha) {
        const blob = await this.request("POST", `/repos/${this.repo}/git/blobs`,
          f.base64 !== undefined ? { content: f.base64, encoding: "base64" } : { content: f.text, encoding: "utf-8" });
        sha = blob.sha;
      }
      entries.push({ path: f.path, mode: "100644", type: "blob", sha });
    }
    const tree = await this.request("POST", `/repos/${this.repo}/git/trees`, { base_tree: parentCommit.tree.sha, tree: entries });
    const commit = await this.request("POST", `/repos/${this.repo}/git/commits`, { message, tree: tree.sha, parents: [parent] });
    await this.request("PATCH", `/repos/${this.repo}/git/refs/heads/${encodeURIComponent(this.branch)}`, { sha: commit.sha, force: false });
    return commit.sha;
  }

  static textToBase64(text) {
    return utf8ToBase64(text);
  }
}
