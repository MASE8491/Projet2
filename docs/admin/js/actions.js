// Actions de structure (masquer, déplacer, renommer, supprimer, ajouter), toutes précédées
// d'une fenêtre qui explique leur impact sur le site.

import { h, confirmImpact, prompt, openModal, toast } from "./ui.js";
import * as M from "./model.js";

const pageItem = (data, x) => ({ text: x.title || x.path, sub: `${x.path} — ${x.why}` });

export async function togglePublished(app, id) {
  const data = app.store.data;
  const e = M.getEntity(data, id);
  const title = M.titleOf(data, id);
  const willHide = M.isPublished(e);
  const p = M.parseId(id);
  const sections = [];
  if (willHide) {
    sections.push({ heading: "Cette page disparaîtra de :", items: M.appearsOn(data, id).map((x) => pageItem(data, x)) });
    const menu = M.menuMentions(data, id);
    if (menu.length) sections.push({ heading: "Menus concernés (l'entrée sera retirée) :", items: menu });
    if (p.type === "island") sections.push({ heading: "Lieux masqués avec l'île :", items: data.places.filter((pl) => pl.island === p.slug).map((pl) => pl.name), empty: "Aucun lieu" });
    if (p.type === "topic") sections.push({ heading: "Articles masqués avec la rubrique :", items: e.pages.map((pg) => pg.name), empty: "Aucun article" });
    const links = M.inboundLinks(data, M.pathOf(data, id));
    if (links.length) sections.push({ heading: "Liens vers cette page (ils s'afficheront comme du texte simple) :", items: links.map((l) => `${l.title} (${l.count})`) });
  } else {
    sections.push({ heading: "La page sera de nouveau visible sur :", items: M.appearsOn(data, id).map((x) => pageItem(data, x)) });
  }
  const ok = await confirmImpact({
    title: willHide ? `Masquer « ${title} » ?` : `Remettre en ligne « ${title} » ?`,
    severity: willHide ? "warning" : "info",
    intro: willHide
      ? "La page ne sera plus accessible aux visiteurs après publication. Son contenu est conservé : vous pourrez la remettre en ligne à tout moment."
      : "La page redeviendra accessible aux visiteurs après publication.",
    sections,
    notes: ["Rien ne change sur le site public tant que vous n'avez pas cliqué sur « Publier »."],
    confirmLabel: willHide ? "Masquer la page" : "Remettre en ligne",
  });
  if (!ok) return false;
  app.store.apply(`${willHide ? "Masquage" : "Remise en ligne"} de « ${title} »`, (d) => {
    const target = M.getEntity(d, id);
    if (willHide) target.published = false; else delete target.published;
  });
  toast(willHide ? "Page masquée (en attente de publication)" : "Page remise en ligne (en attente de publication)");
  return true;
}

export async function move(app, id, dir) {
  const data = app.store.data;
  const title = M.titleOf(data, id);
  const p = M.parseId(id);
  const where = {
    island: "l'ordre des îles (accueil, menu, tableau comparatif)",
    place: "la liste « À voir » de l'île et la page Voyager",
    topic: "l'ordre des rubriques (accueil, « autres rubriques »)",
    topicpage: "l'ordre des articles de la rubrique (liste, menu, pages précédente / suivante)",
    experience: "la liste des expériences et le sous-menu",
    itinerary: "la liste des itinéraires (les 4 premiers sont sur l'accueil)",
    practical: "la liste des infos pratiques",
  }[p.type];
  const ok = await confirmImpact({
    title: `${dir < 0 ? "Monter" : "Descendre"} « ${title} » ?`,
    severity: "info",
    intro: `Cela modifie ${where}. Aucune adresse ne change.`,
    confirmLabel: dir < 0 ? "Monter" : "Descendre",
  });
  if (!ok) return false;
  let moved = false;
  app.store.apply(`Ordre modifié : « ${title} » ${dir < 0 ? "monte" : "descend"}`, (d) => { moved = M.moveInList(d, id, dir); });
  if (!moved) toast("Cet élément est déjà en bout de liste.", "info");
  return moved;
}

export async function changeSlug(app, id) {
  const data = app.store.data;
  const e = M.getEntity(data, id);
  const p = M.parseId(id);
  const title = M.titleOf(data, id);
  const value = await prompt("Changer l'adresse de la page", {
    label: "Nouvelle adresse (lettres minuscules, chiffres et tirets)", value: e.slug,
    help: `Adresse actuelle : ${M.pathOf(data, id)}`, confirmLabel: "Voir l'impact",
  });
  if (!value) return false;
  const slug = M.slugify(value);
  if (!slug || slug === e.slug) { toast("L'adresse n'a pas changé.", "info"); return false; }
  const siblings = M.siblingsSlugs(data, p.type, p.topic);
  if (siblings.includes(slug)) { toast(`L'adresse « ${slug} » est déjà utilisée.`, "error"); return false; }
  if (p.type === "topic" && app.config.reserved_slugs.includes(slug)) { toast(`L'adresse « ${slug} » est réservée par le site.`, "error"); return false; }
  const oldPath = M.pathOf(data, id);
  const newId = p.type === "topicpage" ? `topicpage:${p.topic}/${slug}` : `${p.type}:${slug}`;
  const newPath = p.type === "topic" ? `${slug}/index.html` : oldPath.slice(0, -(`${e.slug}.html`.length)) + `${slug}.html`;
  const links = p.type === "topic" ? M.inboundLinks(data, `${e.slug}/`, { prefix: true }) : M.inboundLinks(data, oldPath);
  const refs = M.slugReferences(data, id);
  const ok = await confirmImpact({
    title: `Changer l'adresse de « ${title} » ?`,
    severity: "warning",
    intro: p.type === "topic"
      ? `Toutes les pages de la rubrique changent d'adresse : ${e.slug}/… devient ${slug}/…`
      : `${oldPath} devient ${newPath}`,
    sections: [
      { heading: "Liens du site mis à jour automatiquement :", items: links.map((l) => `${l.title} (${l.count} lien${l.count > 1 ? "s" : ""})`), empty: "Aucun lien à mettre à jour" },
      { heading: "Références mises à jour automatiquement :", items: refs.map((r) => `${r.title} — ${r.how}`), empty: "Aucune" },
    ],
    notes: ["Attention : les liens externes (réseaux sociaux, favoris, moteurs de recherche) vers l'ancienne adresse ne fonctionneront plus."],
    requireCheck: "J'ai compris que l'ancienne adresse ne fonctionnera plus.",
    confirmLabel: "Changer l'adresse",
  });
  if (!ok) return false;
  app.store.apply(`Adresse de « ${title} » : ${e.slug} → ${slug}`, (d) => M.renameSlug(d, id, slug));
  toast("Adresse modifiée (en attente de publication)");
  return newId;
}

export async function relocate(app, id) {
  const data = app.store.data;
  const p = M.parseId(id);
  const title = M.titleOf(data, id);
  if (p.type === "place") {
    const place = M.getEntity(data, id);
    const options = data.islands.filter((i) => i.slug !== place.island);
    const sel = h("select", { class: "input" }, options.map((i) => h("option", { value: i.slug }, i.name)));
    const target = await openModal({
      title: `Rattacher « ${title} » à une autre île`,
      body: h("label", { class: "field-label" }, "Nouvelle île", sel),
      actions: [{ label: "Annuler", value: null }, { label: "Voir l'impact", kind: "btn-primary", value: () => sel.value }],
    });
    if (!target) return false;
    const from = data.islands.find((i) => i.slug === place.island);
    const to = data.islands.find((i) => i.slug === target);
    const ok = await confirmImpact({
      title: `Déplacer « ${title} » vers ${to.name} ?`, severity: "warning",
      intro: "L'adresse de la page ne change pas.",
      sections: [{ heading: "Pages modifiées :", items: [
        `${from ? from.name : "?"} — le lieu disparaît de « À voir »`,
        `${to.name} — le lieu apparaît en fin de liste « À voir »`,
        "Carte des îles et page Voyager — couleur et regroupement du lieu"] }],
      notes: ["Pensez à adapter le surtitre et la position du lieu sur la carte si besoin."],
      confirmLabel: "Déplacer",
    });
    if (!ok) return false;
    app.store.apply(`« ${title} » déplacé vers ${to.name}`, (d) => M.movePlace(d, p.slug, target));
    toast("Lieu déplacé (en attente de publication)");
    return id;
  }
  if (p.type === "topicpage") {
    const options = data.topics.filter((t) => t.slug !== p.topic);
    if (!options.length) { toast("Il n'existe pas d'autre rubrique.", "info"); return false; }
    const sel = h("select", { class: "input" }, options.map((t) => h("option", { value: t.slug }, t.name)));
    const target = await openModal({
      title: `Déplacer « ${title} » dans une autre rubrique`,
      body: h("label", { class: "field-label" }, "Nouvelle rubrique", sel),
      actions: [{ label: "Annuler", value: null }, { label: "Voir l'impact", kind: "btn-primary", value: () => sel.value }],
    });
    if (!target) return false;
    const oldPath = M.pathOf(data, id);
    const page = M.getEntity(data, id);
    const links = M.inboundLinks(data, oldPath);
    const ok = await confirmImpact({
      title: `Déplacer « ${title} » ?`, severity: "warning",
      intro: `L'adresse change : ${oldPath} devient ${target}/${page.slug}.html`,
      sections: [{ heading: "Liens du site mis à jour automatiquement :", items: links.map((l) => `${l.title} (${l.count})`), empty: "Aucun" }],
      notes: ["Les liens externes vers l'ancienne adresse ne fonctionneront plus."],
      requireCheck: "J'ai compris que l'adresse de l'article va changer.",
      confirmLabel: "Déplacer",
    });
    if (!ok) return false;
    let newId = id;
    app.store.apply(`« ${title} » déplacé vers la rubrique ${target}`, (d) => { newId = M.moveTopicPage(d, id, target); });
    toast("Article déplacé (en attente de publication)");
    return newId;
  }
  return false;
}

export async function remove(app, id) {
  const data = app.store.data;
  const p = M.parseId(id);
  const e = M.getEntity(data, id);
  const title = M.titleOf(data, id);
  let blocked = null;
  const sections = [{ heading: "La page sera retirée de :", items: M.appearsOn(data, id).map((x) => pageItem(data, x)) }];
  if (p.type === "island") {
    const places = data.places.filter((pl) => pl.island === p.slug);
    if (places.length) blocked = `Cette île contient encore ${places.length} lieu(x) : ${places.map((pl) => pl.name).join(", ")}. Déplacez-les vers une autre île ou supprimez-les d'abord.`;
  }
  if (p.type === "topic" && e.pages.length) sections.push({ heading: "⚠ Articles supprimés avec la rubrique :", items: e.pages.map((pg) => pg.name) });
  const refs = M.slugReferences(data, id);
  if (refs.length) sections.push({ heading: "Références retirées automatiquement :", items: refs.map((r) => `${r.title} — ${r.how}`) });
  const links = M.inboundLinks(data, M.pathOf(data, id));
  if (links.length) sections.push({ heading: "Liens vers cette page (ils s'afficheront comme du texte simple) :", items: links.map((l) => `${l.title} (${l.count})`) });
  const menu = M.menuMentions(data, id);
  if (menu.length) sections.push({ heading: "Menus concernés :", items: menu });
  const ok = await confirmImpact({
    title: `Supprimer « ${title} » ?`, severity: "danger",
    intro: "La page et tout son contenu seront supprimés après publication. Si vous voulez seulement la cacher, utilisez plutôt « Masquer ».",
    sections, blocked,
    notes: ["En cas d'erreur, une version précédente peut être restaurée depuis l'Historique."],
    requireType: "SUPPRIMER", confirmLabel: "Supprimer définitivement",
  });
  if (!ok) return false;
  app.store.apply(`Suppression de « ${title} »`, (d) => M.deleteEntity(d, id));
  toast("Page supprimée (en attente de publication)");
  return true;
}

export async function create(app, type, parentSlug) {
  const data = app.store.data;
  const def = M.TYPES[type];
  const parentLabel = type === "place" ? data.islands.find((i) => i.slug === parentSlug)?.name
    : type === "topicpage" ? data.topics.find((t) => t.slug === parentSlug)?.name : null;
  const title = await prompt(`Ajouter : ${def.label.toLowerCase()}`, {
    label: "Titre", help: parentLabel ? `Dans : ${parentLabel}` : null, confirmLabel: "Voir l'impact",
  });
  if (!title) return false;
  const entity = M.blankEntity(data, type, title, parentSlug);
  if (type === "topic" && app.config.reserved_slugs.includes(entity.slug)) entity.slug = M.uniqueSlug([...app.config.reserved_slugs, ...data.topics.map((t) => t.slug)], `${entity.slug}-rubrique`);
  const path = type === "topicpage" ? `${parentSlug}/${entity.slug}.html` : def.path(entity);
  const ok = await confirmImpact({
    title: `Créer « ${title} » ?`, severity: "info",
    intro: `Une nouvelle page sera créée à l'adresse ${path}.`,
    sections: [{ heading: "Ce qui va se passer :", items: [
      "La page est créée MASQUÉE : les visiteurs ne la verront pas.",
      "Complétez ensuite son contenu dans l'éditeur (une image par défaut est proposée).",
      "Quand elle est prête, cliquez sur « Remettre en ligne », puis publiez.",
      ...(type === "topic" ? ["Pour l'afficher dans le menu, ajoutez-la dans « Menu et pied de page »."] : []),
    ] }],
    confirmLabel: "Créer la page",
  });
  if (!ok) return false;
  let id;
  app.store.apply(`Création de « ${title} » (${def.label.toLowerCase()})`, (d) => { id = M.insertEntity(d, type, entity, parentSlug); });
  toast("Page créée (masquée)");
  return id;
}
