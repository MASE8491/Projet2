// Point d'entrée du back-office : connexion, mise en page, navigation et assistants.

import { h, clear, openModal, confirmImpact, toast, ask, formatDate } from "./ui.js";
import { Store } from "./store.js";
import * as M from "./model.js";
import * as V from "./views.js";
import * as A from "./actions.js";
import { toEditable } from "./richtext.js";

const TOKEN_KEY = "komori-admin-token";
const PUBLISH_KEY = "komori-admin-last-publish";
const COMMONS = "https://commons.wikimedia.org/wiki/Special:FilePath/";

class App {
  constructor(root, config) {
    this.root = root;
    this.config = config;
    this.store = new Store(config);
    this.dirtyCheck = null;
    this.store.onChange(() => this.updateTopbar());
    window.addEventListener("hashchange", () => this.onRoute());
    window.addEventListener("beforeunload", (e) => {
      if (this.dirtyCheck && this.dirtyCheck()) { e.preventDefault(); e.returnValue = ""; }
    });
  }

  // ---------------------------------------------------------------- Adresses
  siteUrl(path) { return new URL(`../${path || ""}`, window.location.href).href; }

  thumb(key, width = 330) {
    const m = this.store.data.media[key];
    if (!m) return "";
    if ((m.kind || "image") === "video") return m.poster ? this.thumb(m.poster, width) : "";
    if (m.src) return this.store.previews[m.src] || this.siteUrl(`assets/${m.src}`);
    return `${COMMONS}${encodeURIComponent(m.file)}?width=${width <= 500 ? 500 : 960}`;
  }

  fileUrl(key) {
    const m = this.store.data.media[key];
    return m.src ? this.siteUrl(`assets/${m.src}`) : `${COMMONS}${encodeURIComponent(m.file)}`;
  }

  pageTitle(path) { return M.pageTitleByPath(this.store.data, path); }

  // ---------------------------------------------------------------- Démarrage
  async start() {
    const token = sessionStorage.getItem(TOKEN_KEY) || localStorage.getItem(TOKEN_KEY);
    if (token) {
      try {
        await this.connect(token);
        return;
      } catch (err) {
        sessionStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(TOKEN_KEY);
        this.loginScreen(err.message);
        return;
      }
    }
    this.loginScreen();
  }

  async connect(token) {
    clear(this.root).append(h("div", { class: "loading" }, h("div", { class: "spinner" }), h("p", {}, "Chargement du contenu du site…")));
    await this.store.connect(token);
    const draft = this.store.readDraft();
    if (draft && Object.keys(draft.data || {}).length) {
      if (this.store.draftMatchesBase(draft)) {
        this.store.restoreDraft(draft);
        toast(`Brouillon restauré : ${draft.log ? draft.log.length : 0} modification(s) non publiée(s).`, "info");
      } else {
        const keep = await confirmImpact({
          title: "Un ancien brouillon a été trouvé", severity: "warning",
          intro: `Ce navigateur contient des modifications non publiées (du ${formatDate(draft.savedAt)}), mais le site a été publié entre-temps.`,
          sections: [{ heading: "Modifications du brouillon :", items: (draft.log || []).map((l) => l.text) }],
          notes: ["Reprendre le brouillon écrasera les changements publiés depuis sur les mêmes fichiers. En cas de doute, abandonnez le brouillon."],
          confirmLabel: "Reprendre mon brouillon", cancelLabel: "Abandonner le brouillon",
        });
        if (keep) this.store.restoreDraft(draft);
        else this.store.discardDraft();
      }
    }
    this.layout();
    this.onRoute();
  }

  loginScreen(error) {
    const token = h("input", { type: "password", class: "input", autocomplete: "off", placeholder: "github_pat_…", "aria-label": "Jeton GitHub" });
    const remember = h("input", { type: "checkbox" });
    const msg = h("p", { class: "error", hidden: !error }, error || "");
    const submit = async (e) => {
      e.preventDefault();
      const value = token.value.trim();
      if (!value) return;
      msg.hidden = true;
      try {
        (remember.checked ? localStorage : sessionStorage).setItem(TOKEN_KEY, value);
        await this.connect(value);
      } catch (err) {
        sessionStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(TOKEN_KEY);
        this.loginScreen(err.message);
      }
    };
    const [owner, repo] = this.config.repo.split("/");
    clear(this.root).append(h("div", { class: "login" },
      h("div", { class: "login-card" },
        h("p", { class: "brand" }, "🌙 Administration"),
        h("h1", {}, "Connexion au back-office"),
        h("p", {}, `Cette interface modifie le contenu du site enregistré dans le dépôt GitHub ${this.config.repo}.`),
        h("form", { onsubmit: submit },
          h("label", { class: "field-label" }, "Votre jeton d'accès GitHub", token),
          h("label", { class: "check" }, remember, " Rester connecté sur cet appareil (ordinateur personnel uniquement)"),
          msg,
          h("button", { type: "submit", class: "btn btn-primary btn-block" }, "Se connecter")),
        h("details", { class: "faq", open: !error && !localStorage.getItem("komori-admin-seen") },
          h("summary", {}, "Comment obtenir un jeton ? (à faire une seule fois)"),
          h("ol", {},
            h("li", {}, "Connectez-vous à GitHub avec un compte autorisé à modifier le dépôt."),
            h("li", {}, "Ouvrez ", h("a", { href: "https://github.com/settings/personal-access-tokens/new", target: "_blank", rel: "noopener" }, "la création d'un jeton à accès précis ↗"), "."),
            h("li", {}, "Nom : « Administration du site » ; Expiration : par exemple 90 jours."),
            h("li", {}, `Repository access : « Only select repositories » puis choisissez ${repo} (propriétaire ${owner}).`),
            h("li", {}, "Repository permissions : « Contents » → Read and write ; « Actions » → Read-only (pour suivre la mise en ligne)."),
            h("li", {}, "Cliquez sur « Generate token », copiez le jeton et collez-le ci-dessus."),
            h("li", {}, "Gardez ce jeton secret : il donne le droit de modifier le site."))),
      ),
    ));
    localStorage.setItem("komori-admin-seen", "1");
    token.focus();
  }

  logout() {
    sessionStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(TOKEN_KEY);
    window.location.hash = "";
    window.location.reload();
  }

  // ---------------------------------------------------------------- Mise en page
  layout() {
    const link = (href, label) => h("a", { href, class: "nav-link", "data-route": href }, label);
    this.topbar = h("div", { class: "topbar-status" });
    this.main = h("main", { class: "admin-main", id: "admin-main" });
    clear(this.root).append(
      h("aside", { class: "sidebar" },
        h("a", { class: "sidebar-brand", href: "#/" }, "🌙 ", h("span", {}, this.store.data.settings.site_name), h("small", {}, "Administration")),
        h("nav", { "aria-label": "Administration" },
          link("#/", "📊 Tableau de bord"),
          link("#/arborescence", "🗂️ Arborescence & pages"),
          link("#/edit/doc:home", "🏠 Page d'accueil"),
          link("#/medias", "🖼️ Médiathèque"),
          link("#/edit/doc:navigation", "🧭 Menu & pied de page"),
          h("p", { class: "nav-group" }, "Rubriques"),
          link("#/edit/topic:histoire", "📜 Histoire"),
          link("#/edit/fixed:contes", "🌙 Hale halele (contes)"),
          link("#/edit/fixed:loisirs", "🎲 Loisirs & quiz"),
          h("p", { class: "nav-group" }, "Listes"),
          link("#/edit/list:timeline", "🕰️ Frise chronologique"),
          link("#/edit/list:events", "📅 Agenda"),
          link("#/edit/list:glossary", "🔤 Glossaire"),
          link("#/edit/list:bibliography", "📖 Bibliographie"),
          link("#/edit/doc:videos", "🎬 Vidéos"),
          h("p", { class: "nav-group" }, "Site"),
          link("#/edit/doc:settings", "⚙️ Réglages"),
          link("#/historique", "🕓 Historique"),
          link("#/publier", "🚀 Publier"),
          link("#/aide", "❔ Aide")),
        h("div", { class: "sidebar-foot" },
          this.store.user ? h("p", {}, "Connecté : ", h("strong", {}, this.store.user.login)) : null,
          h("a", { href: this.siteUrl("index.html"), target: "_blank", rel: "noopener" }, "Voir le site ↗"),
          h("button", { type: "button", class: "btn btn-link btn-small", onclick: async () => {
            if (this.store.dirtyFiles().length && !(await ask("Se déconnecter ?", "Vos modifications non publiées restent enregistrées dans ce navigateur et seront proposées à la prochaine connexion.", { confirmLabel: "Se déconnecter", cancelLabel: "Rester" }))) return;
            this.logout();
          } }, "Se déconnecter"))),
      h("div", { class: "admin-content" }, h("header", { class: "topbar" }, this.topbar), this.main),
    );
    this.updateTopbar();
  }

  updateTopbar() {
    if (!this.topbar) return;
    const n = V.changedIds(this.store).length;
    clear(this.topbar).append(n ? h("span", { class: "draft-pill" }, `✏️ ${n} modification(s) non publiée(s)`) : h("span", { class: "ok-pill" }, "✅ Tout est publié"));
    if (n) this.topbar.append(h("a", { class: "btn btn-primary btn-small", href: "#/publier" }, "🚀 Publier"));
  }

  // ---------------------------------------------------------------- Navigation
  setDirtyCheck(fn) { this.dirtyCheck = fn; }

  async guardLeave() {
    if (this.dirtyCheck && this.dirtyCheck()) {
      const leave = await ask("Quitter sans enregistrer ?", "Les modifications de ce formulaire n'ont pas été enregistrées. Elles seront perdues.", { confirmLabel: "Quitter sans enregistrer", cancelLabel: "Rester sur la page" });
      if (!leave) return false;
    }
    this.dirtyCheck = null;
    return true;
  }

  go(hash) {
    if (window.location.hash === hash) this.render();
    else window.location.hash = hash;
  }

  async onRoute() {
    if (!this.main) return;
    if (this.currentHash !== undefined && this.currentHash !== window.location.hash && this.dirtyCheck && this.dirtyCheck()) {
      const target = window.location.hash;
      history.replaceState(null, "", this.currentHash || "#/");
      if (!(await this.guardLeave())) return;
      window.location.hash = target;
      return;
    }
    this.currentHash = window.location.hash;
    this.dirtyCheck = null;
    this.render();
  }

  render() {
    const hash = window.location.hash || "#/";
    const [, route, ...rest] = hash.split("/");
    const arg = decodeURIComponent(rest.join("/"));
    let view;
    try {
      if (!route) view = V.dashboard(this);
      else if (route === "arborescence") view = V.tree(this);
      else if (route === "edit") view = V.editor(this, arg);
      else if (route === "medias") view = V.mediaLibrary(this);
      else if (route === "media") view = V.mediaEditor(this, arg);
      else if (route === "publier") view = V.publishView(this);
      else if (route === "historique") view = V.historyView(this);
      else if (route === "aide") view = V.helpView(this);
      else view = h("div", { class: "view" }, h("h1", {}, "Page inconnue"), h("a", { href: "#/" }, "← Tableau de bord"));
    } catch (err) {
      console.error(err);
      view = h("div", { class: "view" }, h("h1", {}, "Erreur d'affichage"), h("p", { class: "error" }, err.message));
    }
    clear(this.main).append(view);
    this.root.querySelectorAll("[data-route]").forEach((a) => a.classList.toggle("is-active", a.dataset.route === hash || (hash.startsWith("#/media/") && a.dataset.route === "#/medias")));
    this.updateTopbar();
    this.main.focus({ preventScroll: true });
  }

  // ---------------------------------------------------------------- Contexte des formulaires
  fieldContext(extra = {}) {
    return {
      data: this.store.data,
      thumb: (k) => this.thumb(k),
      pickMedia: (opts) => this.pickMedia(opts),
      pickLink: () => this.pickLink(),
      pageTitle: (p) => this.pageTitle(p),
      ...extra,
    };
  }

  pickMedia({ kind } = {}) {
    return new Promise((resolve) => {
      let done = false;
      const finish = (key) => { if (done) return; done = true; dialogClose(key); };
      let dialogClose = () => {};
      const body = V.mediaLibrary(this, { picker: true, kind: kind || "image", onPick: (key) => finish(key) });
      openModal({ title: kind === "video" ? "Choisir une vidéo" : "Choisir une image", body, size: "modal-wide",
        actions: [{ label: "Annuler", value: null }],
        onOpen: (dialog) => { dialogClose = (key) => { dialog.close(); dialog.remove(); resolve(key); }; },
      }).then((v) => { if (!done) { done = true; resolve(v); } });
    });
  }

  pickLink() {
    const pages = M.sitePages(this.store.data);
    const sel = h("select", { class: "input", size: 12 },
      [...new Set(pages.map((p) => p.group))].map((g) => h("optgroup", { label: g },
        pages.filter((p) => p.group === g).map((p) => h("option", { value: p.path }, p.title + (p.hidden ? " (masquée)" : ""))))));
    return openModal({ title: "Lien vers une page du site", body: h("label", { class: "field-label" }, "Choisissez la page", sel),
      actions: [{ label: "Annuler", value: null }, { label: "Insérer le lien", kind: "btn-primary", value: () => sel.value || null }] });
  }

  // ---------------------------------------------------------------- Aperçu
  preview(id, value) {
    const p = M.parseId(id);
    const media = this.store.data.media;
    const img = (key, cls = "") => (key && media[key] && (media[key].kind || "image") === "image"
      ? `<img class="${cls}" src="${this.thumb(key, 960)}" alt="">` : "");
    const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;");
    const html = (s) => toEditable(s || "").replace(/data-internal="[^"]*"/g, "");
    const title = value.name || value.title || M.titleOf(this.store.data, id);
    const lead = value.lead || value.summary || "";
    let body = "";
    if (value.intro) body += `<div class="prose">${html(value.intro)}</div>`;
    for (const s of value.sections || value.themes || []) {
      body += `<h2>${esc(s.title)}</h2>${s.media ? `<figure class="figure figure-wide">${img(s.media)}<figcaption>${esc(media[s.media]?.caption)}</figcaption></figure>` : ""}${html(s.html)}`;
    }
    if (value.days) body += `<ol>${value.days.map((d) => `<li><strong>${esc(d.when)} — ${esc(d.title)}</strong><br>${esc(d.text)}</li>`).join("")}</ol>`;
    if (value.items && Array.isArray(value.items) && p.type === "list") body += `<ul>${value.items.map((it) => `<li>${esc(it.title || it.term || it.q || "")}</li>`).join("")}</ul>`;
    if (value.body) body += html(value.body);
    if (p.type === "tale") {
      body += `<p class="hale-call"><span class="hale-teller">« Hale ! »</span> <span class="hale-answer">« Halele ! »</span></p>`;
      body += `<div class="tale-text">${html(value.text)}</div>`;
      if (value.moral) body += `<p class="tale-moral">${esc(value.moral)}</p>`;
      if (value.about) body += `<section class="tale-about"><h2>Ce que l'on en sait</h2>${html(value.about)}</section>`;
    }
    if (p.type === "quiz") {
      body += `<ol class="quiz">${(value.questions || []).map((q) => `<li class="quiz-item"><fieldset><legend>${esc(q.q)}</legend>
        <div class="quiz-choices">${(q.choices || []).map((c, i) => `<label class="quiz-choice${i === q.answer ? " is-correct" : ""}">${esc(c)}</label>`).join("")}</div>
        <p class="quiz-explain">${esc(q.explain)}</p></fieldset></li>`).join("")}</ol>`;
    }
    const refs = (value.refs || []).map((rid) => (this.store.data.bibliography || []).find((b) => b.id === rid)).filter(Boolean);
    if (refs.length) body += `<section class="sources"><h2>Références</h2><ul class="sources-list">${refs.map((b) => `<li><strong>${esc(b.author)}</strong>, <em>${esc(b.title)}</em>${b.year ? `, ${esc(b.year)}` : ""}</li>`).join("")}</ul></section>`;
    const doc = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><base href="${this.siteUrl("")}">
      <link rel="stylesheet" href="${this.siteUrl("assets/css/style.css")}"></head><body>
      <section class="hero"><div class="hero-media">${img(value.hero)}</div><div class="hero-overlay"></div>
      <div class="container hero-content"><p class="kicker">${esc(value.kicker || value.period || "")}</p><h1>${esc(title)}</h1><p class="lead">${esc(lead)}</p></div></section>
      <section class="section"><div class="container narrow prose">${body}</div></section></body></html>`;
    const frame = h("iframe", { class: "preview-frame", title: "Aperçu de la page", sandbox: "allow-same-origin" });
    frame.srcdoc = doc;
    openModal({ title: "Aperçu simplifié (non publié)", size: "modal-full",
      body: h("div", {}, h("p", { class: "muted" }, "Aperçu approximatif du contenu actuel du formulaire, avant enregistrement et publication. La mise en page finale peut légèrement différer."), frame),
      actions: [{ label: "Fermer", kind: "btn-primary", value: true }] });
  }

  // ---------------------------------------------------------------- Assistants
  async newPageWizard() {
    const data = this.store.data;
    const type = h("select", { class: "input" },
      h("option", { value: "topicpage" }, "Article dans une rubrique (géographie, histoire, culture…)"),
      h("option", { value: "place" }, "Lieu à visiter, rattaché à une île"),
      h("option", { value: "experience" }, "Expérience"),
      h("option", { value: "itinerary" }, "Itinéraire"),
      h("option", { value: "practical" }, "Info pratique"),
      h("option", { value: "tale" }, "Conte ou récit (Hale halele)"),
      h("option", { value: "quiz" }, "Quiz (Loisirs)"),
      h("option", { value: "topic" }, "Nouvelle rubrique"),
      h("option", { value: "island" }, "Nouvelle île"));
    const parentTopic = h("select", { class: "input" }, data.topics.map((t) => h("option", { value: t.slug }, t.name)));
    const parentIsland = h("select", { class: "input" }, data.islands.map((i) => h("option", { value: i.slug }, i.name)));
    const topicRow = h("label", { class: "field-label" }, "Dans la rubrique", parentTopic);
    const islandRow = h("label", { class: "field-label", hidden: true }, "Sur l'île", parentIsland);
    type.addEventListener("change", () => { topicRow.hidden = type.value !== "topicpage"; islandRow.hidden = type.value !== "place"; });
    const choice = await openModal({ title: "Ajouter une page", body: h("div", {}, h("label", { class: "field-label" }, "Type de page", type), topicRow, islandRow),
      actions: [{ label: "Annuler", value: null }, { label: "Continuer", kind: "btn-primary", value: () => ({ type: type.value, parent: type.value === "topicpage" ? parentTopic.value : type.value === "place" ? parentIsland.value : null }) }] });
    if (!choice) return;
    const id = await A.create(this, choice.type, choice.parent);
    if (id) this.go(`#/edit/${id}`);
  }

  async uploadWizard() {
    const file = await new Promise((resolve) => {
      const input = h("input", { type: "file", accept: "image/jpeg,image/png,image/webp", hidden: true });
      input.addEventListener("change", () => resolve(input.files[0] || null));
      document.body.append(input);
      input.click();
      setTimeout(() => input.remove(), 60000);
    });
    if (!file) return null;
    if (file.size > 25 * 1024 * 1024) { toast("Image trop lourde (25 Mo maximum).", "error"); return null; }
    let resized;
    try {
      resized = await resizeImage(file, 2000, 0.85);
    } catch {
      toast("Ce fichier n'a pas pu être lu comme une image.", "error");
      return null;
    }
    const cats = this.store.data.settings.media_categories || {};
    const caption = h("textarea", { class: "input", rows: 2 });
    const author = h("input", { type: "text", class: "input" });
    const license = h("select", { class: "input" }, ["Photo personnelle (tous droits accordés au site)", "CC BY 4.0", "CC BY-SA 4.0", "Domaine public", "Autre (préciser dans le crédit)"].map((l) => h("option", {}, l)));
    const cat = h("select", { class: "input" }, Object.entries(cats).map(([k, l]) => h("option", { value: k }, l)));
    const inGallery = h("input", { type: "checkbox", checked: true });
    const rights = h("input", { type: "checkbox" });
    const form = h("div", { class: "upload-form" },
      h("img", { src: resized.url, alt: "", class: "upload-preview" }),
      h("div", {},
        h("p", { class: "muted" }, `${file.name} → ${resized.width} × ${resized.height} px, ${Math.round(resized.bytes / 1024)} Ko après optimisation`),
        h("label", { class: "field-label" }, "Légende (obligatoire)", caption),
        h("label", { class: "field-label" }, "Auteur / crédit (obligatoire)", author),
        h("label", { class: "field-label" }, "Licence", license),
        h("label", { class: "field-label" }, "Catégorie (galerie)", cat),
        h("label", { class: "check" }, inGallery, " Afficher dans la galerie photos"),
        h("label", { class: "check" }, rights, " Je certifie avoir le droit de publier cette image (photo personnelle ou licence libre).")));
    const ok = await openModal({ title: "Téléverser une image", body: form, size: "modal-wide",
      actions: [{ label: "Annuler", value: false }, { label: "Continuer", kind: "btn-primary", value: true, validate: () => {
        if (!caption.value.trim() || !author.value.trim()) { toast("La légende et l'auteur sont obligatoires.", "error"); return false; }
        if (!rights.checked) { toast("Merci de confirmer que vous avez le droit de publier cette image.", "error"); return false; }
        return true;
      } }] });
    if (!ok) return null;
    const base = M.slugify(caption.value).slice(0, 40) || "image";
    const stamp = new Date().toISOString().slice(0, 10).replace(/-/g, "");
    const fileName = `${stamp}-${base}-${Math.random().toString(36).slice(2, 6)}.${resized.ext}`;
    const key = M.uniqueSlug(Object.keys(this.store.data.media), base).replace(/-/g, "_");
    const confirmed = await confirmImpact({
      title: "Envoyer l'image ?", severity: "info",
      intro: `Le fichier « ${fileName} » (${Math.round(resized.bytes / 1024)} Ko) sera envoyé tout de suite dans la médiathèque du dépôt GitHub.`,
      sections: [{ heading: "Ce qui va se passer :", items: [
        "L'image est ajoutée à la médiathèque (brouillon) et devient utilisable dans toutes les pages.",
        inGallery.checked ? "Après publication, elle apparaîtra aussi dans la galerie photos et la page des crédits." : "Après publication, elle apparaîtra dans la page des crédits.",
        "Elle ne s'affiche sur une page que si vous la choisissez dans l'éditeur de cette page.",
      ] }],
      confirmLabel: "Envoyer l'image",
    });
    if (!confirmed) return null;
    try {
      toast("Envoi de l'image…", "info");
      const src = await this.store.uploadImage(fileName, resized.base64, resized.url);
      this.store.apply(`Ajout de l'image « ${caption.value.trim()} »`, (d) => {
        d.media[key] = { src, caption: caption.value.trim(), island: cat.value, author: author.value.trim(), license: license.value, ...(inGallery.checked ? {} : { gallery: false }) };
      });
      toast("Image ajoutée à la médiathèque");
      return key;
    } catch (err) {
      toast(`Échec de l'envoi : ${err.message}`, "error");
      return null;
    }
  }

  async commonsWizard() {
    const cats = this.store.data.settings.media_categories || {};
    const file = h("input", { type: "text", class: "input", placeholder: "Exemple : Moroni_beach.jpg ou adresse de la page Commons" });
    const caption = h("textarea", { class: "input", rows: 2 });
    const author = h("input", { type: "text", class: "input" });
    const license = h("input", { type: "text", class: "input", placeholder: "Exemple : CC BY-SA 4.0" });
    const cat = h("select", { class: "input" }, Object.entries(cats).map(([k, l]) => h("option", { value: k }, l)));
    const preview = h("img", { class: "upload-preview", alt: "", hidden: true });
    const normalize = (v) => decodeURIComponent((v || "").trim().replace(/^.*(File:|Fichier:|FilePath\/)/, "").split("?")[0]).replace(/ /g, "_");
    file.addEventListener("change", () => { const f = normalize(file.value); if (f && !/\.(webm|ogv)$/i.test(f)) { preview.src = `${COMMONS}${encodeURIComponent(f)}?width=500`; preview.hidden = false; } });
    const ok = await openModal({ title: "Ajouter un média depuis Wikimedia Commons", size: "modal-wide",
      body: h("div", { class: "upload-form" }, preview, h("div", {},
        h("p", { class: "muted" }, "Wikimedia Commons ne contient que des médias sous licence libre. Copiez le nom du fichier (ou l'adresse de sa page) et reportez l'auteur et la licence indiqués sur Commons."),
        h("label", { class: "field-label" }, "Nom du fichier sur Commons", file),
        h("label", { class: "field-label" }, "Légende (obligatoire)", caption),
        h("label", { class: "field-label" }, "Auteur", author),
        h("label", { class: "field-label" }, "Licence", license),
        h("label", { class: "field-label" }, "Catégorie (galerie)", cat))),
      actions: [{ label: "Annuler", value: false }, { label: "Continuer", kind: "btn-primary", value: true, validate: () => {
        if (!normalize(file.value) || !caption.value.trim()) { toast("Le nom du fichier et la légende sont obligatoires.", "error"); return false; }
        return true;
      } }] });
    if (!ok) return null;
    const f = normalize(file.value);
    const isVideo = /\.(webm|ogv)$/i.test(f);
    const key = M.uniqueSlug(Object.keys(this.store.data.media), caption.value).replace(/-/g, "_");
    const confirmed = await confirmImpact({
      title: "Ajouter ce média ?", severity: "info",
      intro: `« ${f} » sera ajouté à la médiathèque (brouillon).`,
      sections: [{ heading: "Ce qui va se passer :", items: [
        "Le média devient utilisable dans les pages.",
        isVideo ? "C'est une vidéo : ajoutez-la dans « Vidéos » pour l'afficher sur la page vidéos." : "Après publication, il apparaîtra dans la galerie et les crédits.",
        "Vérifiez que l'aperçu s'affiche : un nom de fichier erroné donnera une image vide.",
      ] }],
      confirmLabel: "Ajouter",
    });
    if (!confirmed) return null;
    this.store.apply(`Ajout du média Commons « ${caption.value.trim()} »`, (d) => {
      d.media[key] = { file: f, caption: caption.value.trim(), island: cat.value,
        ...(author.value.trim() ? { author: author.value.trim() } : {}), ...(license.value.trim() ? { license: license.value.trim() } : {}),
        ...(isVideo ? { kind: "video", gallery: false } : {}) };
    });
    toast("Média ajouté à la médiathèque");
    return key;
  }

  // ---------------------------------------------------------------- Suivi de la mise en ligne
  rememberPublish(sha) {
    localStorage.setItem(PUBLISH_KEY, JSON.stringify({ sha, at: new Date().toISOString() }));
  }

  lastPublish() {
    try { return JSON.parse(localStorage.getItem(PUBLISH_KEY)); } catch { return null; }
  }

  buildStatusNode(last) {
    const node = h("div", { class: "build-status" }, h("p", {}, `Publiée le ${formatDate(last.at)}.`), h("p", { class: "muted" }, "Vérification de la mise en ligne…"));
    const started = Date.now();
    const poll = async () => {
      if (!node.isConnected && Date.now() - started > 2000) return;
      let run = null;
      try { run = await this.store.buildStatus(last.sha); } catch { /* droits Actions absents */ }
      const status = node.querySelector(".muted") || node.appendChild(h("p", { class: "muted" }));
      if (!run) {
        status.textContent = Date.now() - started > 120000
          ? "Aucune génération trouvée. Vérifiez l'onglet « Actions » du dépôt GitHub (ou les droits « Actions » du jeton)."
          : "La génération du site va démarrer…";
      } else if (run.status !== "completed") {
        status.textContent = "⏳ Génération du site en cours (1 à 3 minutes)…";
      } else {
        status.textContent = run.conclusion === "success"
          ? "✅ Le site public est à jour."
          : `❌ La génération a échoué (${run.conclusion}). Ouvrez le détail sur GitHub ou restaurez la version précédente.`;
        status.append(" ", h("a", { href: run.html_url, target: "_blank", rel: "noopener" }, "Détails ↗"));
        return;
      }
      if (Date.now() - started < 10 * 60000) setTimeout(poll, 8000);
    };
    setTimeout(poll, 500);
    return node;
  }
}

// ---------------------------------------------------------------- Réduction des images avant envoi
function resizeImage(file, maxSize, quality) {
  return new Promise((resolve, reject) => {
    const url = URL.createObjectURL(file);
    const img = new Image();
    img.onload = () => {
      const scale = Math.min(1, maxSize / Math.max(img.width, img.height));
      const width = Math.round(img.width * scale);
      const height = Math.round(img.height * scale);
      const canvas = document.createElement("canvas");
      canvas.width = width;
      canvas.height = height;
      canvas.getContext("2d").drawImage(img, 0, 0, width, height);
      const png = file.type === "image/png" && file.size < 600 * 1024;
      const type = png ? "image/png" : "image/jpeg";
      canvas.toBlob((blob) => {
        if (!blob) { reject(new Error("conversion impossible")); return; }
        const reader = new FileReader();
        reader.onload = () => resolve({
          base64: reader.result.split(",")[1], url: URL.createObjectURL(blob), width, height, bytes: blob.size, ext: png ? "png" : "jpg",
        });
        reader.readAsDataURL(blob);
      }, type, quality);
      URL.revokeObjectURL(url);
    };
    img.onerror = reject;
    img.src = url;
  });
}

// ---------------------------------------------------------------- Lancement
(async () => {
  const root = document.getElementById("app");
  try {
    const config = await fetch("config.json", { cache: "no-store" }).then((r) => r.json());
    await new App(root, config).start();
  } catch (err) {
    root.textContent = `Impossible de démarrer l'administration : ${err.message}`;
  }
})();
