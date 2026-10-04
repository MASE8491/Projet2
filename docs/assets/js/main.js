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
      var attr = filters.getAttribute("data-filter-attr") || "data-island";
      var shown = 0;
      document.querySelectorAll(filters.getAttribute("data-filter-items") || ".gallery-item").forEach(function (item) {
        item.hidden = value !== "all" && item.getAttribute(attr) !== value;
        if (!item.hidden) shown++;
      });
      // Masque les groupes devenus vides (contes, bibliographie)
      document.querySelectorAll("[data-filter-group]").forEach(function (group) {
        var items = group.querySelectorAll(filters.getAttribute("data-filter-items"));
        group.hidden = items.length > 0 && Array.prototype.every.call(items, function (i) { return i.hidden; });
      });
      var empty = document.querySelector("[data-filter-empty]");
      if (empty) empty.hidden = shown !== 0;
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

/* Quiz et glossaire */
(function () {
  "use strict";

  var quiz = document.querySelector("[data-quiz]");
  if (quiz) {
    var result = document.querySelector("[data-quiz-result]");
    var items = quiz.querySelectorAll(".quiz-item");
    var progress = document.querySelector("[data-quiz-progress]");
    // Mélange l'ordre des réponses (la valeur de chaque bouton reste l'index d'origine)
    var shuffle = function (item) {
      var box = item.querySelector(".quiz-choices");
      var labels = Array.prototype.slice.call(box.children);
      for (var i = labels.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = labels[i]; labels[i] = labels[j]; labels[j] = t;
      }
      labels.forEach(function (l) { box.appendChild(l); });
    };
    items.forEach(shuffle);
    var update = function () {
      var answered = 0, correct = 0;
      items.forEach(function (item) {
        if (item.dataset.done) { answered++; if (item.dataset.done === "ok") correct++; }
      });
      if (!answered) {
        if (progress) progress.textContent = "0 / " + items.length + " réponse";
        result.innerHTML = "<p>Répondez aux questions pour voir votre score.</p>";
        return;
      }
      if (progress) progress.textContent = answered + " / " + items.length + (answered > 1 ? " réponses" : " réponse");
      var msg = "Score : " + correct + " / " + answered;
      if (answered === items.length) {
        msg += correct === items.length ? " — parfait, vous connaissez les îles de la Lune !" :
               correct >= items.length * 0.6 ? " — très bien, encore un petit effort !" :
               " — continuez à explorer le site pour progresser !";
      }
      result.innerHTML = "<p>" + msg + "</p>";
    };
    quiz.addEventListener("change", function (e) {
      var input = e.target;
      if (input.type !== "radio") return;
      var item = input.closest(".quiz-item");
      if (item.dataset.done) return;
      var answer = item.getAttribute("data-answer");
      var ok = input.value === answer;
      item.dataset.done = ok ? "ok" : "ko";
      item.querySelectorAll("input").forEach(function (r) {
        r.disabled = true;
        var label = r.closest(".quiz-choice");
        if (r.value === answer) label.classList.add("is-correct");
        else if (r === input) label.classList.add("is-wrong");
      });
      item.querySelector(".quiz-explain").hidden = false;
      update();
    });
    var reset = document.querySelector("[data-quiz-reset]");
    if (reset) reset.addEventListener("click", function () {
      items.forEach(function (item) {
        delete item.dataset.done;
        item.querySelectorAll("input").forEach(function (r) { r.disabled = false; r.checked = false; });
        item.querySelectorAll(".quiz-choice").forEach(function (l) { l.classList.remove("is-correct", "is-wrong"); });
        item.querySelector(".quiz-explain").hidden = true;
        shuffle(item);
      });
      update();
      quiz.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  var search = document.querySelector("[data-glossary-search]");
  if (search) {
    var entries = document.querySelectorAll(".glossary-entry");
    var empty = document.querySelector("[data-glossary-empty]");
    var norm = function (s) { return s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); };
    search.addEventListener("input", function () {
      var q = norm(search.value.trim());
      var shown = 0;
      entries.forEach(function (entry) {
        var match = !q || norm(entry.textContent).indexOf(q) !== -1;
        entry.hidden = !match;
        if (match) shown++;
      });
      empty.hidden = shown !== 0;
    });
  }
})();
