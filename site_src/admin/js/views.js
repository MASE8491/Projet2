// Écrans du back-office.

import { h, clear, confirmImpact, openModal, toast, ask, formatDate } from "./ui.js";
import { buildForm } from "./fields.js";
import * as M from "./model.js";
import * as A from "./actions.js";
import { ConflictError } from "./store.js";

const statusBadge = (data, id) => {
  const e = M.getEntity(data, id);
  if (!M.isPublished(e)) return h("span", { class: "badge badge-hidden" }, "Masquée");
  if (!M.isOnline(data, id)) return h("span", { class: "badge badge-hidden" }, "Masquée par son parent");
  return h("span", { class: "badge badge-online" }, "En ligne");
};

/** Éléments dont le contenu diffère de la version publiée. */
export function changedIds(store) {
  const ids = new Set();
  const collect = (data) => {
    const out = new Map();
    M.allEntityIds(data).forEach((id) => out.set(id, JSON.stringify(M.getEntity(data, id))));
    Object.keys(M.FIXED).forEach((k) => out.set(`fixed:${k}`, JSON.stringify(data.pages[k])));
    Object.keys(M.DOCS).forEach((k) => out.set(`doc:${k}`, JSON.stringify(data[M.DOCS[k].file])));
    Object.keys(M.LISTS).forEach((k) => out.set(`list:${k}`, JSON.stringify(data[M.LISTS[k].file])));
    Object.keys(data.media).forEach((k) => out.set(`media:${k}`, JSON.stringify(data.media[k])));
    return out;
  };
  const a = collect(store.base);
  const b = collect(store.data);
  for (const [id, v] of b) if (a.get(id) !== v) ids.add(id);
  for (const id of a.keys()) if (!b.has(id)) ids.add(id);
  return [...ids].map((id) => ({ id, status: !a.has(id) ? "ajouté" : !b.has(id) ? "supprimé" : "modifié" }));
}

const isChanged = (store, id) => {
  const before = M.getEntity(store.base, id);
  const after = M.getEntity(store.data, id);
  return JSON.stringify(before) !== JSON.stringify(after);
};

// ==================================================================== Tableau de bord

export function dashboard(app) {
  const { store } = app;
  const data = store.data;
  const pending = changedIds(store);
  const { errors } = M.validate(data, app.config.reserved_slugs);
  const ids = M.allEntityIds(data);
  const hidden = ids.filter((id) => !M.isOnline(data, id)).length;
  const last = app.lastPublish();
  return h("div", { class: "view" },
    h("h1", {}, `Bonjour${store.user ? " " + (store.user.name || store.user.login) : ""} 👋`),
    h("p", { class: "lead" }, "Bienvenue dans l'administration du site. Toutes vos modifications restent en brouillon jusqu'à ce que vous cliquiez sur « Publier »."),
    h("div", { class: "cards" },
      h("div", { class: `card ${pending.length ? "card-warn" : ""}` },
        h("p", { class: "card-num" }, pending.length),
        h("p", {}, "élément(s) modifié(s) non publié(s)"),
        pending.length ? h("a", { class: "btn btn-primary btn-small", href: "#/publier" }, "Vérifier et publier") : h("p", { class: "muted" }, "Tout est publié.")),
      h("div", { class: "card" },
        h("p", { class: "card-num" }, ids.length - hidden),
        h("p", {}, `page(s) en ligne · ${hidden} masquée(s)`),
        h("a", { class: "btn btn-secondary btn-small", href: "#/arborescence" }, "Voir l'arborescence")),
      h("div", { class: "card" },
        h("p", { class: "card-num" }, Object.keys(data.media).length),
        h("p", {}, "images et vidéos"),
        h("a", { class: "btn btn-secondary btn-small", href: "#/medias" }, "Ouvrir la médiathèque")),
      h("div", { class: `card ${errors.length ? "card-error" : ""}` },
        h("p", { class: "card-num" }, errors.length),
        h("p", {}, "problème(s) bloquant(s) avant publication"),
        errors.length ? h("a", { class: "btn btn-secondary btn-small", href: "#/publier" }, "Voir le détail") : h("p", { class: "muted" }, "Aucun problème détecté."))),
    last ? h("div", { class: "panel" }, h("h2", {}, "Dernière publication"), app.buildStatusNode(last)) : null,
    h("div", { class: "panel" },
      h("h2", {}, "Actions rapides"),
      h("div", { class: "btn-row" },
        h("a", { class: "btn btn-secondary", href: "#/edit/doc:home" }, "🏠 Modifier l'accueil"),
        h("a", { class: "btn btn-secondary", href: "#/arborescence" }, "🗂️ Modifier une page"),
        h("button", { type: "button", class: "btn btn-secondary", onclick: () => app.newPageWizard() }, "➕ Ajouter une page"),
        h("a", { class: "btn btn-secondary", href: "#/medias" }, "🖼️ Ajouter une image"),
        h("a", { class: "btn btn-secondary", href: "#/edit/doc:navigation" }, "🧭 Modifier le menu"),
        h("a", { class: "btn btn-secondary", href: app.siteUrl("index.html"), target: "_blank", rel: "noopener" }, "🌍 Voir le site"))),
    h("div", { class: "panel" },
      h("h2", {}, "Comment ça marche ?"),
      h("ol", { class: "steps" },
        h("li", {}, h("strong", {}, "Modifiez"), " une page, une image ou le menu. Chaque changement est expliqué dans une fenêtre avant d'être appliqué."),
        h("li", {}, h("strong", {}, "Vérifiez"), " avec le bouton « Aperçu » de l'éditeur. Vos changements sont gardés en brouillon dans ce navigateur."),
        h("li", {}, h("strong", {}, "Publiez"), " : le bouton « Publier » envoie toutes les modifications d'un coup."),
        h("li", {}, h("strong", {}, "Patientez"), " 1 à 3 minutes : le site public est régénéré automatiquement."))),
  );
}

// ==================================================================== Arborescence

export function tree(app) {
  const { store } = app;
  const data = store.data;
  const root = h("div", { class: "view" },
    h("div", { class: "view-head" },
      h("div", {}, h("h1", {}, "Arborescence du site"),
        h("p", { class: "lead" }, "Toutes les pages, dans l'ordre où elles apparaissent. Utilisez les boutons pour modifier, réordonner, déplacer, masquer ou ajouter des pages.")),
      h("button", { type: "button", class: "btn btn-primary", onclick: () => app.newPageWizard() }, "➕ Ajouter une page")),
  );

  const actions = (id, { canMove = true, relocate = false, add = null } = {}) => {
    const p = M.parseId(id);
    const e = M.getEntity(data, id);
    const btn = (label, title, fn, cls = "") => h("button", { type: "button", class: `tree-btn ${cls}`, title, "aria-label": title, onclick: fn }, label);
    const run = (fn) => async () => { const r = await fn(); if (r) app.render(); };
    return h("div", { class: "tree-actions" },
      h("a", { class: "tree-btn tree-edit", href: `#/edit/${id}` }, "✏️ Modifier"),
      canMove ? btn("↑", "Monter", run(() => A.move(app, id, -1))) : null,
      canMove ? btn("↓", "Descendre", run(() => A.move(app, id, +1))) : null,
      relocate ? btn("⇄ Déplacer", p.type === "topicpage" ? "Déplacer dans une autre rubrique" : "Rattacher à une autre île", run(() => A.relocate(app, id))) : null,
      btn(M.isPublished(e) ? "🙈 Masquer" : "👁️ Remettre en ligne", M.isPublished(e) ? "Masquer la page" : "Remettre la page en ligne", run(() => A.togglePublished(app, id))),
      btn("🔗 Adresse", "Changer l'adresse de la page", async () => { const r = await A.changeSlug(app, id); if (r) app.render(); }),
      btn("🗑️", "Supprimer", run(() => A.remove(app, id)), "tree-danger"),
      add ? btn(`➕ ${add.label}`, add.label, async () => { const nid = await A.create(app, add.type, add.parent); if (nid) app.go(`#/edit/${nid}`); }) : null,
    );
  };

  const node = (id, { emoji, extra, children, opts, simpleActions } = {}) => {
    const title = M.titleOf(data, id);
    const path = M.pathOf(data, id);
    return h("li", { class: "tree-node" },
      h("div", { class: `tree-row ${isChanged(store, id) ? "is-changed" : ""}` },
        h("span", { class: "tree-title" }, emoji ? emoji + " " : "", h("a", { href: `#/edit/${id}` }, title)),
        path ? h("code", { class: "tree-path" }, path) : null,
        M.TYPES[M.parseId(id).type] ? statusBadge(data, id) : null,
        isChanged(store, id) ? h("span", { class: "badge badge-draft" }, "Modifiée") : null,
        extra || null,
        simpleActions ? h("div", { class: "tree-actions" }, h("a", { class: "tree-btn tree-edit", href: `#/edit/${id}` }, "✏️ Modifier"), simpleActions) : actions(id, opts)),
      children && children.length ? h("ul", { class: "tree-children" }, children) : null);
  };
  const group = (label, emoji, fixedId, children, addBtn) => h("li", { class: "tree-node tree-group" },
    h("div", { class: "tree-row" },
      h("span", { class: "tree-title" }, `${emoji} `, fixedId ? h("a", { href: `#/edit/${fixedId}` }, label) : label),
      fixedId && M.pathOf(data, fixedId) ? h("code", { class: "tree-path" }, M.pathOf(data, fixedId)) : null,
      h("div", { class: "tree-actions" },
        fixedId ? h("a", { class: "tree-btn tree-edit", href: `#/edit/${fixedId}` }, "✏️ Modifier la page") : null,
        addBtn || null)),
    children.length ? h("ul", { class: "tree-children" }, children) : null);
  const addButton = (label, type, parent) => h("button", { type: "button", class: "tree-btn", onclick: async () => {
    const nid = await A.create(app, type, parent);
    if (nid) app.go(`#/edit/${nid}`);
  } }, `➕ ${label}`);

  // Groupe sans page propre (spots, institutions d'une île) : chemin affiché et bouton d'ajout
  const subGroup = (label, emoji, path, editId, children, addBtn) => h("li", { class: "tree-node tree-group" },
    h("div", { class: "tree-row" },
      h("span", { class: "tree-title" }, `${emoji} `, h("a", { href: `#/edit/${editId}` }, label)),
      h("code", { class: "tree-path" }, path),
      h("div", { class: "tree-actions" }, h("a", { class: "tree-btn tree-edit", href: `#/edit/${editId}` }, "✏️ Textes de la page"), addBtn)),
    children.length ? h("ul", { class: "tree-children" }, children) : null);
  const scopeBadge = (x) => (x.scope && x.scope !== "ile" ? h("span", { class: "badge" }, x.scope === "union" ? "Union" : "Archipel") : null);
  const islandNodes = data.islands.map((island) => {
    const placeSlugs = [...(island.places || []), ...data.places.filter((p) => p.island === island.slug && !(island.places || []).includes(p.slug)).map((p) => p.slug)];
    const spots = data.spots.filter((x) => x.island === island.slug);
    const insts = data.institutions.filter((x) => x.island === island.slug);
    return node(`island:${island.slug}`, {
      emoji: "🏝️",
      opts: { add: { label: "Lieu", type: "place", parent: island.slug } },
      children: [
        ...placeSlugs.filter((s) => data.places.some((p) => p.slug === s)).map((s) => node(`place:${s}`, { emoji: "📍", opts: { relocate: true } })),
        subGroup(`Spots & bons plans (${spots.length})`, "⭐", `iles/${island.slug}/bons-plans.html`, `island:${island.slug}`,
          spots.map((x) => node(`spot:${x.slug}`, { emoji: "⭐", opts: { relocate: true } })), addButton("Spot", "spot", island.slug)),
        subGroup(`Vie publique & institutions (${insts.length})`, "🏛️", `iles/${island.slug}/vie-publique.html`, `island:${island.slug}`,
          insts.map((x) => node(`institution:${x.slug}`, { emoji: "🏛️", extra: scopeBadge(x), opts: { relocate: true } })), addButton("Institution", "institution", island.slug)),
      ],
    });
  });
  const topicNodes = data.topics.map((t) => node(`topic:${t.slug}`, {
    emoji: "📚",
    opts: { add: { label: "Article", type: "topicpage", parent: t.slug } },
    children: t.pages.map((pg) => node(`topicpage:${t.slug}/${pg.slug}`, { emoji: "📄", opts: { relocate: true } })),
  }));
  const listNodes = (type, emoji) => data[M.TYPES[type].file].map((e) => node(`${type}:${e.slug}`, { emoji }));
  const docLink = (id, emoji) => node(id, { emoji, simpleActions: " " });

  root.append(h("ul", { class: "tree" },
    docLink("doc:home", "🏠"),
    group("Les îles", "🗺️", "fixed:iles", [...islandNodes, docLink("fixed:bonsplans", "⭐"), docLink("fixed:viepublique", "🏛️")], addButton("Île", "island")),
    group("Rubriques de découverte", "📚", null, [
      ...topicNodes,
      group("Sources & bibliographie", "📖", "fixed:bibliographie", [docLink("list:bibliography", "📖"), docLink("list:timeline", "🕰️")]),
    ], addButton("Rubrique", "topic")),
    group("Hale halele : contes et récits", "🌙", "fixed:contes",
      Object.entries(M.TALE_KINDS).map(([kind, label]) => group(label, "🌙", null,
        data.tales.filter((t) => t.kind === kind).map((t) => node(`tale:${t.slug}`, { emoji: "🌙" })))),
      addButton("Conte ou récit", "tale")),
    group("Loisirs", "🎲", "fixed:loisirs", [
      ...listNodes("quiz", "❓"),
      group("Glossaire", "🔤", "fixed:glossaire", [docLink("list:glossary", "🔤")]),
      docLink("fixed:galerie", "🖼️"),
      group("Vidéos", "🎬", "fixed:videos", [docLink("doc:videos", "🎬")]),
    ], addButton("Quiz", "quiz")),
    group("Voyager", "🧳", "fixed:voyager", [
      group("Expériences", "🌊", "fixed:experiences", listNodes("experience", "🌊"), addButton("Expérience", "experience")),
      group("Itinéraires", "🧭", "fixed:itineraires", listNodes("itinerary", "🧭"), addButton("Itinéraire", "itinerary")),
      group("Préparer son voyage", "🧳", "fixed:preparer", listNodes("practical", "🧳"), addButton("Info pratique", "practical")),
      group("Agenda & saisons", "📅", "fixed:agenda", [docLink("list:events", "📅")]),
    ]),
    group("Pages annexes", "📎", null, ["contact", "credits", "mentions", "plan", "404"].map((k) => docLink(`fixed:${k}`, "📎"))),
    docLink("doc:navigation", "🧭"),
    docLink("doc:settings", "⚙️"),
  ));
  return root;
}

// ==================================================================== Éditeur

export function editor(app, id) {
  const { store } = app;
  const data = store.data;
  const entity = M.getEntity(data, id);
  if (!entity) return h("div", { class: "view" }, h("h1", {}, "Page introuvable"), h("p", {}, "Elle a peut-être été supprimée ou renommée."), h("a", { href: "#/arborescence" }, "← Retour à l'arborescence"));
  const p = M.parseId(id);
  const fields = M.schemaOf(id);
  const original = JSON.parse(JSON.stringify(entity));
  const ctx = app.fieldContext({ entity });
  const form = buildForm(fields, original, ctx);
  const path = M.pathOf(data, id);
  const title = M.titleOf(data, id);
  const isType = !!M.TYPES[p.type];

  app.setDirtyCheck(() => JSON.stringify(form.get()) !== JSON.stringify(original));

  const save = async () => {
    const value = form.get();
    const changes = M.diffFields(fields, original, value);
    if (!changes.length) { toast("Aucune modification à enregistrer.", "info"); return; }
    const missing = fields.filter((f) => f.required && (value[f.key] === "" || value[f.key] === undefined || value[f.key] === null));
    if (missing.length) {
      await openModal({ title: "Champs obligatoires", tone: "warning", body: h("div", {}, h("p", {}, "Merci de remplir :"), h("ul", {}, missing.map((f) => h("li", {}, f.label)))), actions: [{ label: "Compris", kind: "btn-primary", value: true }] });
      return;
    }
    let severity = "info";
    const notes = ["Rien ne change sur le site public tant que vous n'avez pas cliqué sur « Publier »."];
    const sections = [{ heading: "Champs modifiés :", items: changes }];
    if (p.type === "doc" && p.slug === "navigation") {
      severity = "warning";
      sections.push({ heading: "Pages concernées :", items: ["Toutes les pages du site (le menu et le pied de page sont communs)"] });
    } else if (p.type === "doc" && p.slug === "settings") {
      const danger = fields.filter((f) => f.danger && JSON.stringify(original[f.key]) !== JSON.stringify(value[f.key]));
      severity = danger.length ? "danger" : "warning";
      sections.push({ heading: "Pages concernées :", items: ["Toutes les pages du site"] });
      if (danger.length) notes.unshift(`⚠ Réglages avancés modifiés (${danger.map((f) => f.label).join(", ")}) : une erreur peut rendre le site ou cette administration inaccessibles. Ne modifiez ces champs que si vous savez ce que vous faites.`);
    } else if (id === "list:bibliography") {
      const before = new Map((original.items || []).map((b) => [b.id, b]));
      const after = new Set((value.items || []).map((b) => b.id));
      const lost = [...before.keys()].filter((rid) => rid && !after.has(rid));
      const touched = M.citingPages(data).filter((pg) => pg.refs.some((rid) => before.has(rid)));
      sections.push({ heading: "Pages qui affichent ces références :", items: [{ text: "Sources & bibliographie", sub: "bibliographie.html" },
        ...touched.map((pg) => ({ text: pg.title, sub: pg.path }))] });
      const broken = lost.flatMap((rid) => M.citationsOf(data, rid).map((pg) => `${pg.title} — cite « ${rid} »`));
      if (broken.length) {
        severity = "danger";
        sections.push({ heading: "⚠ Références supprimées ou renommées alors qu'elles sont citées :", items: broken });
        notes.unshift("La publication sera bloquée tant que ces pages citeront une référence absente. Rétablissez l'identifiant ou retirez la référence des pages concernées.");
      } else if (lost.length) severity = "warning";
    } else if (p.type === "media") {
      sections.push({ heading: "Pages où cette image apparaît :", items: M.appearsOn(data, id).map((x) => ({ text: x.title, sub: x.path })) });
    } else {
      let pages = path ? M.appearsOn(data, id) : [];
      // Une institution ou un spot peut changer de portée : on ajoute les pages touchées après la modification
      if (p.type === "institution" || p.type === "spot") {
        const after = JSON.parse(JSON.stringify(data));
        M.setEntity(after, id, value);
        M.appearsOn(after, id).forEach((x) => { if (!pages.some((y) => y.path === x.path)) pages = [...pages, x]; });
      }
      sections.push({ heading: "Pages mises à jour :", items: pages.map((x) => ({ text: x.title, sub: `${x.path} — ${x.why}` })), empty: path ? "Uniquement cette page" : "—" });
      if (isType && changes.some((c) => c.startsWith("Titre") || c.startsWith("Nom"))) {
        const menu = M.menuMentions(data, id);
        if (menu.length) sections.push({ heading: "Le nouveau titre apparaîtra aussi dans :", items: menu });
      }
    }
    const ok = await confirmImpact({
      title: `Enregistrer les modifications de « ${title} » ?`, severity, sections, notes,
      requireType: severity === "danger" ? "CONFIRMER" : undefined,
      confirmLabel: "Enregistrer",
    });
    if (!ok) return;
    store.apply(`Modification de « ${title} » : ${changes.join(", ")}`, (d) => M.setEntity(d, id, value));
    app.setDirtyCheck(null);
    toast("Modifications enregistrées dans le brouillon");
    app.render();
  };

  const preview = () => app.preview(id, form.get());
  const reset = async () => {
    if (JSON.stringify(form.get()) === JSON.stringify(original)) return;
    if (await ask("Annuler les changements du formulaire ?", "Les modifications non enregistrées de ce formulaire seront perdues.")) {
      app.setDirtyCheck(null);
      app.render();
    }
  };

  const side = isType ? h("aside", { class: "editor-side" },
    h("div", { class: "panel" },
      h("h2", {}, "État"),
      h("p", {}, statusBadge(data, id), isChanged(store, id) ? h("span", { class: "badge badge-draft" }, "Modifiée") : null),
      path ? h("p", { class: "muted" }, "Adresse : ", h("code", {}, path)) : null,
      h("div", { class: "btn-col" },
        h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => { if (await app.guardLeave() && await A.togglePublished(app, id)) app.render(); } },
          M.isPublished(entity) ? "🙈 Masquer la page" : "👁️ Remettre en ligne"),
        h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => { if (!(await app.guardLeave())) return; const r = await A.changeSlug(app, id); if (r) app.go(`#/edit/${r}`); } }, "🔗 Changer l'adresse"),
        ["place", "topicpage", "spot", "institution"].includes(p.type) ? h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => { if (!(await app.guardLeave())) return; const r = await A.relocate(app, id); if (r) app.go(`#/edit/${r}`); } }, "⇄ Déplacer") : null,
        h("button", { type: "button", class: "btn btn-danger btn-small", onclick: async () => { if (!(await app.guardLeave())) return; if (await A.remove(app, id)) app.go("#/arborescence"); } }, "🗑️ Supprimer"))),
    h("div", { class: "panel" },
      h("h2", {}, "Où apparaît cette page ?"),
      h("ul", { class: "small-list" }, M.appearsOn(data, id).map((x) => h("li", {}, x.title, h("small", {}, ` — ${x.why}`)))))) : null;

  return h("div", { class: "view" },
    h("div", { class: "view-head sticky-head" },
      h("div", {},
        h("p", { class: "kicker" }, M.typeLabel(id), path ? [" · ", h("a", { href: app.siteUrl(path), target: "_blank", rel: "noopener" }, "voir en ligne ↗")] : null),
        h("h1", {}, title)),
      h("div", { class: "btn-row" },
        h("button", { type: "button", class: "btn btn-secondary", onclick: reset }, "Annuler"),
        path ? h("button", { type: "button", class: "btn btn-secondary", onclick: preview }, "👁️ Aperçu") : null,
        h("button", { type: "button", class: "btn btn-primary", onclick: save }, "💾 Enregistrer"))),
    h("div", { class: `editor ${side ? "with-side" : ""}` }, h("div", { class: "editor-main panel" }, form.node), side));
}

// ==================================================================== Médiathèque

export function mediaLibrary(app, { picker = false, kind = null, onPick = null } = {}) {
  const { store } = app;
  const data = store.data;
  let query = "";
  let cat = "";
  let k = kind || "";
  const grid = h("div", { class: "media-grid" });
  const render = () => {
    clear(grid);
    const items = Object.entries(data.media).filter(([key, m]) => {
      const mk = m.kind || "image";
      if (k && mk !== k) return false;
      if (cat && m.island !== cat) return false;
      if (query && !(`${key} ${m.caption} ${m.author || ""}`.toLowerCase().includes(query.toLowerCase()))) return false;
      return true;
    });
    if (!items.length) grid.append(h("p", { class: "muted" }, "Aucun média ne correspond."));
    items.forEach(([key, m]) => {
      const uses = picker ? null : M.mediaUsages(data, key).length;
      grid.append(h("button", { type: "button", class: "media-card", onclick: () => (picker ? onPick(key) : app.go(`#/media/${encodeURIComponent(key)}`)) },
        (m.kind || "image") === "image" ? h("img", { src: app.thumb(key), alt: "", loading: "lazy" }) : h("div", { class: "media-video" }, "🎬"),
        h("span", { class: "media-caption" }, m.caption),
        uses !== null ? h("span", { class: `badge ${uses ? "badge-online" : "badge-hidden"}` }, uses ? `utilisée ${uses}×` : "non utilisée") : null));
    });
  };
  const search = h("input", { type: "search", class: "input", placeholder: "Rechercher une image…", oninput: (e) => { query = e.target.value; render(); } });
  const cats = h("select", { class: "input", onchange: (e) => { cat = e.target.value; render(); } },
    h("option", { value: "" }, "Toutes les catégories"),
    Object.entries(data.settings.media_categories || {}).map(([c, label]) => h("option", { value: c }, label)));
  const kinds = kind ? null : h("select", { class: "input", onchange: (e) => { k = e.target.value; render(); } },
    h("option", { value: "" }, "Images et vidéos"), h("option", { value: "image" }, "Images"), h("option", { value: "video" }, "Vidéos"));
  render();
  const toolbar = h("div", { class: "media-toolbar" }, search, cats, kinds,
    h("button", { type: "button", class: "btn btn-primary btn-small", onclick: async () => { const key = await app.uploadWizard(); if (key) { if (picker) onPick(key); else app.render(); } } }, "⬆️ Téléverser une image"),
    h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => { const key = await app.commonsWizard(); if (key) { if (picker) onPick(key); else app.render(); } } }, "➕ Depuis Wikimedia Commons"));
  if (picker) return h("div", { class: "media-picker" }, toolbar, grid);
  return h("div", { class: "view" },
    h("h1", {}, "Médiathèque"),
    h("p", { class: "lead" }, "Toutes les images et vidéos du site. Cliquez sur une image pour modifier sa légende, ses crédits ou voir où elle est utilisée."),
    toolbar, grid);
}

export function mediaEditor(app, key) {
  const { store } = app;
  const data = store.data;
  const m = data.media[key];
  if (!m) return h("div", { class: "view" }, h("h1", {}, "Média introuvable"), h("a", { href: "#/medias" }, "← Retour à la médiathèque"));
  const id = `media:${key}`;
  const uses = M.mediaUsages(data, key);
  const editorNode = editor(app, id);
  const replace = async () => {
    const other = await app.pickMedia({ kind: m.kind || "image" });
    if (!other || other === key) return;
    const ok = await confirmImpact({
      title: "Remplacer cette image partout ?", severity: "warning",
      intro: `Toutes les pages qui utilisent « ${m.caption} » utiliseront « ${data.media[other].caption} ».`,
      sections: [{ heading: "Pages modifiées :", items: uses.map((u) => u.title), empty: "Aucune page n'utilise cette image" }],
      confirmLabel: "Remplacer partout",
    });
    if (!ok) return;
    store.apply(`Image « ${m.caption} » remplacée par « ${data.media[other].caption} »`, (d) => {
      const rec = (v, k2) => {
        if (Array.isArray(v)) return v.map((x) => (x === key && (k2 === "gallery" || k2 === "items") ? other : rec(x, k2)));
        if (v && typeof v === "object") { for (const kk of Object.keys(v)) v[kk] = (["hero", "card", "media", "poster", "spots_hero", "public_hero"].includes(kk) && v[kk] === key) ? other : rec(v[kk], kk); return v; }
        return v;
      };
      for (const f of Object.keys(d)) if (f !== "media") d[f] = rec(d[f], null);
    });
    toast("Image remplacée (en attente de publication)");
    app.render();
  };
  const del = async () => {
    const ok = await confirmImpact({
      title: `Supprimer « ${m.caption} » de la médiathèque ?`, severity: "danger",
      intro: "Le média ne sera plus proposé et disparaîtra de la galerie et des crédits après publication.",
      sections: [{ heading: "Utilisations :", items: uses.map((u) => u.title), empty: "Aucune — suppression possible" }],
      blocked: uses.length ? "Ce média est encore utilisé. Remplacez-le d'abord partout (bouton « Remplacer partout »), puis supprimez-le." : null,
      notes: m.src ? ["Le fichier image reste stocké dans le dépôt GitHub (il pourra être réutilisé ou supprimé manuellement)."] : [],
      requireType: "SUPPRIMER", confirmLabel: "Supprimer",
    });
    if (!ok) return;
    store.apply(`Suppression du média « ${m.caption} »`, (d) => { delete d.media[key]; });
    toast("Média supprimé (en attente de publication)");
    app.go("#/medias");
  };
  return h("div", {},
    h("div", { class: "view media-detail" },
      h("a", { href: "#/medias", class: "back" }, "← Médiathèque"),
      h("div", { class: "media-detail-grid" },
        (m.kind || "image") === "image" ? h("img", { src: app.thumb(key, 960), alt: m.caption, class: "media-large" }) : h("video", { src: app.fileUrl(key), controls: true, class: "media-large", preload: "none" }),
        h("div", {},
          h("p", {}, h("strong", {}, "Identifiant : "), h("code", {}, key)),
          h("p", {}, h("strong", {}, "Fichier : "), m.src ? h("code", {}, m.src) : h("a", { href: `https://commons.wikimedia.org/wiki/File:${encodeURIComponent(m.file)}`, target: "_blank", rel: "noopener" }, `${m.file} (Wikimedia Commons) ↗`)),
          h("h2", {}, `Utilisations (${uses.length})`),
          h("ul", { class: "small-list" }, uses.length ? uses.map((u) => h("li", {}, h("a", { href: `#/edit/${u.id}` }, u.title))) : h("li", { class: "muted" }, "Non utilisée")),
          h("div", { class: "btn-row" },
            h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: replace }, "⇄ Remplacer partout"),
            h("button", { type: "button", class: "btn btn-danger btn-small", onclick: del }, "🗑️ Supprimer"))))),
    editorNode);
}

// ==================================================================== Publication

export function publishView(app) {
  const { store } = app;
  const pending = changedIds(store);
  const { errors, warnings } = M.validate(store.data, app.config.reserved_slugs);
  const message = h("textarea", { class: "input", rows: 3 });
  message.value = store.log.length ? `Administration : ${store.log.slice(-3).map((l) => l.text).join(" ; ")}`.slice(0, 300) : "Administration : mise à jour du contenu";
  const publish = async () => {
    const affected = new Map();
    pending.forEach(({ id }) => {
      // Pages concernées avant ET après la modification (déplacement, changement de portée, suppression…)
      [store.base, store.data].forEach((data) => {
        try { if (M.getEntity(data, id)) M.appearsOn(data, id).forEach((x) => affected.set(x.path, x.title)); } catch { /* document sans page */ }
      });
      if (id === "doc:navigation" || id === "doc:settings") affected.set("*", "Toutes les pages du site");
    });
    const ok = await confirmImpact({
      title: "Publier sur le site public ?", severity: "warning",
      intro: `${pending.length} élément(s) modifié(s) seront mis en ligne. Le site public sera régénéré automatiquement (1 à 3 minutes).`,
      sections: [
        { heading: "Modifications publiées :", items: store.log.map((l) => l.text), empty: pending.map((x) => `${M.titleOf(x.status === "supprimé" ? store.base : store.data, x.id)} (${x.status})`).join(", ") },
        { heading: "Pages du site concernées :", items: [...affected.values()] },
        ...(warnings.length ? [{ heading: "Avertissements (la publication reste possible) :", items: warnings }] : []),
      ],
      notes: ["Une fois publiées, les modifications sont visibles par tous les visiteurs. Une version précédente peut toujours être restaurée depuis l'Historique."],
      requireCheck: "J'ai relu mes modifications et je veux les mettre en ligne.",
      confirmLabel: "Publier maintenant",
    });
    if (!ok) return;
    const btn = document.querySelector("[data-publish]");
    if (btn) { btn.disabled = true; btn.textContent = "Publication en cours…"; }
    try {
      const sha = await store.publish(message.value.trim() || "Administration : mise à jour du contenu");
      app.rememberPublish(sha);
      toast("Publié ! Le site sera à jour dans quelques minutes.");
      app.go("#/");
    } catch (err) {
      if (err instanceof ConflictError) {
        await openModal({ title: "Publication impossible : conflit", tone: "danger",
          body: h("div", {}, h("p", {}, "Ces fichiers ont été modifiés ailleurs (par une autre personne ou une autre fenêtre) depuis l'ouverture de l'administration :"),
            h("ul", {}, err.files.map((f) => h("li", {}, f))),
            h("p", {}, "Pour ne rien écraser : notez vos changements, cliquez sur « Annuler mes modifications » ci-dessous puis rechargez la page, et refaites vos modifications.")),
          actions: [{ label: "Compris", kind: "btn-primary", value: true }] });
      } else {
        await openModal({ title: "La publication a échoué", tone: "danger", body: h("p", {}, err.message), actions: [{ label: "Fermer", kind: "btn-primary", value: true }] });
      }
      app.render();
    }
  };
  const discard = async () => {
    const ok = await confirmImpact({
      title: "Annuler toutes les modifications non publiées ?", severity: "danger",
      intro: "Le brouillon sera effacé et le contenu reviendra à la version actuellement en ligne.",
      sections: [{ heading: "Modifications perdues :", items: store.log.map((l) => l.text) }],
      requireType: "ANNULER", confirmLabel: "Tout annuler",
    });
    if (!ok) return;
    store.discardDraft();
    app.setDirtyCheck(null);
    toast("Brouillon effacé");
    app.go("#/");
  };
  return h("div", { class: "view" },
    h("h1", {}, "Publier"),
    pending.length ? null : h("p", { class: "lead" }, "Aucune modification en attente : le site est à jour."),
    errors.length ? h("div", { class: "panel panel-error" }, h("h2", {}, "⛔ À corriger avant de publier"), h("ul", {}, errors.map((e) => h("li", {}, e)))) : null,
    warnings.length ? h("div", { class: "panel panel-warn" }, h("h2", {}, "⚠️ Avertissements"), h("ul", {}, warnings.map((w) => h("li", {}, w)))) : null,
    pending.length ? h("div", { class: "panel" },
      h("h2", {}, `Modifications en attente (${pending.length})`),
      h("ul", { class: "small-list" }, pending.map(({ id, status }) => h("li", {},
        h("span", { class: `badge badge-${status === "supprimé" ? "hidden" : "draft"}` }, status), " ",
        status === "supprimé" ? M.titleOf(store.base, id) : h("a", { href: id.startsWith("media:") ? `#/media/${encodeURIComponent(id.slice(6))}` : `#/edit/${id}` }, M.titleOf(store.data, id)),
        h("small", {}, ` — ${M.typeLabel(id)}`)))),
      h("h3", {}, "Journal"),
      h("ol", { class: "small-list" }, store.log.map((l) => h("li", {}, l.text, h("small", {}, ` — ${formatDate(l.at)}`)))),
      h("label", { class: "field-label" }, "Description de la publication (visible dans l'historique)", message),
      h("div", { class: "btn-row" },
        h("button", { type: "button", class: "btn btn-primary", "data-publish": "1", disabled: errors.length > 0, onclick: publish }, "🚀 Publier"),
        h("button", { type: "button", class: "btn btn-danger", onclick: discard }, "Annuler mes modifications"))) : null);
}

// ==================================================================== Historique

export function historyView(app) {
  const { store } = app;
  const list = h("div", { class: "panel" }, h("p", { class: "muted" }, "Chargement de l'historique…"));
  store.history().then((commits) => {
    clear(list);
    list.append(h("h2", {}, "Dernières versions du contenu"),
      h("table", { class: "table" },
        h("thead", {}, h("tr", {}, h("th", {}, "Date"), h("th", {}, "Auteur"), h("th", {}, "Description"), h("th", {}, ""))),
        h("tbody", {}, commits.map((c, i) => h("tr", {},
          h("td", {}, formatDate(c.commit.author.date)),
          h("td", {}, c.commit.author.name),
          h("td", {}, c.commit.message.split("\n")[0]),
          h("td", {}, i === 0 ? h("span", { class: "badge badge-online" }, "Version actuelle")
            : h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => {
              const label = `${formatDate(c.commit.author.date)} — ${c.commit.message.split("\n")[0]}`;
              const ok = await confirmImpact({
                title: "Restaurer cette version ?", severity: "danger",
                intro: `Tout le contenu du site (textes, menus, médiathèque, réglages) reviendra à la version du ${formatDate(c.commit.author.date)}.`,
                sections: [{ heading: "Conséquences :", items: [
                  "Les modifications publiées après cette date seront annulées (elles restent dans l'historique et pourront être restaurées à leur tour).",
                  ...(store.dirtyFiles().length ? ["Vos modifications NON publiées seront perdues."] : []),
                  "Le site public sera régénéré automatiquement.",
                ] }],
                requireType: "RESTAURER", confirmLabel: "Restaurer",
              });
              if (!ok) return;
              try {
                const sha = await store.restore(c.sha, label);
                app.rememberPublish(sha);
                toast("Version restaurée. Le site sera à jour dans quelques minutes.");
                app.go("#/");
              } catch (err) {
                toast(err.message, "error");
              }
            } }, "↩️ Restaurer")))))));
  }).catch((err) => { clear(list); list.append(h("p", { class: "error" }, err.message)); });
  return h("div", { class: "view" },
    h("h1", {}, "Historique"),
    h("p", { class: "lead" }, "Chaque publication est conservée. En cas d'erreur, vous pouvez revenir à une version précédente du contenu."),
    list);
}

// ==================================================================== Aide

export function helpView(app) {
  const item = (q, ...a) => h("details", { class: "faq" }, h("summary", {}, q), h("div", {}, ...a));
  return h("div", { class: "view prose-admin" },
    h("h1", {}, "Aide"),
    h("p", { class: "lead" }, "Tout ce qu'il faut savoir pour administrer le site, sans connaissances techniques."),
    item("Comment modifier le texte d'une page ?",
      h("p", {}, "Ouvrez « Arborescence », cliquez sur « ✏️ Modifier » à côté de la page, changez le texte puis cliquez sur « 💾 Enregistrer ». Une fenêtre vous montre ce qui va changer. Terminez par « Publier »."),
      h("p", {}, "Dans les zones de texte, utilisez la barre d'outils : gras, italique, listes, lien vers une page du site, lien externe, encadré.")),
    item("Comment ajouter une image ?",
      h("p", {}, "Dans « Médiathèque », cliquez sur « ⬆️ Téléverser une image », choisissez un fichier, remplissez la légende et les crédits, et confirmez que vous avez le droit de la publier. Elle est automatiquement réduite à une taille adaptée au web."),
      h("p", {}, "Ensuite, dans l'éditeur d'une page, cliquez sur « Choisir une image » pour l'utiliser.")),
    item("Comment ajouter une page ?",
      h("p", {}, "Cliquez sur « ➕ Ajouter une page », choisissez son type et son emplacement. Elle est créée masquée : complétez-la, vérifiez l'aperçu, puis cliquez sur « Remettre en ligne » et publiez.")),
    item("Comment réorganiser le site (arborescence) ?",
      h("p", {}, "Dans « Arborescence » : ↑ et ↓ changent l'ordre, « ⇄ Déplacer » rattache un lieu, un spot ou une institution à une autre île, ou un article à une autre rubrique, « 🔗 Adresse » change l'adresse de la page. Les liens internes sont mis à jour automatiquement."),
      h("p", {}, "Le menu principal et le pied de page se modifient dans « Menu et pied de page »."))
    ,
    item("Comment ajouter un conte dans « Hale halele » ?",
      h("p", {}, "« ➕ Ajouter une page » → « Conte ou récit ». Choisissez le genre (mythe, légende de lieu, récit, conte), l'île et éventuellement le lieu associé. Écrivez le récit avec vos mots ; la formule « Hale ! – Halele ! » est ajoutée automatiquement."),
      h("p", {}, "L'encadré « Ce que l'on en sait » sert à distinguer la légende de l'histoire : variantes, origine du récit, avis des historiens. Cochez « Mettre en avant » pour l'afficher sur la page d'accueil (4 récits au maximum).")),
    item("Comment créer ou modifier un quiz ?",
      h("p", {}, "Dans « Arborescence » → « Loisirs », modifiez un quiz ou cliquez sur « ➕ Quiz ». Pour chaque question : la question, les réponses proposées, le numéro de la bonne réponse (1 = la première), une explication et, si vous voulez, une page du site « pour en savoir plus ». La vérification avant publication bloque une bonne réponse qui n'existe pas.")),
    item("Comment ajouter un spot ou un bon plan ?",
      h("p", {}, "Dans « Arborescence » → « Les îles », dépliez l'île puis cliquez sur « ➕ Spot » dans le groupe « ⭐ Spots & bons plans ». Choisissez la catégorie (marché, artisanat, saveurs, plage, nature, patrimoine, culture) et la notoriété : « Incontournable » pour un lieu connu, « Secret local » pour un lieu méconnu. Ajoutez un bon plan pratique et, si possible, une image ou un lieu associé."),
      h("p", {}, "Le texte de présentation et les « bons plans pratiques » de la page de l'île se modifient dans la fiche de l'île (« ✏️ Textes de la page »). Les spots apparaissent aussi sur la page des quatre îles, avec des filtres par île, catégorie et notoriété.")),
    item("Comment présenter une institution ou une autorité coutumière ?",
      h("p", {}, "Même principe, dans le groupe « 🏛️ Vie publique & institutions » de l'île : « ➕ Institution ». Choisissez le domaine (pouvoirs publics, justice, religion, coutume, environnement, culture, sport, associations) et le statut : institution officielle, autorité coutumière ou religieuse (non officielle) ou association."),
      h("p", {}, "La portée « Union des Comores » affiche la fiche sur les pages des trois îles de l'Union (cochez « fait partie de l'Union » dans la fiche de ces îles) ; « Tout l'archipel » l'affiche pour les quatre îles. Restez factuel et citez vos sources dans le champ « Sources »."),
      h("p", {}, "Les noms de responsables changent souvent : décrivez plutôt les fonctions que les personnes en poste.")),
    item("Le menu tiroir du site, comment est-il construit ?",
      h("p", {}, "Le bouton « Menu », en haut à gauche de chaque page, ouvre un tiroir qui donne accès à toutes les pages, rangées comme le menu principal (« Menu et pied de page ») et complétées automatiquement : îles et leurs pages, lieux, articles, contes par genre, quiz, expériences, itinéraires… Il contient aussi une recherche. Rien à faire de votre côté : il se met à jour à chaque publication.")),
    item("Comment citer une source (bibliographie) ?",
      h("p", {}, "Ajoutez d'abord l'ouvrage dans « Bibliographie » (menu de gauche) avec un identifiant court, par exemple walker-2019, et indiquez s'il s'agit d'une voix de l'archipel ou d'un regard extérieur. Ensuite, dans un article d'histoire ou un conte, choisissez-le dans le champ « Références »."),
      h("p", {}, "Ne changez pas l'identifiant d'un ouvrage déjà cité : la publication serait bloquée tant que les pages citeraient l'ancien identifiant.")),
    item("Masquer ou supprimer ?",
      h("p", {}, "« Masquer » retire la page du site sans perdre son contenu : c'est réversible. « Supprimer » efface la page ; seule une restauration depuis l'Historique permet de la récupérer.")),
    item("Pourquoi une fenêtre s'ouvre-t-elle à chaque action ?",
      h("p", {}, "C'est un garde-fou : avant chaque modification, elle indique les pages touchées, les liens mis à jour et les risques. Les actions risquées demandent de recopier un mot de confirmation.")),
    item("Quand mes changements sont-ils visibles ?",
      h("p", {}, "Après « Publier », le site public est régénéré automatiquement en 1 à 3 minutes. Avant cela, vos changements sont un brouillon gardé dans ce navigateur.")),
    item("J'ai fait une erreur, comment revenir en arrière ?",
      h("p", {}, "Avant publication : « Publier » → « Annuler mes modifications ». Après publication : « Historique » → « ↩️ Restaurer » sur la version voulue.")),
    item("Le jeton GitHub, c'est quoi ?",
      h("p", {}, "C'est une clé personnelle qui autorise cette administration à modifier le dépôt GitHub du site. Ne la partagez jamais. Vous pouvez la révoquer à tout moment depuis les réglages de votre compte GitHub."),
      h("p", {}, "Cochez « Rester connecté » seulement sur un ordinateur personnel.")),
  );
}
