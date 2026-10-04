/* Komori — interactions : menu, lightbox, filtres de galerie, cartes, images manquantes */
(function () {
  "use strict";

  /* ---------------------------------------------------------- En-tête */
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------------------------------------------------------- Menu mobile */
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      document.body.classList.toggle("nav-open", open);
    });
    nav.querySelectorAll(".sub-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sub = btn.nextElementSibling;
        var open = sub.classList.toggle("is-open");
        btn.setAttribute("aria-expanded", String(open));
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-open");
        toggle.focus();
      }
    });
  }

  /* ---------------------------------------------------------- Images indisponibles
     Les images sont chargées depuis Wikimedia Commons. Si l'une d'elles ne répond
     pas, on affiche un aplat aux couleurs du site avec sa légende. */
  function markBroken(img) {
    if (img.classList.contains("is-broken")) return;
    img.classList.add("is-broken");
    var holder = img.parentElement;
    if (holder) {
      holder.classList.add("img-missing");
      holder.setAttribute("data-missing", img.getAttribute("data-fallback") || img.alt || "");
    }
  }
  document.addEventListener("error", function (e) {
    var t = e.target;
    if (t && t.tagName === "IMG") markBroken(t);
  }, true);
  document.querySelectorAll("img").forEach(function (img) {
    if (img.complete && img.naturalWidth === 0 && img.getAttribute("src")) markBroken(img);
  });

  /* ---------------------------------------------------------- Lightbox */
  var box = document.querySelector("[data-lightbox]");
  var items = [];
  var current = 0;
  function visibleItems() {
    return Array.prototype.filter.call(document.querySelectorAll("[data-lightbox-item]"), function (el) {
      return !el.hidden;
    });
  }
  function show(index) {
    if (!items.length) return;
    current = (index + items.length) % items.length;
    var item = items[current];
    var img = box.querySelector("[data-lightbox-img]");
    img.src = item.getAttribute("href");
    img.alt = item.getAttribute("data-caption") || "";
    box.querySelector("[data-lightbox-caption]").textContent = item.getAttribute("data-caption") || "";
  }
  if (box && typeof box.showModal === "function") {
    document.addEventListener("click", function (e) {
      var link = e.target.closest("[data-lightbox-item]");
      if (!link) return;
      e.preventDefault();
      items = visibleItems();
      show(items.indexOf(link));
      box.showModal();
    });
    box.querySelector("[data-lightbox-close]").addEventListener("click", function () { box.close(); });
    box.querySelector("[data-lightbox-prev]").addEventListener("click", function () { show(current - 1); });
    box.querySelector("[data-lightbox-next]").addEventListener("click", function () { show(current + 1); });
    box.addEventListener("click", function (e) { if (e.target === box) box.close(); });
    box.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") show(current - 1);
      if (e.key === "ArrowRight") show(current + 1);
    });
  }

  /* ---------------------------------------------------------- Filtres de galerie */
  var filters = document.querySelector("[data-filters]");
  if (filters) {
    filters.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-filter]");
      if (!btn) return;
      var value = btn.getAttribute("data-filter");
      filters.querySelectorAll("[data-filter]").forEach(function (b) {
        var active = b === btn;
        b.classList.toggle("is-active", active);
        b.setAttribute("aria-pressed", String(active));
      });
      document.querySelectorAll(".gallery-item").forEach(function (item) {
        item.hidden = value !== "all" && item.getAttribute("data-island") !== value;
      });
    });
  }

  /* ---------------------------------------------------------- Cartes Leaflet */
  function initMaps() {
    if (typeof window.L === "undefined") return;
    document.querySelectorAll("[data-map]").forEach(function (el) {
      var points = [];
      try { points = JSON.parse(el.getAttribute("data-map")); } catch (err) { return; }
      var center = (el.getAttribute("data-center") || "-12.25,44.2").split(",").map(Number);
      var zoom = Number(el.getAttribute("data-zoom") || 8);
      var map = L.map(el, { scrollWheelZoom: false }).setView(center, zoom);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 18,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);
      points.forEach(function (p) {
        var marker = L.circleMarker([p.lat, p.lng], {
          radius: 9, color: "#ffffff", weight: 2, fillColor: p.color, fillOpacity: 0.95
        }).addTo(map);
        var href = relativeHref(p.href);
        marker.bindPopup('<strong>' + escapeHtml(p.name) + '</strong><br>' + escapeHtml(p.island) +
          '<br><a href="' + href + '">Voir la fiche →</a>');
      });
    });
  }
  /* Les liens de la carte sont exprimés depuis la racine du site : on les rend
     relatifs à la page courante grâce à l'adresse de la feuille de style. */
  function relativeHref(target) {
    var css = document.querySelector('link[href$="assets/css/style.css"]');
    if (!css) return target;
    var prefix = css.getAttribute("href").replace(/assets\/css\/style\.css$/, "");
    return prefix + target;
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  if (document.querySelector("[data-map]")) {
    if (document.readyState === "complete") initMaps();
    else window.addEventListener("load", initMaps);
  }
})();
