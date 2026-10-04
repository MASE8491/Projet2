// Éditeur de texte enrichi simple (gras, italique, listes, liens, encadré) avec nettoyage du HTML.
// Les liens internes sont stockés sous la forme [[chemin|libellé]] pour que le générateur
// calcule des liens relatifs et masque ceux qui mènent vers des pages non publiées.

import { h } from "./ui.js";

const ALLOWED = new Set(["P", "BR", "STRONG", "EM", "UL", "OL", "LI", "A", "H3", "TABLE", "THEAD", "TBODY",
  "TR", "TH", "TD", "DIV", "SMALL"]);
const RENAME = { B: "STRONG", I: "EM", H1: "H3", H2: "H3", H4: "H3", SPAN: null, FONT: null };

const escapeHtml = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

/** [[chemin|libellé]] → <a data-internal="chemin">libellé</a> pour l'édition. */
export function toEditable(html) {
  return (html || "").replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g,
    (_, path, label) => `<a href="#" data-internal="${escapeHtml(path)}">${label}</a>`);
}

/** Nettoie le HTML saisi et reconvertit les liens internes. */
export function fromEditable(html) {
  const tpl = document.createElement("template");
  tpl.innerHTML = html;
  const clean = (node) => {
    for (const child of [...node.childNodes]) {
      if (child.nodeType === Node.COMMENT_NODE) { child.remove(); continue; }
      if (child.nodeType !== Node.ELEMENT_NODE) continue;
      let el = child;
      const tag = el.tagName;
      if (tag in RENAME) {
        const target = RENAME[tag];
        if (!target) { el.replaceWith(...el.childNodes); continue; }
        const repl = document.createElement(target);
        repl.append(...el.childNodes);
        el.replaceWith(repl);
        el = repl;
      } else if (!ALLOWED.has(tag)) {
        if (["SCRIPT", "STYLE", "IFRAME", "OBJECT", "EMBED"].includes(tag)) el.remove();
        else el.replaceWith(...el.childNodes);
        continue;
      }
      // Attributs autorisés
      const keep = {};
      if (el.tagName === "A") {
        if (el.dataset.internal) keep["data-internal"] = el.dataset.internal;
        const href = el.getAttribute("href") || "";
        if (/^(https?:|mailto:)/i.test(href)) { keep.href = href; keep.rel = "noopener"; }
      }
      if (el.tagName === "DIV" && el.classList.contains("notice")) keep.class = "notice";
      if (el.tagName === "TABLE" && el.classList.contains("table")) keep.class = "table";
      if ((el.tagName === "TD" || el.tagName === "TH") && el.getAttribute("colspan")) keep.colspan = el.getAttribute("colspan");
      for (const attr of [...el.attributes]) el.removeAttribute(attr.name);
      for (const [k, v] of Object.entries(keep)) el.setAttribute(k, v);
      if (el.tagName === "DIV" && !keep.class) {
        // Les <div> créés par le navigateur deviennent des paragraphes
        const p = document.createElement("p");
        p.append(...el.childNodes);
        el.replaceWith(p);
        el = p;
      }
      if (el.tagName === "A" && !keep.href && !keep["data-internal"]) { el.replaceWith(...el.childNodes); continue; }
      clean(el);
    }
  };
  clean(tpl.content);
  // Texte isolé au premier niveau → paragraphe
  for (const n of [...tpl.content.childNodes]) {
    if (n.nodeType === Node.TEXT_NODE && n.textContent.trim()) {
      const p = document.createElement("p");
      n.replaceWith(p);
      p.append(n);
    }
  }
  let out = tpl.innerHTML;
  out = out.replace(/<a data-internal="([^"]+)">([\s\S]*?)<\/a>/g, (_, path, label) => `[[${path.replace(/&amp;/g, "&")}|${label}]]`);
  out = out.replace(/<p>(\s|&nbsp;|<br>)*<\/p>/g, "").trim();
  return out;
}

/**
 * Crée un éditeur. `pickLink()` doit renvoyer une promesse de chemin interne (ou null).
 * Renvoie { node, get() }.
 */
export function richEditor(initial, { pickLink, pageTitle }) {
  const area = h("div", { class: "rte-area", contenteditable: "true", role: "textbox", "aria-multiline": "true" });
  area.innerHTML = toEditable(initial);
  const source = h("textarea", { class: "rte-source input", rows: 10, hidden: true });
  let sourceMode = false;

  const decorate = () => {
    area.querySelectorAll("a[data-internal]").forEach((a) => {
      const t = pageTitle(a.dataset.internal);
      a.title = t ? `Lien vers « ${t} »` : `Lien vers une page introuvable : ${a.dataset.internal}`;
      a.classList.toggle("rte-broken", !t);
    });
  };
  decorate();

  const exec = (cmd, value = null) => {
    area.focus();
    document.execCommand(cmd, false, value);
  };

  const saveRange = () => {
    const sel = window.getSelection();
    return sel.rangeCount ? sel.getRangeAt(0).cloneRange() : null;
  };
  const restoreRange = (r) => {
    if (!r) return;
    area.focus();
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(r);
  };

  const btn = (label, title, onClick) => h("button", { type: "button", class: "rte-btn", title, "aria-label": title,
    onmousedown: (e) => e.preventDefault(), onclick: onClick }, label);

  const insertLink = (attrs, fallbackText) => {
    const sel = window.getSelection();
    const text = sel.toString() || fallbackText;
    const a = document.createElement("a");
    Object.entries(attrs).forEach(([k, v]) => a.setAttribute(k, v));
    a.textContent = text;
    if (sel.rangeCount) {
      const range = sel.getRangeAt(0);
      range.deleteContents();
      range.insertNode(a);
    } else area.append(a);
    decorate();
  };

  const toolbar = h("div", { class: "rte-toolbar", role: "toolbar", "aria-label": "Mise en forme" },
    btn(h("strong", {}, "G"), "Gras", () => exec("bold")),
    btn(h("em", {}, "I"), "Italique", () => exec("italic")),
    btn("• Liste", "Liste à puces", () => exec("insertUnorderedList")),
    btn("1. Liste", "Liste numérotée", () => exec("insertOrderedList")),
    btn("🔗 Page du site", "Lien vers une page du site", async () => {
      const range = saveRange();
      const path = await pickLink();
      if (!path) return;
      restoreRange(range);
      insertLink({ href: "#", "data-internal": path }, pageTitle(path) || path);
    }),
    btn("🌐 Lien externe", "Lien vers un autre site", () => {
      const range = saveRange();
      const url = window.prompt("Adresse du site (commençant par https://)", "https://");
      if (!url || !/^https?:\/\//i.test(url)) return;
      restoreRange(range);
      insertLink({ href: url, rel: "noopener" }, url);
    }),
    btn("Retirer le lien", "Retirer le lien sélectionné", () => {
      const sel = window.getSelection();
      let node = sel.anchorNode;
      while (node && node !== area && node.tagName !== "A") node = node.parentNode;
      if (node && node.tagName === "A") node.replaceWith(...node.childNodes);
    }),
    btn("Encadré", "Encadré « Bon à savoir »", () => {
      const div = document.createElement("div");
      div.className = "notice";
      div.innerHTML = "<strong>Bon à savoir&nbsp;:</strong> texte de l'encadré.";
      const sel = window.getSelection();
      if (sel.rangeCount && area.contains(sel.anchorNode)) {
        const range = sel.getRangeAt(0);
        range.collapse(false);
        range.insertNode(div);
      } else area.append(div);
    }),
    btn("Effacer la mise en forme", "Effacer la mise en forme", () => exec("removeFormat")),
    btn("</> HTML", "Voir ou modifier le code HTML (avancé)", () => {
      sourceMode = !sourceMode;
      if (sourceMode) { source.value = fromEditable(area.innerHTML); }
      else { area.innerHTML = toEditable(fromEditable(toEditable(source.value))); decorate(); }
      source.hidden = !sourceMode;
      area.hidden = sourceMode;
    }),
  );
  area.addEventListener("click", (e) => { if (e.target.closest("a")) e.preventDefault(); });
  area.addEventListener("paste", (e) => {
    // Coller du texte brut évite d'importer la mise en forme d'autres sites
    e.preventDefault();
    const text = (e.clipboardData || window.clipboardData).getData("text/plain");
    document.execCommand("insertText", false, text);
  });
  document.execCommand("defaultParagraphSeparator", false, "p");
  const node = h("div", { class: "rte" }, toolbar, area, source);
  return {
    node,
    get: () => (sourceMode ? fromEditable(toEditable(source.value)) : fromEditable(area.innerHTML)),
  };
}
