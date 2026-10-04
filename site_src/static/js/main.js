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

  /* ---------------------------------------------------------- Menu tiroir (toutes les pages)
     Un <dialog> modal, hors de l'en-tête : il s'affiche au premier plan sur toutes les pages,
     quelle que soit la largeur de l'écran. */
  var drawer = document.querySelector("[data-drawer]");
  var openers = document.querySelectorAll("[data-drawer-open]");
  if (drawer && openers.length) {
    var drawerSearch = drawer.querySelector("[data-drawer-search]");
    var drawerItems = Array.prototype.slice.call(drawer.querySelectorAll("[data-drawer-item]"));
    var drawerEmpty = drawer.querySelector("[data-drawer-empty]");
    var drawerOpener = null;
    var setBranch = function (li, open) {
      var btn = li.querySelector(":scope > .drawer-row > .drawer-toggle");
      var sub = li.querySelector(":scope > .drawer-sub");
      if (!btn || !sub) return;
      sub.hidden = !open;
      btn.setAttribute("aria-expanded", String(open));
    };
    var openDrawer = function (opener) {
      drawerOpener = opener;
      if (typeof drawer.showModal === "function") drawer.showModal(); else drawer.setAttribute("open", "");
      document.body.classList.add("drawer-open");
      openers.forEach(function (b) { b.setAttribute("aria-expanded", "true"); });
      var current = drawer.querySelector('[aria-current="page"]');
      if (current) {
        current.scrollIntoView({ block: "center" });
        current.focus({ preventScroll: true });
      }
    };
    var onClosed = function () {
      document.body.classList.remove("drawer-open");
      openers.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
      if (drawerOpener) drawerOpener.focus();
    };
    var closeDrawer = function () {
      if (typeof drawer.close === "function" && drawer.open) drawer.close(); else { drawer.removeAttribute("open"); onClosed(); }
    };
    openers.forEach(function (b) { b.addEventListener("click", function () { openDrawer(b); }); });
    drawer.addEventListener("close", onClosed);
    drawer.querySelector("[data-drawer-close]").addEventListener("click", closeDrawer);
    // Clic sur le voile sombre (à côté du panneau)
    drawer.addEventListener("click", function (e) {
      if (e.target !== drawer) return;
      var r = drawer.getBoundingClientRect();
      if (e.clientX > r.right || e.clientX < r.left || e.clientY < r.top || e.clientY > r.bottom) closeDrawer();
    });
    drawer.addEventListener("click", function (e) {
      var btn = e.target.closest(".drawer-toggle");
      if (btn) { setBranch(btn.closest("[data-drawer-item]"), btn.getAttribute("aria-expanded") !== "true"); return; }
      var link = e.target.closest("a[href]");
      // Un lien vers une ancre de la page courante : on referme le tiroir pour laisser voir la cible
      if (link && link.hash && link.pathname === window.location.pathname) closeDrawer();
    });

    // Recherche : n'affiche que les pages dont le titre correspond, avec leurs rubriques parentes
    var drawerNorm = function (str) { return str.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); };
    var drawerLabel = function (li) {
      var el = li.querySelector(":scope > .drawer-row > a, :scope > .drawer-row > .drawer-label");
      return el ? el : null;
    };
    // Libellé principal (sans la petite note éventuelle) et contenu d'origine, pour pouvoir le restaurer
    drawerItems.forEach(function (li) {
      var el = drawerLabel(li);
      if (!el) return;
      var first = el.firstChild;
      el.setAttribute("data-text", first && first.nodeType === 3 ? first.nodeValue : el.textContent);
      el._original = el.innerHTML;
    });
    if (drawerSearch) drawerSearch.addEventListener("input", function () {
      var q = drawerNorm(drawerSearch.value.trim());
      var shown = 0;
      // Du plus profond au plus haut, pour savoir si un descendant correspond
      drawerItems.slice().reverse().forEach(function (li) {
        var el = drawerLabel(li);
        var text = el ? el.getAttribute("data-text") : "";
        var own = !q || drawerNorm(text).indexOf(q) !== -1;
        var childShown = Array.prototype.some.call(li.querySelectorAll(":scope > .drawer-sub > [data-drawer-item]"),
          function (c) { return !c.hidden; });
        li.hidden = !(own || childShown);
        if (q) setBranch(li, childShown);
        else setBranch(li, li.hasAttribute("data-open-default"));
        if (el) {
          if (el.querySelector("mark")) el.innerHTML = el._original;
          if (q && own) {
            var i = drawerNorm(text).indexOf(q);
            var frag = document.createDocumentFragment();
            frag.appendChild(document.createTextNode(text.slice(0, i)));
            var mark = document.createElement("mark");
            mark.textContent = text.slice(i, i + q.length);
            frag.appendChild(mark);
            frag.appendChild(document.createTextNode(text.slice(i + q.length)));
            var first = el.firstChild;
            if (first && first.nodeType === 3) el.replaceChild(frag, first); else { el.textContent = ""; el.appendChild(frag); }
          }
        }
        if (!li.hidden && own && q) shown++;
      });
      if (drawerEmpty) drawerEmpty.hidden = !q || shown > 0;
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

  /* ---------------------------------------------------------- Filtres (galerie, contes, spots, institutions…)
     Chaque barre [data-filters] filtre les éléments [data-filter-items] selon un attribut ;
     plusieurs barres se combinent (île + catégorie, par exemple). */
  var bars = Array.prototype.slice.call(document.querySelectorAll("[data-filters]"));
  if (bars.length) {
    var applyFilters = function () {
      var selector = bars[0].getAttribute("data-filter-items") || ".gallery-item";
      var active = bars.map(function (bar) {
        var on = bar.querySelector("[data-filter].is-active");
        return { attr: bar.getAttribute("data-filter-attr") || "data-island", value: on ? on.getAttribute("data-filter") : "all" };
      });
      var shown = 0;
      document.querySelectorAll(selector).forEach(function (item) {
        item.hidden = !active.every(function (f) { return f.value === "all" || item.getAttribute(f.attr) === f.value; });
        if (!item.hidden) shown++;
      });
      // Masque les groupes devenus vides (contes, bibliographie, spots, institutions)
      document.querySelectorAll("[data-filter-group]").forEach(function (group) {
        var inside = group.querySelectorAll(selector);
        group.hidden = inside.length > 0 && Array.prototype.every.call(inside, function (i) { return i.hidden; });
      });
      var empty = document.querySelector("[data-filter-empty]");
      if (empty) empty.hidden = shown !== 0;
    };
    bars.forEach(function (bar) {
      bar.addEventListener("click", function (e) {
        var btn = e.target.closest("[data-filter]");
        if (!btn) return;
        bar.querySelectorAll("[data-filter]").forEach(function (b) {
          var on = b === btn;
          b.classList.toggle("is-active", on);
          b.setAttribute("aria-pressed", String(on));
        });
        applyFilters();
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
