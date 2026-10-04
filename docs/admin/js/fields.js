// Moteur de formulaires : chaque champ d'un schéma devient un widget adapté aux débutants.

import { h, clear, confirmImpact } from "./ui.js";
import { richEditor } from "./richtext.js";
import { ICONS, sitePages, isOnline } from "./model.js";

/**
 * ctx = { data, thumb(key), pickMedia({kind, multiple}), pickLink(current), pageTitle(path) }
 * Renvoie { node, get() } ; get() renvoie un nouvel objet (les clés non éditées sont conservées).
 */
export function buildForm(fields, value, ctx) {
  const widgets = [];
  const node = h("div", { class: "form-grid" });
  for (const f of fields) {
    if (f.videoOnly && (value.kind || "image") !== "video") continue;
    const w = widget(f, value ? value[f.key] : undefined, ctx);
    widgets.push([f, w]);
    node.append(h("div", { class: `field field-${f.type}${f.danger ? " field-danger" : ""}` },
      f.type === "checkbox" ? null : h("label", { class: "field-label" }, f.label, f.required ? h("span", { class: "req", title: "Obligatoire" }, " *") : null),
      w.node,
      f.help ? h("p", { class: "help" }, f.help) : null));
  }
  return {
    node,
    get() {
      const out = { ...(value || {}) };
      for (const [f, w] of widgets) {
        const v = w.get();
        if (v === undefined) delete out[f.key];
        else out[f.key] = v;
      }
      return out;
    },
  };
}

function widget(f, value, ctx) {
  const make = WIDGETS[f.type] || WIDGETS.text;
  return make(f, value, ctx);
}

const moveBtns = (onUp, onDown, onRemove, removeLabel = "Retirer") => h("div", { class: "row-actions" },
  h("button", { type: "button", class: "icon-btn", title: "Monter", "aria-label": "Monter", onclick: onUp }, "↑"),
  h("button", { type: "button", class: "icon-btn", title: "Descendre", "aria-label": "Descendre", onclick: onDown }, "↓"),
  h("button", { type: "button", class: "icon-btn icon-danger", title: removeLabel, "aria-label": removeLabel, onclick: onRemove }, "✕"));

function swap(arr, i, j) {
  if (j < 0 || j >= arr.length) return false;
  [arr[i], arr[j]] = [arr[j], arr[i]];
  return true;
}

const WIDGETS = {
  text(f, value) {
    const input = h("input", { type: "text", class: "input", value: value ?? "" });
    return { node: input, get: () => input.value };
  },
  textarea(f, value) {
    const input = h("textarea", { class: "input", rows: 3 });
    input.value = value ?? "";
    return { node: input, get: () => input.value };
  },
  number(f, value) {
    const input = h("input", { type: "number", class: "input", value: value ?? "", step: "any" });
    return { node: input, get: () => (input.value === "" ? undefined : Number(input.value)) };
  },
  checkbox(f, value) {
    const input = h("input", { type: "checkbox" });
    input.checked = !!value;
    return { node: h("label", { class: "check" }, input, " ", f.label), get: () => input.checked };
  },
  color(f, value) {
    const input = h("input", { type: "color", class: "input-color", value: value || "#0b4f5c" });
    return { node: input, get: () => input.value };
  },
  icon(f, value) {
    const sel = h("select", { class: "input" }, Object.entries(ICONS).map(([k, label]) => h("option", { value: k, selected: k === value }, label)));
    return { node: sel, get: () => sel.value };
  },
  category(f, value, ctx) {
    const cats = ctx.data.settings.media_categories || {};
    const sel = h("select", { class: "input" }, Object.entries(cats).map(([k, label]) => h("option", { value: k, selected: k === value }, label)));
    return { node: sel, get: () => sel.value };
  },
  select(f, value) {
    const entries = Object.entries(f.options || {});
    const known = entries.some(([k]) => k === value);
    const sel = h("select", { class: "input" },
      !known && value ? h("option", { value, selected: true }, `${value} (valeur actuelle)`) : null,
      entries.map(([k, label]) => h("option", { value: k, selected: k === value }, label)));
    return { node: sel, get: () => sel.value };
  },
  answer(f, value) {
    const input = h("input", { type: "number", class: "input input-small", min: 1, value: (value ?? 0) + 1 });
    return { node: input, get: () => Math.max(0, Number(input.value || 1) - 1) };
  },
  autochildren(f, value, ctx) {
    const opts = [["", "Aucun (seulement le sous-menu manuel)"], ["iles", "Les îles"],
      ...ctx.data.topics.map((t) => [`rubrique:${t.slug}`, `Articles de la rubrique « ${t.name} »`]),
      ["contes", "Hale halele : catégories de contes"], ["loisirs", "Loisirs : liste des quiz"],
      ["experiences", "Expériences"], ["itineraires", "Itinéraires"], ["pratique", "Infos pratiques"]];
    const sel = h("select", { class: "input" }, opts.map(([k, label]) => h("option", { value: k, selected: k === (value || "") }, label)));
    return { node: sel, get: () => sel.value };
  },
  richtext(f, value, ctx) {
    const ed = richEditor(value || "", { pickLink: () => ctx.pickLink(), pageTitle: ctx.pageTitle });
    return { node: ed.node, get: ed.get };
  },

  // ---------------------------------------------------------------- Images
  media(f, value, ctx) {
    let current = value || "";
    const box = h("div", { class: "media-field" });
    const render = () => {
      clear(box);
      const m = current && ctx.data.media[current];
      box.append(
        m ? h("img", { src: ctx.thumb(current), alt: "", class: "media-thumb", loading: "lazy" }) : h("div", { class: "media-thumb media-empty" }, "Aucune image"),
        h("div", { class: "media-meta" },
          m ? h("p", {}, m.caption) : current ? h("p", { class: "error" }, `Image introuvable : ${current}`) : null,
          h("div", { class: "btn-row" },
            h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => {
              const key = await ctx.pickMedia({ kind: f.kind });
              if (key) { current = key; render(); }
            } }, current ? "Changer d'image" : "Choisir une image"),
            current && f.optional ? h("button", { type: "button", class: "btn btn-link btn-small", onclick: () => { current = ""; render(); } }, "Retirer l'image") : null)));
    };
    render();
    return { node: box, get: () => (current ? current : (f.optional ? undefined : "")) };
  },
  medialist(f, value, ctx) {
    const items = [...(value || [])];
    const box = h("div", { class: "medialist" });
    const render = () => {
      clear(box);
      const grid = h("div", { class: "medialist-grid" });
      items.forEach((key, i) => {
        const m = ctx.data.media[key];
        grid.append(h("div", { class: "medialist-item" },
          m && (m.kind || "image") === "image"
            ? h("img", { src: ctx.thumb(key), alt: "", loading: "lazy" })
            : h("div", { class: "media-empty" }, m ? "🎬 " + m.caption : `Introuvable : ${key}`),
          moveBtns(() => { swap(items, i, i - 1); render(); }, () => { swap(items, i, i + 1); render(); },
            () => { items.splice(i, 1); render(); })));
      });
      box.append(items.length ? grid : h("p", { class: "muted" }, "Aucune image pour l'instant."),
        h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: async () => {
          const key = await ctx.pickMedia({ kind: f.kind });
          if (key && !items.includes(key)) { items.push(key); render(); }
        } }, f.kind === "video" ? "+ Ajouter une vidéo" : "+ Ajouter une image"));
    };
    render();
    return { node: box, get: () => [...items] };
  },

  // ---------------------------------------------------------------- Liens et références
  link(f, value, ctx) {
    const pages = sitePages(ctx.data);
    const isExternal = value && /^(https?:|mailto:)/.test(value);
    const [path, anchor] = (value && !isExternal ? value : "").split("#");
    const sel = h("select", { class: "input" },
      h("option", { value: "" }, f.optional ? "— Aucun lien —" : "— Choisir une page —"),
      groupBy(pages, "group").map(([group, list]) => h("optgroup", { label: group },
        list.map((p) => h("option", { value: p.path, selected: p.path === path }, p.title + (p.hidden ? " (masquée)" : ""))))),
      h("option", { value: "__external", selected: isExternal }, "Lien vers un autre site…"));
    if (path && !pages.some((p) => p.path === path)) sel.prepend(h("option", { value: path, selected: true }, `⚠ Page introuvable : ${path}`));
    const ext = h("input", { type: "url", class: "input", placeholder: "https://…", value: isExternal ? value : "", hidden: !isExternal });
    const anch = h("input", { type: "text", class: "input input-small", placeholder: "ancre (facultatif)", value: anchor || "", hidden: isExternal });
    sel.addEventListener("change", () => { ext.hidden = sel.value !== "__external"; anch.hidden = sel.value === "__external"; });
    return {
      node: h("div", { class: "link-field" }, sel, anch, ext),
      get: () => {
        if (sel.value === "__external") return ext.value.trim();
        if (!sel.value) return f.optional ? "" : "";
        return sel.value + (anch.value.trim() ? "#" + anch.value.trim().replace(/^#/, "") : "");
      },
    };
  },
  ref(f, value, ctx) {
    const items = refItems(f.ref, ctx.data);
    const sel = h("select", { class: "input" },
      f.optional ? h("option", { value: "" }, f.emptyLabel || "— Aucun —") : null,
      items.map((it) => h("option", { value: it.slug, selected: it.slug === value }, it.label)));
    return { node: sel, get: () => sel.value };
  },
  reflist(f, value, ctx) {
    const items = [...(value || [])];
    const all = refItems(f.ref, ctx.data);
    const box = h("div", { class: "reflist" });
    const labelOf = (slug) => (all.find((x) => x.slug === slug) || { label: `⚠ introuvable : ${slug}` }).label;
    const render = () => {
      clear(box);
      const list = h("ol", { class: "reflist-items" });
      items.forEach((slug, i) => list.append(h("li", {}, h("span", {}, labelOf(slug)),
        moveBtns(() => { swap(items, i, i - 1); render(); }, () => { swap(items, i, i + 1); render(); },
          () => { items.splice(i, 1); render(); }))));
      const available = all.filter((x) => !items.includes(x.slug) && (!f.sameIsland || x.island === ctx.entity?.slug));
      const add = h("select", { class: "input" }, h("option", { value: "" }, "+ Ajouter…"),
        available.map((x) => h("option", { value: x.slug }, x.label)));
      add.addEventListener("change", () => { if (add.value) { items.push(add.value); render(); } });
      box.append(items.length ? list : h("p", { class: "muted" }, "Aucun élément."));
      if (available.length) box.append(add);
    };
    render();
    return { node: box, get: () => [...items] };
  },

  // ---------------------------------------------------------------- Listes
  stringlist(f, value) {
    const items = [...(value || [])];
    const box = h("div", { class: "stringlist" });
    const inputs = [];
    const render = () => {
      clear(box);
      inputs.length = 0;
      items.forEach((text, i) => {
        const input = h("input", { type: "text", class: "input", value: text });
        input.addEventListener("input", () => { items[i] = input.value; });
        inputs.push(input);
        box.append(h("div", { class: "stringlist-row" }, input,
          moveBtns(() => { swap(items, i, i - 1); render(); }, () => { swap(items, i, i + 1); render(); },
            () => { items.splice(i, 1); render(); })));
      });
      box.append(h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: () => { items.push(""); render(); inputs[inputs.length - 1].focus(); } },
        "+ " + (f.addLabel || "Ajouter")));
    };
    render();
    return { node: box, get: () => items.map((s) => s.trim()).filter(Boolean) };
  },
  list(f, value, ctx) {
    const items = (value || []).map((v) => ({ value: v, form: null, open: false }));
    const box = h("div", { class: "listfield" });
    const collect = () => items.forEach((it) => { if (it.form) it.value = it.form.get(); });
    const titleOf = (v, i) => {
      const t = v && f.itemLabel ? v[f.itemLabel] : "";
      return `${i + 1}. ${t || "(sans titre)"}`;
    };
    const render = () => {
      collect();
      clear(box);
      items.forEach((it, i) => {
        it.form = buildForm(f.fields, it.value || {}, ctx);
        const body = h("div", { class: "listfield-body", hidden: !it.open }, it.form.node);
        const head = h("div", { class: "listfield-head" },
          h("button", { type: "button", class: "listfield-toggle", "aria-expanded": String(it.open), onclick: () => {
            it.open = !it.open; body.hidden = !it.open; head.querySelector(".listfield-toggle").setAttribute("aria-expanded", String(it.open));
          } }, (it.open ? "▾ " : "▸ ") + titleOf(it.value, i)),
          moveBtns(() => { collect(); swap(items, i, i - 1); render(); }, () => { collect(); swap(items, i, i + 1); render(); },
            async () => {
              collect();
              const ok = await confirmImpact({
                title: "Retirer cet élément ?", severity: "warning",
                intro: `Vous allez retirer « ${titleOf(it.value, i)} » de « ${f.label} ».`,
                notes: ["Le retrait ne sera effectif qu'après avoir cliqué sur « Enregistrer », puis publié. Vous pouvez encore annuler en quittant sans enregistrer."],
                confirmLabel: "Retirer",
              });
              if (ok) { items.splice(i, 1); render(); }
            }));
        box.append(h("div", { class: "listfield-item" }, head, body));
      });
      box.append(h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: () => {
        collect();
        const blank = Object.fromEntries(f.fields.map((sf) => [sf.key, sf.type === "list" || sf.type === "stringlist" || sf.type === "medialist" ? [] : sf.type === "checkbox" ? false : ""]));
        items.push({ value: blank, form: null, open: true });
        render();
      } }, "+ " + (f.addLabel || "Ajouter")));
    };
    render();
    return { node: box, get: () => { collect(); return items.map((it) => it.value); } };
  },
  group(f, value, ctx) {
    const form = buildForm(f.fields, value || {}, ctx);
    return { node: h("div", { class: "group" }, form.node), get: () => form.get() };
  },
  keyvalue(f, value) {
    const rows = Object.entries(value || {}).map(([k, v]) => ({ k, v }));
    const box = h("div", { class: "keyvalue" });
    const render = () => {
      clear(box);
      rows.forEach((r, i) => {
        const k = h("input", { type: "text", class: "input input-small", value: r.k, placeholder: "code" });
        const v = h("input", { type: "text", class: "input", value: r.v, placeholder: "libellé" });
        k.addEventListener("input", () => { r.k = k.value; });
        v.addEventListener("input", () => { r.v = v.value; });
        box.append(h("div", { class: "stringlist-row" }, k, v,
          h("button", { type: "button", class: "icon-btn icon-danger", "aria-label": "Retirer", onclick: () => { rows.splice(i, 1); render(); } }, "✕")));
      });
      box.append(h("button", { type: "button", class: "btn btn-secondary btn-small", onclick: () => { rows.push({ k: "", v: "" }); render(); } }, "+ Ajouter"));
    };
    render();
    return { node: box, get: () => Object.fromEntries(rows.filter((r) => r.k.trim()).map((r) => [r.k.trim(), r.v])) };
  },
  coords(f, value) {
    const [lat0, lng0, zoom0] = value || [];
    const lat = h("input", { type: "number", step: "any", class: "input input-small", value: lat0 ?? "", "aria-label": "Latitude" });
    const lng = h("input", { type: "number", step: "any", class: "input input-small", value: lng0 ?? "", "aria-label": "Longitude" });
    const zoom = f.zoom ? h("input", { type: "number", class: "input input-small", value: zoom0 ?? 10, "aria-label": "Zoom" }) : null;
    const osm = h("a", { href: "#", target: "_blank", rel: "noopener", class: "btn btn-link btn-small" }, "Vérifier sur la carte ↗");
    const upd = () => { osm.href = `https://www.openstreetmap.org/?mlat=${lat.value}&mlon=${lng.value}#map=12/${lat.value}/${lng.value}`; };
    [lat, lng].forEach((i) => i.addEventListener("input", upd));
    upd();
    return {
      node: h("div", { class: "coords" }, h("label", {}, "Latitude ", lat), h("label", {}, "Longitude ", lng), zoom ? h("label", {}, "Zoom ", zoom) : null, osm),
      get: () => (zoom ? [Number(lat.value), Number(lng.value), Number(zoom.value)] : [Number(lat.value), Number(lng.value)]),
    };
  },
};

function groupBy(list, key) {
  const map = new Map();
  list.forEach((x) => { if (!map.has(x[key])) map.set(x[key], []); map.get(x[key]).push(x); });
  return [...map.entries()];
}

function refItems(ref, data) {
  if (ref === "place") {
    return data.places.map((p) => {
      const island = data.islands.find((i) => i.slug === p.island);
      return { slug: p.slug, island: p.island, label: `${p.name} (${island ? island.name : "?"})${isOnline(data, `place:${p.slug}`) ? "" : " — masqué"}` };
    });
  }
  if (ref === "island") return data.islands.map((i) => ({ slug: i.slug, label: i.name }));
  if (ref === "source") {
    return (data.bibliography || []).filter((b) => b.id).map((b) => ({
      slug: b.id, label: `${b.author} — ${b.title}${b.year ? ` (${b.year})` : ""}${b.kind === "comorien" ? " · voix de l'archipel" : ""}`,
    }));
  }
  return [];
}
