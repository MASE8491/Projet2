#!/usr/bin/env python3
"""Générateur statique de komori.com.

Usage : python3 build.py        (génère le site dans docs/)

Les pages sont produites à partir des gabarits Jinja2 de site_src/templates et
des contenus de site_src/content_*.py. Tous les liens internes sont relatifs,
ce qui permet d'ouvrir le site directement depuis le disque ou de le servir
depuis n'importe quel hébergement statique (GitHub Pages, Netlify…).
"""

import datetime
import posixpath
import re
import shutil
import unicodedata
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, StrictUndefined, pass_context

from site_src.media import MEDIA, ISLAND_LABELS, COMMONS_FILEPATH, COMMONS_PAGE
from site_src.content_islands import ISLANDS, ISLANDS_BY_SLUG
from site_src.content_places import PLACES, PLACES_BY_SLUG
from site_src.content_experiences import EXPERIENCES, EXPERIENCES_BY_SLUG
from site_src.content_itineraries import ITINERARIES
from site_src.content_practical import PRACTICAL
from site_src.content_misc import EVENTS, VIDEOS, HOME
from site_src.content_geographie import GEOGRAPHIE
from site_src.content_histoire import HISTOIRE, TIMELINE
from site_src.content_culture import CULTURE
from site_src.content_extras import GLOSSARY, QUIZ, FACTS

TOPICS = [GEOGRAPHIE, HISTOIRE, CULTURE]

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "site_src"
OUT = ROOT / "docs"
SITE_URL = "https://komori.com"
DOMAIN = "komori.com"
UPDATED = "octobre 2026"

# Largeurs de vignettes standard de Wikimedia (évite les tailles non mises en cache)
THUMB_WIDTHS = (500, 960, 1280, 1920)

# --------------------------------------------------------------------------- Navigation

NAV = [
    dict(key="iles", label="Les îles", href="iles/index.html", children=[
        dict(label=i["name"], note=i["local"] + " · " + i["tagline"], href=f"iles/{i['slug']}.html")
        for i in ISLANDS
    ] + [dict(label="Comparer les îles", note="Tableau et carte", href="iles/index.html")]),
] + [
    dict(key=t["slug"], label=t["name"], href=f"{t['slug']}/index.html", children=[
        dict(label="Vue d'ensemble", href=f"{t['slug']}/index.html")
    ] + [
        dict(label=pg["name"], note=pg.get("period"), href=f"{t['slug']}/{pg['slug']}.html") for pg in t["pages"]
    ])
    for t in TOPICS
] + [
    dict(key="voyager", label="Voyager", href="voyager/index.html", children=[
        dict(label="Lieux incontournables", href="voyager/index.html"),
        dict(label="Expériences", href="experiences/index.html"),
        dict(label="Itinéraires", href="itineraires/index.html"),
        dict(label="Préparer son voyage", href="preparer-son-voyage/index.html"),
        dict(label="Agenda & saisons", href="agenda.html"),
    ]),
    dict(key="medias", label="Médiathèque", href="galerie.html", children=[
        dict(label="Galerie photos", href="galerie.html"),
        dict(label="Vidéos", href="videos.html"),
        dict(label="Glossaire", href="glossaire.html"),
        dict(label="Quiz", href="quiz.html"),
    ]),
]

FOOTER = [
    dict(title="Les îles", links=[dict(label=i["name"], href=f"iles/{i['slug']}.html") for i in ISLANDS]
         + [dict(label="Comparer les îles", href="iles/index.html")]),
    dict(title="Découvrir", links=[dict(label=t["name"], href=f"{t['slug']}/index.html") for t in TOPICS]
         + [dict(label="Frise chronologique", href="histoire/index.html#frise"),
            dict(label="Glossaire", href="glossaire.html"),
            dict(label="Quiz", href="quiz.html")]),
    dict(title="Voyager", links=[
        dict(label="Lieux incontournables", href="voyager/index.html"),
        dict(label="Expériences", href="experiences/index.html"),
        dict(label="Itinéraires", href="itineraires/index.html"),
        dict(label="Préparer son voyage", href="preparer-son-voyage/index.html"),
        dict(label="Agenda & saisons", href="agenda.html"),
    ]),
    dict(title="Komori", links=[
        dict(label="Galerie photos", href="galerie.html"),
        dict(label="Vidéos", href="videos.html"),
        dict(label="Contact", href="contact.html"),
        dict(label="Crédits", href="credits.html"),
        dict(label="Mentions légales", href="mentions-legales.html"),
        dict(label="Plan du site", href="plan-du-site.html"),
    ]),
]

# --------------------------------------------------------------------------- Helpers médias


def file_url(key):
    return COMMONS_FILEPATH + quote(MEDIA[key]["file"])


def img_url(key, width=1280):
    return f"{file_url(key)}?width={width}"


def img_srcset(key):
    return ", ".join(f"{img_url(key, w)} {w}w" for w in THUMB_WIDTHS)


def commons_page(key):
    return COMMONS_PAGE + quote(MEDIA[key]["file"])


def credit_text(key):
    m = MEDIA[key]
    parts = [m["author"] or "Wikimedia Commons"]
    if m["license"]:
        parts.append(m["license"])
    return "© " + ", ".join(parts)


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# --------------------------------------------------------------------------- Rendu

env = Environment(
    loader=FileSystemLoader(SRC / "templates"),
    autoescape=True,
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
)


def relative(page_path, target):
    """Lien relatif de page_path vers target (tous deux relatifs à la racine)."""
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target
    anchor = ""
    if "#" in target:
        target, anchor = target.split("#", 1)
        anchor = "#" + anchor
    start = posixpath.dirname(page_path) or "."
    return posixpath.relpath(target, start) + anchor


@pass_context
def url(ctx, target):
    if ctx.get("absolute_urls"):
        return "/" + target
    return relative(ctx["page_path"], target)


LINK_RE = re.compile(r"\[\[([^|\]]+)\|([^\]]+)\]\]")


@pass_context
def links_filter(ctx, html):
    """Convertit la syntaxe [[chemin|libellé]] en liens relatifs."""
    def repl(match):
        href, label = match.group(1), match.group(2)
        return f'<a href="{url(ctx, href)}">{label}</a>'
    return LINK_RE.sub(repl, html)


env.globals.update(
    url=url, img_url=img_url, img_srcset=img_srcset, file_url=file_url,
    commons_page=commons_page, credit_text=credit_text,
    media=MEDIA, nav=NAV, footer=FOOTER, site_url=SITE_URL,
    year=datetime.date.today().year, updated=UPDATED,
    islands=ISLANDS, islands_by_slug=ISLANDS_BY_SLUG, places=PLACES_BY_SLUG,
    experiences=EXPERIENCES, itineraries=ITINERARIES, practical=PRACTICAL,
    events=EVENTS, videos=VIDEOS, home=HOME, island_labels=ISLAND_LABELS,
    topics=TOPICS, geographie=GEOGRAPHIE, histoire=HISTOIRE, culture=CULTURE,
    timeline=None, facts=FACTS,
)
env.filters["links"] = links_filter
env.filters["slugify"] = slugify
env.filters["island_name"] = lambda slug: ISLANDS_BY_SLUG[slug]["name"]

PAGES = []  # (chemin de sortie, gabarit, contexte)


def add(path, template, title, description, og_image=None, section=None, **ctx):
    PAGES.append((path, template, dict(title=title, description=description, og_image=og_image,
                                       section=section, **ctx)))


def map_point(place):
    island = ISLANDS_BY_SLUG[place["island"]]
    return dict(name=place["name"], lat=place["coords"][0], lng=place["coords"][1],
                island=island["name"], color=island["accent"], href=f"lieux/{place['slug']}.html")


def collect_pages():
    add("index.html", "index.html", None,
        "Komori, le site de découverte des quatre îles des Comores : Grande Comore, Mohéli, Anjouan et Mayotte. "
        "Géographie, histoire, culture, folklore et tourisme.", og_image=HOME["hero"],
        timeline_highlights=[TIMELINE[i] for i in (0, 3, 7, 10, 15, 19)])

    # Les îles et les lieux
    add("iles/index.html", "iles.html", "Les quatre îles",
        "Grande Comore, Mohéli, Anjouan et Mayotte : tableau comparatif, présentation et carte interactive des quatre îles.",
        og_image="lagon_dembeni", section="iles", map_points=[map_point(p) for p in PLACES])
    for island in ISLANDS:
        add(f"iles/{island['slug']}.html", "island.html", f"{island['name']} ({island['local']})",
            island["lead"], og_image=island["hero"], section="iles", island=island)
    for place in PLACES:
        island = ISLANDS_BY_SLUG[place["island"]]
        add(f"lieux/{place['slug']}.html", "place.html", f"{place['name']} — {island['name']}", place["lead"],
            og_image=place["hero"], section="iles", place=place, island=island,
            map_point=map_point(place))

    # Rubriques de découverte
    for topic in TOPICS:
        extra = dict(timeline=TIMELINE) if topic is HISTOIRE else {}
        add(f"{topic['slug']}/index.html", "topic_index.html", topic["name"], topic["lead"],
            og_image=topic["hero"], section=topic["slug"], topic=topic, **extra)
        pages = topic["pages"]
        for idx, page in enumerate(pages):
            add(f"{topic['slug']}/{page['slug']}.html", "topic_page.html", f"{page['name']} — {topic['name']}",
                page["lead"], og_image=page["hero"], section=topic["slug"], topic=topic, page=page,
                prev_page=pages[idx - 1] if idx > 0 else None,
                next_page=pages[idx + 1] if idx + 1 < len(pages) else None)

    # Voyager
    add("voyager/index.html", "voyager.html", "Voyager aux Comores",
        "Lieux incontournables, expériences, itinéraires et informations pratiques pour découvrir les quatre îles.",
        og_image="tortue_pilote", section="voyager")
    add("experiences/index.html", "experiences.html", "Expériences",
        "Nature, plages, plongée, randonnées, patrimoine et parfums : les expériences à vivre aux Comores.",
        og_image="tortue_pilote", section="voyager")
    for exp in EXPERIENCES:
        add(f"experiences/{exp['slug']}.html", "experience.html", exp["name"], exp["lead"],
            og_image=exp["hero"], section="voyager", exp=exp)
    add("itineraires/index.html", "itineraries.html", "Itinéraires",
        "Itinéraires de 5 à 16 jours à travers l'archipel des Comores.", og_image="moroni_panorama",
        section="voyager")
    for it in ITINERARIES:
        add(f"itineraires/{it['slug']}.html", "itinerary.html", it["name"], it["lead"],
            og_image=it["hero"], section="voyager", it=it)
    add("preparer-son-voyage/index.html", "practical_index.html", "Préparer son voyage",
        "Formalités, climat, transports, santé, budget, hébergement et savoir-vivre aux Comores et à Mayotte.",
        og_image="barge", section="voyager")
    for p in PRACTICAL:
        add(f"preparer-son-voyage/{p['slug']}.html", "practical.html", p["name"], p["summary"],
            og_image=p["hero"], section="voyager", page=p)
    add("agenda.html", "agenda.html", "Agenda & saisons",
        "Fêtes, traditions et saisons de la nature dans l'archipel des Comores.", og_image="moroni_mosquee",
        section="voyager")

    # Médiathèque et outils
    gallery_keys = [k for k, m in MEDIA.items() if m["gallery"]]
    add("galerie.html", "gallery.html", "Galerie photos",
        "Photos sous licence libre des quatre îles de l'archipel des Comores : paysages, histoire, culture, faune.",
        og_image="nioumachoua_ilots", section="medias", gallery_keys=gallery_keys)
    add("videos.html", "videos.html", "Vidéos",
        "Vidéos sous licence libre de la vie marine de l'archipel des Comores : baleines, tortues, récifs.",
        og_image="baleine", section="medias")
    glossary = sorted(GLOSSARY, key=lambda g: slugify(g[0]))
    add("glossaire.html", "glossaire.html", "Glossaire",
        "Les mots comoriens et les notions utiles pour comprendre l'archipel des Comores.", section="medias",
        glossary=glossary, glossary_letters=sorted({slugify(g[0])[0].upper() for g in glossary}))
    add("quiz.html", "quiz.html", "Quiz", "Testez vos connaissances sur la géographie, l'histoire et la culture des Comores.",
        section="medias", quiz=QUIZ)

    # Pages annexes
    add("credits.html", "credits.html", "Crédits photos & vidéos",
        "Auteurs et licences des photos et vidéos utilisées sur Komori.")
    add("mentions-legales.html", "legal.html", "Mentions légales", "Mentions légales du site komori.com.")
    add("contact.html", "contact.html", "Contact", "Contacter l'équipe de Komori.")
    add("plan-du-site.html", "plan.html", "Plan du site", "Toutes les pages du site komori.com.",
        sitemap_groups=sitemap_groups())
    add("404.html", "404.html", "Page introuvable", "Cette page n'existe pas.", absolute_urls=True)


def sitemap_groups():
    groups = [
        dict(title="Les îles", links=[("Les quatre îles", "iles/index.html")]
             + [(i["name"], f"iles/{i['slug']}.html") for i in ISLANDS]),
        dict(title="Lieux", links=[(p["name"], f"lieux/{p['slug']}.html") for p in PLACES]),
    ]
    for t in TOPICS:
        groups.append(dict(title=t["name"], links=[("Vue d'ensemble", f"{t['slug']}/index.html")]
                           + [(pg["name"], f"{t['slug']}/{pg['slug']}.html") for pg in t["pages"]]))
    groups += [
        dict(title="Voyager", links=[("Voyager aux Comores", "voyager/index.html"),
                                     ("Expériences", "experiences/index.html")]
             + [(e["name"], f"experiences/{e['slug']}.html") for e in EXPERIENCES]),
        dict(title="Itinéraires", links=[("Tous les itinéraires", "itineraires/index.html")]
             + [(i["name"], f"itineraires/{i['slug']}.html") for i in ITINERARIES]),
        dict(title="Préparer son voyage", links=[("Vue d'ensemble", "preparer-son-voyage/index.html")]
             + [(p["name"], f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL]
             + [("Agenda & saisons", "agenda.html")]),
        dict(title="Komori", links=[("Galerie", "galerie.html"), ("Vidéos", "videos.html"),
                                    ("Glossaire", "glossaire.html"), ("Quiz", "quiz.html"),
                                    ("Contact", "contact.html"), ("Crédits", "credits.html"),
                                    ("Mentions légales", "mentions-legales.html")]),
    ]
    return groups


def validate():
    """Vérifie que toutes les références de contenu pointent vers des éléments existants."""
    errors = []

    def need_media(key, where):
        if key and key not in MEDIA:
            errors.append(f"{where} : média inconnu « {key} »")

    for i in ISLANDS:
        for k in [i["hero"], i["card"], *i["gallery"], *(t["media"] for t in i["themes"])]:
            need_media(k, f"île {i['slug']}")
        errors += [f"île {i['slug']} : lieu inconnu « {p} »" for p in i["places"] if p not in PLACES_BY_SLUG]
    for p in PLACES:
        for k in [p["hero"], *p["gallery"], *(s.get("media") for s in p["sections"])]:
            need_media(k, f"lieu {p['slug']}")
    for e in EXPERIENCES:
        for k in [e["hero"], e["card"], *e["gallery"], *(s.get("media") for s in e["sections"])]:
            need_media(k, f"expérience {e['slug']}")
        errors += [f"expérience {e['slug']} : lieu inconnu « {p} »" for p in e["places"] if p not in PLACES_BY_SLUG]
    for it in ITINERARIES:
        need_media(it["hero"], f"itinéraire {it['slug']}")
        need_media(it["card"], f"itinéraire {it['slug']}")
        errors += [f"itinéraire {it['slug']} : lieu inconnu « {d[3]} »" for d in it["days"]
                   if d[3] and d[3] not in PLACES_BY_SLUG]
    for p in PRACTICAL:
        need_media(p["hero"], f"pratique {p['slug']}")
    for t in TOPICS:
        need_media(t["hero"], f"rubrique {t['slug']}")
        need_media(t["card"], f"rubrique {t['slug']}")
        for pg in t["pages"]:
            for k in [pg["hero"], *pg.get("gallery", []), *(s.get("media") for s in pg["sections"])]:
                need_media(k, f"page {t['slug']}/{pg['slug']}")
    for k in VIDEOS:
        need_media(k, "vidéos")
        need_media(MEDIA[k].get("poster"), f"poster {k}")
    if errors:
        raise SystemExit("Erreurs de contenu :\n  " + "\n  ".join(errors))


def check_internal_links():
    """Vérifie que chaque lien relatif des pages générées mène à un fichier existant."""
    href_re = re.compile(r'(?:href|src)="([^"]+)"')
    broken = []
    for html_file in OUT.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        if "[[" in text:
            broken.append(f"{html_file.relative_to(OUT)} → syntaxe [[lien]] non convertie")
        for target in href_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            path = target.split("#", 1)[0]
            base = OUT if path.startswith("/") else html_file.parent
            if not (base / path.lstrip("/")).resolve().exists():
                broken.append(f"{html_file.relative_to(OUT)} → {target}")
    if broken:
        raise SystemExit("Liens internes cassés :\n  " + "\n  ".join(sorted(set(broken))))


def build():
    validate()
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC / "static", OUT / "assets")

    collect_pages()
    for path, template, ctx in PAGES:
        html = env.get_template(template).render(page_path=path, **ctx)
        target = OUT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")

    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}/{path}</loc><lastmod>{today}</lastmod></url>"
        for path, _, _ in PAGES if path != "404.html"
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n",
        encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    (OUT / "CNAME").write_text(DOMAIN + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    check_internal_links()
    print(f"{len(PAGES)} pages générées dans {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
