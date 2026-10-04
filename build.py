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
from site_src.content_misc import ARCHIPEL, EVENTS, VIDEOS, HOME

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
    dict(key="destinations", label="Destinations", href="destinations/index.html", children=[
        dict(label=i["name"], note=i["local"] + " · " + i["tagline"], href=f"destinations/{i['slug']}.html")
        for i in ISLANDS
    ] + [dict(label="Découvrir l'archipel", note="Géographie & histoire", href="archipel.html")]),
    dict(key="experiences", label="Expériences", href="experiences/index.html", children=[
        dict(label=e["name"], href=f"experiences/{e['slug']}.html") for e in EXPERIENCES
    ]),
    dict(key="itineraires", label="Itinéraires", href="itineraires/index.html", children=[
        dict(label=i["name"], note=i["duration"], href=f"itineraires/{i['slug']}.html") for i in ITINERARIES
    ]),
    dict(key="preparer", label="Préparer", href="preparer-son-voyage/index.html", children=[
        dict(label=p["name"], href=f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL
    ]),
    dict(key="medias", label="Galerie & vidéos", href="galerie.html", children=[
        dict(label="Galerie photos", href="galerie.html"),
        dict(label="Vidéos", href="videos.html"),
    ]),
    dict(key="agenda", label="Agenda", href="agenda.html", children=None),
]

FOOTER = [
    dict(title="Destinations", links=[dict(label=i["name"], href=f"destinations/{i['slug']}.html") for i in ISLANDS]
         + [dict(label="Découvrir l'archipel", href="archipel.html")]),
    dict(title="Expériences", links=[dict(label=e["name"], href=f"experiences/{e['slug']}.html") for e in EXPERIENCES[:5]]
         + [dict(label="Itinéraires", href="itineraires/index.html")]),
    dict(title="Préparer", links=[dict(label=p["name"], href=f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL[:5]]
         + [dict(label="Agenda", href="agenda.html")]),
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
    archipel=ARCHIPEL, events=EVENTS, videos=VIDEOS, home=HOME,
    island_labels=ISLAND_LABELS,
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
        "Komori, le guide de voyage de l'archipel des Comores : Grande Comore, Mohéli, Anjouan et Mayotte. "
        "Volcans, lagons, plages, culture et infos pratiques.", og_image=HOME["hero"])

    # Destinations
    add("destinations/index.html", "destinations.html", "Destinations",
        "Les quatre îles de l'archipel des Comores : Grande Comore, Mohéli, Anjouan et Mayotte, avec une carte interactive.",
        og_image="lagon_dembeni", section="destinations", map_points=[map_point(p) for p in PLACES])
    for island in ISLANDS:
        add(f"destinations/{island['slug']}.html", "island.html", f"{island['name']} ({island['local']})",
            island["lead"], og_image=island["hero"], section="destinations", island=island)
    for place in PLACES:
        island = ISLANDS_BY_SLUG[place["island"]]
        add(f"lieux/{place['slug']}.html", "place.html", f"{place['name']} — {island['name']}", place["lead"],
            og_image=place["hero"], section="destinations", place=place, island=island,
            map_point=map_point(place))
    add("archipel.html", "archipel.html", "Découvrir l'archipel", ARCHIPEL["lead"],
        og_image=ARCHIPEL["hero"], section="destinations")

    # Expériences
    add("experiences/index.html", "experiences.html", "Expériences",
        "Nature, plages, plongée, randonnées, culture, gastronomie et parfums : les expériences à vivre aux Comores.",
        og_image="tortue_pilote", section="experiences")
    for exp in EXPERIENCES:
        add(f"experiences/{exp['slug']}.html", "experience.html", exp["name"], exp["lead"],
            og_image=exp["hero"], section="experiences", exp=exp)

    # Itinéraires
    add("itineraires/index.html", "itineraries.html", "Itinéraires",
        "Itinéraires de 5 à 16 jours à travers l'archipel des Comores.", og_image="moroni_panorama",
        section="itineraires")
    for it in ITINERARIES:
        add(f"itineraires/{it['slug']}.html", "itinerary.html", it["name"], it["lead"],
            og_image=it["hero"], section="itineraires", it=it)

    # Préparer son voyage
    add("preparer-son-voyage/index.html", "practical_index.html", "Préparer son voyage",
        "Formalités, climat, transports, santé, budget, hébergement et savoir-vivre aux Comores et à Mayotte.",
        og_image="barge", section="preparer")
    for p in PRACTICAL:
        add(f"preparer-son-voyage/{p['slug']}.html", "practical.html", p["name"], p["summary"],
            og_image=p["hero"], section="preparer", page=p)

    # Médias, agenda, pages annexes
    gallery_keys = [k for k, m in MEDIA.items() if m["gallery"]]
    add("galerie.html", "gallery.html", "Galerie photos",
        "Photos sous licence libre des quatre îles de l'archipel des Comores.", og_image="nioumachoua_ilots",
        section="medias", gallery_keys=gallery_keys)
    add("videos.html", "videos.html", "Vidéos",
        "Vidéos sous licence libre de la vie marine de l'archipel des Comores : baleines, tortues, récifs.",
        og_image="baleine", section="medias")
    add("agenda.html", "agenda.html", "Agenda & saisons",
        "Fêtes, traditions et saisons de la nature dans l'archipel des Comores.", og_image="moroni_mosquee",
        section="agenda")
    add("credits.html", "credits.html", "Crédits photos & vidéos",
        "Auteurs et licences des photos et vidéos utilisées sur Komori.")
    add("mentions-legales.html", "legal.html", "Mentions légales", "Mentions légales du site komori.com.")
    add("contact.html", "contact.html", "Contact", "Contacter l'équipe de Komori.")
    add("plan-du-site.html", "plan.html", "Plan du site", "Toutes les pages du site komori.com.",
        sitemap_groups=sitemap_groups())
    add("404.html", "404.html", "Page introuvable", "Cette page n'existe pas.", absolute_urls=True)


def sitemap_groups():
    return [
        dict(title="Destinations", links=[("Toutes les destinations", "destinations/index.html"),
                                          ("Découvrir l'archipel", "archipel.html")]
             + [(i["name"], f"destinations/{i['slug']}.html") for i in ISLANDS]),
        dict(title="Lieux", links=[(p["name"], f"lieux/{p['slug']}.html") for p in PLACES]),
        dict(title="Expériences", links=[("Toutes les expériences", "experiences/index.html")]
             + [(e["name"], f"experiences/{e['slug']}.html") for e in EXPERIENCES]),
        dict(title="Itinéraires", links=[("Tous les itinéraires", "itineraires/index.html")]
             + [(i["name"], f"itineraires/{i['slug']}.html") for i in ITINERARIES]),
        dict(title="Préparer son voyage", links=[("Vue d'ensemble", "preparer-son-voyage/index.html")]
             + [(p["name"], f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL]),
        dict(title="Komori", links=[("Galerie", "galerie.html"), ("Vidéos", "videos.html"),
                                    ("Agenda", "agenda.html"), ("Contact", "contact.html"),
                                    ("Crédits", "credits.html"), ("Mentions légales", "mentions-legales.html")]),
    ]


def validate():
    """Vérifie que toutes les références de contenu pointent vers des éléments existants."""
    errors = []

    def need_media(key, where):
        if key and key not in MEDIA:
            errors.append(f"{where} : média inconnu « {key} »")

    for i in ISLANDS:
        for k in [i["hero"], i["card"], *i["gallery"], *(s["media"] for s in i["sections"])]:
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
        if html_file.name == "404.html":
            continue
        for target in href_re.findall(html_file.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            path = target.split("#", 1)[0]
            if not (html_file.parent / path).resolve().exists():
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
