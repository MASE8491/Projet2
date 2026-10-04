// Briques d'interface : création d'éléments, fenêtres contextuelles (garde-fous), notifications.

export function h(tag, attrs = {}, ...children) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k === "class") el.className = v;
    else if (k === "dataset") Object.assign(el.dataset, v);
    else if (k.startsWith("on") && typeof v === "function") el.addEventListener(k.slice(2), v);
    else if (k === "html") el.innerHTML = v;
    else if (v === true) el.setAttribute(k, "");
    else el.setAttribute(k, v);
  }
  for (const c of children.flat(Infinity)) {
    if (c === null || c === undefined || c === false) continue;
    el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return el;
}

export function clear(el) {
  while (el.firstChild) el.removeChild(el.firstChild);
  return el;
}

// ------------------------------------------------------------------ Fenêtres contextuelles

let modalStack = 0;

/**
 * Ouvre une fenêtre et renvoie une promesse résolue avec la valeur du bouton choisi
 * (ou null si l'utilisateur ferme la fenêtre).
 */
export function openModal({ title, body, actions = [], size = "", tone = "", onOpen }) {
  return new Promise((resolve) => {
    const dialog = h("dialog", { class: `modal ${size} ${tone ? "modal-" + tone : ""}`, "aria-labelledby": "modal-title" });
    const footer = h("div", { class: "modal-actions" });
    const close = (value) => {
      dialog.close();
      dialog.remove();
      modalStack -= 1;
      resolve(value);
    };
    for (const a of actions) {
      const btn = h("button", { type: "button", class: `btn ${a.kind || "btn-secondary"}`, ...(a.attrs || {}) }, a.label);
      btn.addEventListener("click", async () => {
        if (a.validate) {
          const ok = await a.validate();
          if (!ok) return;
        }
        close(typeof a.value === "function" ? a.value() : a.value);
      });
      footer.append(btn);
      a.button = btn;
    }
    dialog.append(
      h("header", { class: "modal-head" },
        h("h2", { id: "modal-title" }, title),
        h("button", { type: "button", class: "icon-btn", "aria-label": "Fermer", onclick: () => close(null) }, "✕")),
      h("div", { class: "modal-body" }, body),
      footer,
    );
    dialog.addEventListener("cancel", (e) => { e.preventDefault(); close(null); });
    document.body.append(dialog);
    modalStack += 1;
    dialog.showModal();
    if (onOpen) onOpen(dialog, actions);
  });
}

const SEVERITY = {
  info: { icon: "ℹ️", label: "Impact faible", tone: "info" },
  warning: { icon: "⚠️", label: "Impact important", tone: "warning" },
  danger: { icon: "⛔", label: "Action risquée", tone: "danger" },
};

/**
 * Garde-fou : décrit l'impact d'une modification et demande une confirmation explicite.
 *  - severity : info | warning | danger
 *  - sections : [{ heading, items: [texte | { text, sub }], empty }]
 *  - requireCheck : texte d'une case à cocher obligatoire
 *  - requireType : mot à recopier pour confirmer (actions destructrices)
 */
export function confirmImpact({ title, severity = "info", intro, sections = [], notes = [], requireCheck,
  requireType, confirmLabel = "Confirmer", cancelLabel = "Annuler", blocked }) {
  const sev = SEVERITY[severity];
  const body = h("div", { class: "impact" },
    h("p", { class: `impact-badge impact-${sev.tone}` }, `${sev.icon} ${sev.label}`),
    intro ? h("p", { class: "impact-intro" }, intro) : null,
    sections.map((s) => h("section", { class: "impact-section" },
      h("h3", {}, s.heading),
      s.items && s.items.length
        ? h("ul", {}, s.items.slice(0, 40).map((it) => h("li", {}, typeof it === "string" ? it : [it.text, it.sub ? h("small", {}, " — " + it.sub) : null])),
          s.items.length > 40 ? h("li", {}, `… et ${s.items.length - 40} autre(s)`) : null)
        : h("p", { class: "muted" }, s.empty || "Aucun"))),
    notes.length ? h("div", { class: "impact-notes" }, notes.map((n) => h("p", {}, n))) : null,
    blocked ? h("p", { class: "impact-blocked" }, blocked) : null,
  );
  let check;
  let typed;
  if (requireCheck && !blocked) {
    check = h("input", { type: "checkbox", id: "impact-check" });
    body.append(h("label", { class: "impact-check", for: "impact-check" }, check, " ", requireCheck));
  }
  if (requireType && !blocked) {
    typed = h("input", { type: "text", class: "input", autocomplete: "off", "aria-label": `Recopiez ${requireType}` });
    body.append(h("label", { class: "impact-type" }, `Pour confirmer, recopiez « ${requireType} » :`, typed));
  }
  const actions = [{ label: blocked ? "Fermer" : cancelLabel, kind: "btn-secondary", value: false }];
  if (!blocked) {
    actions.push({ label: confirmLabel, kind: severity === "danger" ? "btn-danger" : "btn-primary", value: true,
      attrs: { "data-confirm": "1" } });
  }
  return openModal({
    title, body, actions, tone: sev.tone,
    onOpen: (dialog, acts) => {
      const btn = acts[1] && acts[1].button;
      if (!btn) return;
      const refresh = () => {
        btn.disabled = (check && !check.checked) || (typed && typed.value.trim().toUpperCase() !== requireType.toUpperCase());
      };
      if (check) check.addEventListener("change", refresh);
      if (typed) typed.addEventListener("input", refresh);
      refresh();
    },
  }).then((v) => v === true);
}

/** Simple question oui / non. */
export function ask(title, message, { confirmLabel = "Oui", cancelLabel = "Non", tone = "warning" } = {}) {
  return openModal({
    title, tone, body: h("p", {}, message),
    actions: [{ label: cancelLabel, kind: "btn-secondary", value: false }, { label: confirmLabel, kind: "btn-primary", value: true }],
  }).then((v) => v === true);
}

/** Fenêtre de saisie (titre d'une nouvelle page, etc.). */
export function prompt(title, { label, value = "", help, confirmLabel = "Continuer", extra } = {}) {
  const input = h("input", { type: "text", class: "input", value });
  const body = h("div", {}, h("label", { class: "field-label" }, label, input), help ? h("p", { class: "help" }, help) : null, extra || null);
  return openModal({
    title, body,
    actions: [
      { label: "Annuler", kind: "btn-secondary", value: null },
      { label: confirmLabel, kind: "btn-primary", value: () => input.value.trim(), validate: () => input.value.trim().length > 0 },
    ],
    onOpen: () => input.focus(),
  });
}

// ------------------------------------------------------------------ Notifications

export function toast(message, tone = "success") {
  let zone = document.querySelector(".toasts");
  if (!zone) {
    zone = h("div", { class: "toasts", role: "status", "aria-live": "polite" });
    document.body.append(zone);
  }
  const t = h("div", { class: `toast toast-${tone}` }, message);
  zone.append(t);
  setTimeout(() => t.classList.add("is-leaving"), 4200);
  setTimeout(() => t.remove(), 4800);
}

export function formatDate(iso) {
  try {
    return new Date(iso).toLocaleString("fr-FR", { dateStyle: "medium", timeStyle: "short" });
  } catch {
    return iso;
  }
}
