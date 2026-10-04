#!/usr/bin/env python3
"""Générateur statique du site Komori.

Usage : python3 build.py        (génère le site dans docs/)

Tout le contenu éditorial se trouve dans content/*.json. Ces fichiers sont modifiés par
l'interface d'administration (docs/admin/, publiée avec le site) ou à la main. Les gabarits
Jinja2 de site_src/templates mettent ce contenu en forme. Tous les liens internes sont
relatifs, ce qui permet d'ouvrir le site depuis le disque ou de le servir depuis n'importe
quel hébergement statique.
"""

import datetime
import json
import posixpath
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, StrictUndefined, pass_context

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "site_src"
CONTENT = ROOT / "content"
OUT = ROOT / "docs"

COMMONS_FILEPATH = "https://commons.wikimedia.org/wiki/Special:FilePath/"
COMMONS_PAGE = "https://commons.wikimedia.org/wiki/File:"
# Largeurs de vignettes standard de Wikimedia (évite les tailles non mises en cache)
THUMB_WIDTHS = (500, 960, 1280, 1920)

# Dossiers occupés par le générateur : une rubrique ne peut pas porter ces noms.
RESERVED_SLUGS = {"iles", "lieux", "experiences", "itineraires", "preparer-son-voyage", "voyager",
                  "assets", "admin", "index", "galerie", "videos", "agenda", "glossaire", "quiz",
                  "credits", "contact", "mentions-legales", "plan-du-site", "404"}

CONTENT_FILES = ["settings", "navigation", "media", "home", "pages", "islands", "places", "topics",
                 "timeline", "experiences", "itineraries", "practical", "events", "glossary", "quiz",
                 "videos"]


def load(name):
    return json.loads((CONTENT / f"{name}.json").read_text(encoding="utf-8"))


def is_published(item):
    return item.get("published", True) is not False


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# --------------------------------------------------------------------------- Chargement du contenu

RAW = {name: load(name) for name in CONTENT_FILES}
SETTINGS = RAW["settings"]

OWNER, _, REPO = SETTINGS.get("github_repo", "MASE8491/Projet2").partition("/")
CUSTOM_DOMAIN = (SETTINGS.get("custom_domain") or "").strip() or None
if CUSTOM_DOMAIN:
    SITE_URL, BASE_PATH = f"https://{CUSTOM_DOMAIN}", "/"
elif REPO.lower() == f"{OWNER.lower()}.github.io":
    SITE_URL, BASE_PATH = f"https://{OWNER.lower()}.github.io", "/"
else:
    SITE_URL, BASE_PATH = f"https://{OWNER.lower()}.github.io/{REPO}", f"/{REPO}/"
CONTACT_EMAIL = (SETTINGS.get("contact_email") or "").strip() or None

MEDIA = RAW["media"]
for _key, _m in MEDIA.items():
    _m.setdefault("kind", "image")
    _m.setdefault("gallery", _m["kind"] == "image")
    _m.setdefault("author", None)
    _m.setdefault("license", None)
    _m["key"] = _key
MEDIA_LABELS = SETTINGS.get("media_categories", {})

ISLANDS = [i for i in RAW["islands"] if is_published(i)]
ISLANDS_BY_SLUG = {i["slug"]: i for i in ISLANDS}

PLACES = [p for p in RAW["places"] if is_published(p) and p["island"] in ISLANDS_BY_SLUG]
PLACES_BY_SLUG = {p["slug"]: p for p in PLACES}
for _island in ISLANDS:
    listed = [s for s in _island.get("places", []) if s in PLACES_BY_SLUG
              and PLACES_BY_SLUG[s]["island"] == _island["slug"]]
    # Un lieu rattaché à l'île mais absent de sa liste est ajouté à la fin plutôt qu'oublié.
    listed += [p["slug"] for p in PLACES if p["island"] == _island["slug"] and p["slug"] not in listed]
    _island["places"] = listed

TOPICS = []
for _t in RAW["topics"]:
    if is_published(_t):
        _t["pages"] = [pg for pg in _t.get("pages", []) if is_published(pg)]
        TOPICS.append(_t)

EXPERIENCES = [e for e in RAW["experiences"] if is_published(e)]
for _e in EXPERIENCES:
    _e["places"] = [s for s in _e.get("places", []) if s in PLACES_BY_SLUG]

ITINERARIES = [i for i in RAW["itineraries"] if is_published(i)]
for _it in ITINERARIES:
    _it["islands"] = [s for s in _it.get("islands", []) if s in ISLANDS_BY_SLUG]
    for _d in _it["days"]:
        if _d.get("place") not in PLACES_BY_SLUG:
            _d["place"] = None

PRACTICAL = [p for p in RAW["practical"] if is_published(p)]
TIMELINE = RAW["timeline"]
EVENTS = RAW["events"]
GLOSSARY = sorted(RAW["glossary"], key=lambda g: slugify(g["term"]))
QUIZ = RAW["quiz"]
VIDEOS = [k for k in RAW["videos"]["items"] if k in MEDIA and MEDIA[k]["kind"] == "video"]
HOME = RAW["home"]
PG = RAW["pages"]
NAVIGATION = RAW["navigation"]

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
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target
    if ctx.get("absolute_urls"):
        return BASE_PATH + target
    return relative(ctx["page_path"], target)


# ---- médias : fichiers Wikimedia Commons (« file ») ou images téléversées (« src »)

@pass_context
def file_url(ctx, key):
    m = MEDIA[key]
    if m.get("src"):
        return url(ctx, "assets/" + m["src"])
    return COMMONS_FILEPATH + quote(m["file"])


@pass_context
def img_url(ctx, key, width=1280):
    m = MEDIA[key]
    if m.get("src"):
        return url(ctx, "assets/" + m["src"])
    return f"{COMMONS_FILEPATH}{quote(m['file'])}?width={width}"


@pass_context
def img_srcset(ctx, key):
    if MEDIA[key].get("src"):
        return ""
    return ", ".join(f"{img_url(ctx, key, w)} {w}w" for w in THUMB_WIDTHS)


def img_abs(key, width=1280):
    m = MEDIA[key]
    if m.get("src"):
        return f"{SITE_URL}/assets/{m['src']}"
    return f"{COMMONS_FILEPATH}{quote(m['file'])}?width={width}"


@pass_context
def commons_page(ctx, key):
    m = MEDIA[key]
    if m.get("src"):
        return url(ctx, "assets/" + m["src"])
    return COMMONS_PAGE + quote(m["file"])


def credit_text(key):
    m = MEDIA[key]
    parts = [m["author"] or ("Komori" if m.get("src") else "Wikimedia Commons")]
    if m["license"]:
        parts.append(m["license"])
    return "© " + ", ".join(parts)


LINK_RE = re.compile(r"\[\[([^|\]]+)\|([^\]]+)\]\]")
LINK_WARNINGS = set()


@pass_context
def links_filter(ctx, html):
    """Convertit la syntaxe [[chemin|libellé]] en liens relatifs.

    Un lien vers une page masquée ou supprimée devient du texte simple (avec un avertissement)
    pour ne jamais publier de lien cassé.
    """
    def repl(match):
        href, label = match.group(1).strip(), match.group(2)
        if href.startswith(("http://", "https://", "mailto:")):
            return f'<a href="{href}" rel="noopener">{label}</a>'
        if href.split("#", 1)[0] not in PATHS:
            LINK_WARNINGS.add(f"{ctx['page_path']} : lien vers « {href} » retiré (page absente ou masquée)")
            return label
        return f'<a href="{url(ctx, href)}">{label}</a>'
    return LINK_RE.sub(repl, html or "")


env.globals.update(
    url=url, img_url=img_url, img_srcset=img_srcset, img_abs=img_abs, file_url=file_url,
    commons_page=commons_page, credit_text=credit_text,
    media=MEDIA, settings=SETTINGS, site_url=SITE_URL, contact_email=CONTACT_EMAIL,
    year=datetime.date.today().year, updated=SETTINGS.get("updated_label", ""),
    islands=ISLANDS, islands_by_slug=ISLANDS_BY_SLUG, places=PLACES_BY_SLUG,
    experiences=EXPERIENCES, itineraries=ITINERARIES, practical=PRACTICAL,
    events=EVENTS, videos=VIDEOS, home=HOME, island_labels=MEDIA_LABELS, pg=PG,
    topics=TOPICS, timeline=None, facts=HOME.get("facts", []),
)
env.filters["links"] = links_filter
env.filters["slugify"] = slugify
env.filters["island_name"] = lambda slug: ISLANDS_BY_SLUG[slug]["name"]

PAGES = []  # (chemin de sortie, gabarit, contexte)
PATHS = set()


def add(path, template, title, description, og_image=None, section=None, **ctx):
    PAGES.append((path, template, dict(title=title, description=description, og_image=og_image,
                                       section=section, **ctx)))


def map_point(place):
    island = ISLANDS_BY_SLUG[place["island"]]
    return dict(name=place["name"], lat=place["coords"][0], lng=place["coords"][1],
                island=island["name"], color=island["accent"], href=f"lieux/{place['slug']}.html")


def collect_pages():
    add("index.html", "index.html", None, SETTINGS.get("description", ""), og_image=HOME["hero"],
        timeline_highlights=[t for t in TIMELINE if t.get("highlight")])

    # Les îles et les lieux
    add("iles/index.html", "iles.html", PG["iles"]["title"], PG["iles"]["description"],
        og_image=PG["iles"]["hero"], section="iles", map_points=[map_point(p) for p in PLACES])
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
        extra = dict(timeline=TIMELINE) if topic.get("show_timeline") else {}
        add(f"{topic['slug']}/index.html", "topic_index.html", topic["name"], topic["lead"],
            og_image=topic["hero"], section=topic["slug"], topic=topic, **extra)
        pages = topic["pages"]
        for idx, page in enumerate(pages):
            add(f"{topic['slug']}/{page['slug']}.html", "topic_page.html", f"{page['name']} — {topic['name']}",
                page["lead"], og_image=page["hero"], section=topic["slug"], topic=topic, page=page,
                prev_page=pages[idx - 1] if idx > 0 else None,
                next_page=pages[idx + 1] if idx + 1 < len(pages) else None)

    # Voyager
    add("voyager/index.html", "voyager.html", PG["voyager"]["title"], PG["voyager"]["description"],
        og_image=PG["voyager"]["hero"], section="voyager")
    add("experiences/index.html", "experiences.html", PG["experiences"]["title"], PG["experiences"]["description"],
        og_image=PG["experiences"]["hero"], section="voyager")
    for exp in EXPERIENCES:
        add(f"experiences/{exp['slug']}.html", "experience.html", exp["name"], exp["lead"],
            og_image=exp["hero"], section="voyager", exp=exp)
    add("itineraires/index.html", "itineraries.html", PG["itineraires"]["title"], PG["itineraires"]["description"],
        og_image=PG["itineraires"]["hero"], section="voyager")
    for it in ITINERARIES:
        add(f"itineraires/{it['slug']}.html", "itinerary.html", it["name"], it["lead"],
            og_image=it["hero"], section="voyager", it=it)
    add("preparer-son-voyage/index.html", "practical_index.html", PG["preparer"]["title"],
        PG["preparer"]["description"], og_image=PG["preparer"]["hero"], section="voyager")
    for p in PRACTICAL:
        add(f"preparer-son-voyage/{p['slug']}.html", "practical.html", p["name"], p["summary"],
            og_image=p["hero"], section="voyager", page=p)
    add("agenda.html", "agenda.html", PG["agenda"]["title"], PG["agenda"]["description"],
        og_image=PG["agenda"]["hero"], section="voyager")

    # Médiathèque et outils
    gallery_keys = [k for k, m in MEDIA.items() if m["gallery"]]
    add("galerie.html", "gallery.html", PG["galerie"]["title"], PG["galerie"]["description"],
        og_image=PG["galerie"]["hero"], section="medias", gallery_keys=gallery_keys)
    add("videos.html", "videos.html", PG["videos"]["title"], PG["videos"]["description"],
        og_image=PG["videos"]["hero"], section="medias")
    add("glossaire.html", "glossaire.html", PG["glossaire"]["title"], PG["glossaire"]["description"],
        section="medias", glossary=GLOSSARY,
        glossary_letters=sorted({slugify(g["term"])[0].upper() for g in GLOSSARY}))
    add("quiz.html", "quiz.html", "Quiz", PG["quiz"]["description"], section="medias", quiz=QUIZ)

    # Pages annexes
    add("credits.html", "credits.html", PG["credits"]["title"], PG["credits"]["description"])
    add("mentions-legales.html", "legal.html", PG["mentions"]["title"], PG["mentions"]["description"])
    add("contact.html", "contact.html", PG["contact"]["title"], PG["contact"]["description"])
    add("plan-du-site.html", "plan.html", PG["plan"]["title"], PG["plan"]["description"],
        sitemap_groups=sitemap_groups())
    add("404.html", "404.html", "Page introuvable", PG["404"]["description"], absolute_urls=True)


def sitemap_groups():
    groups = [
        dict(title="Les îles", links=[(PG["iles"]["title"], "iles/index.html")]
             + [(i["name"], f"iles/{i['slug']}.html") for i in ISLANDS]),
        dict(title="Lieux", links=[(p["name"], f"lieux/{p['slug']}.html") for p in PLACES]),
    ]
    for t in TOPICS:
        groups.append(dict(title=t["name"], links=[("Vue d'ensemble", f"{t['slug']}/index.html")]
                           + [(pg["name"], f"{t['slug']}/{pg['slug']}.html") for pg in t["pages"]]))
    groups += [
        dict(title="Voyager", links=[(PG["voyager"]["title"], "voyager/index.html"),
                                     (PG["experiences"]["title"], "experiences/index.html")]
             + [(e["name"], f"experiences/{e['slug']}.html") for e in EXPERIENCES]),
        dict(title="Itinéraires", links=[("Tous les itinéraires", "itineraires/index.html")]
             + [(i["name"], f"itineraires/{i['slug']}.html") for i in ITINERARIES]),
        dict(title="Préparer son voyage", links=[("Vue d'ensemble", "preparer-son-voyage/index.html")]
             + [(p["name"], f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL]
             + [(PG["agenda"]["title"], "agenda.html")]),
        dict(title=SETTINGS.get("site_name", "Komori"), links=[
            ("Galerie", "galerie.html"), ("Vidéos", "videos.html"), ("Glossaire", "glossaire.html"),
            ("Quiz", "quiz.html"), ("Contact", "contact.html"), ("Crédits", "credits.html"),
            ("Mentions légales", "mentions-legales.html")]),
    ]
    return groups


# --------------------------------------------------------------------------- Menu et pied de page

def link_ok(link):
    if not link:
        return False
    if link.startswith(("http://", "https://", "mailto:")):
        return True
    return link.split("#", 1)[0] in PATHS


def auto_children(kind):
    """Sous-menus générés automatiquement à partir du contenu."""
    if kind == "iles":
        return [dict(label=i["name"], note=i["local"] + " · " + i["tagline"], href=f"iles/{i['slug']}.html")
                for i in ISLANDS]
    if kind.startswith("rubrique:"):
        topic = next((t for t in TOPICS if t["slug"] == kind.split(":", 1)[1]), None)
        if not topic:
            return []
        return [dict(label="Vue d'ensemble", note=None, href=f"{topic['slug']}/index.html")] + [
            dict(label=pg["name"], note=pg.get("period"), href=f"{topic['slug']}/{pg['slug']}.html")
            for pg in topic["pages"]]
    if kind == "experiences":
        return [dict(label=e["name"], note=None, href=f"experiences/{e['slug']}.html") for e in EXPERIENCES]
    if kind == "itineraires":
        return [dict(label=i["name"], note=i["duration"], href=f"itineraires/{i['slug']}.html") for i in ITINERARIES]
    if kind == "pratique":
        return [dict(label=p["name"], note=None, href=f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL]
    return []


def section_key(link):
    """Rubrique du menu à mettre en surbrillance pour un lien donné."""
    first = link.split("/", 1)[0] if "/" in link else ""
    if first in ("iles", "lieux"):
        return "iles"
    if first in ("voyager", "experiences", "itineraires", "preparer-son-voyage") or link == "agenda.html":
        return "voyager"
    if link in ("galerie.html", "videos.html", "glossaire.html", "quiz.html"):
        return "medias"
    return first or link


def resolve_navigation():
    menu = []
    for item in NAVIGATION["menu"]:
        if not link_ok(item.get("link")):
            continue
        children = auto_children(item.get("auto_children") or "")
        children += [dict(label=c["label"], note=c.get("note") or None, href=c["link"])
                     for c in item.get("children", []) if link_ok(c.get("link"))]
        menu.append(dict(key=section_key(item["link"]), label=item["label"], href=item["link"],
                         children=children or None))
    cta = NAVIGATION.get("cta") or {}
    footer = [dict(title=col["title"], links=[dict(label=l["label"], href=l["link"])
                                              for l in col["links"] if link_ok(l.get("link"))])
              for col in NAVIGATION.get("footer", [])]
    return menu, (cta if link_ok(cta.get("link")) else None), footer


# --------------------------------------------------------------------------- Vérifications

def validate():
    """Vérifie que toutes les références du contenu publié pointent vers des éléments existants."""
    errors = []

    def need_media(key, where):
        if key and key not in MEDIA:
            errors.append(f"{where} : média inconnu « {key} »")

    def unique(items, where):
        seen = set()
        for item in items:
            if not item.get("slug"):
                errors.append(f"{where} : un élément n'a pas d'adresse (slug)")
            elif item["slug"] in seen:
                errors.append(f"{where} : l'adresse « {item['slug']} » est utilisée deux fois")
            seen.add(item.get("slug"))

    unique(RAW["islands"], "Îles")
    unique(RAW["places"], "Lieux")
    unique(RAW["topics"], "Rubriques")
    unique(RAW["experiences"], "Expériences")
    unique(RAW["itineraries"], "Itinéraires")
    unique(RAW["practical"], "Infos pratiques")
    for t in RAW["topics"]:
        unique(t.get("pages", []), f"Rubrique {t.get('slug')}")
        if t.get("slug") in RESERVED_SLUGS:
            errors.append(f"Rubrique : l'adresse « {t['slug']} » est réservée par le site")

    for i in ISLANDS:
        for k in [i["hero"], i["card"], *i.get("gallery", []), *(t.get("media") for t in i["themes"])]:
            need_media(k, f"île {i['slug']}")
    for p in PLACES:
        for k in [p["hero"], *p.get("gallery", []), *(s.get("media") for s in p["sections"])]:
            need_media(k, f"lieu {p['slug']}")
    for e in EXPERIENCES:
        for k in [e["hero"], e["card"], *e.get("gallery", []), *(s.get("media") for s in e["sections"])]:
            need_media(k, f"expérience {e['slug']}")
    for it in ITINERARIES:
        need_media(it["hero"], f"itinéraire {it['slug']}")
        need_media(it["card"], f"itinéraire {it['slug']}")
    for p in PRACTICAL:
        need_media(p["hero"], f"pratique {p['slug']}")
        for s in p["sections"]:
            need_media(s.get("media"), f"pratique {p['slug']}")
    for t in TOPICS:
        need_media(t["hero"], f"rubrique {t['slug']}")
        need_media(t["card"], f"rubrique {t['slug']}")
        for pg in t["pages"]:
            for k in [pg["hero"], *pg.get("gallery", []), *(s.get("media") for s in pg["sections"])]:
                need_media(k, f"page {t['slug']}/{pg['slug']}")
    need_media(HOME["hero"], "accueil")
    for k in [*HOME.get("gallery", []), *(f["media"] for f in HOME.get("features", []))]:
        need_media(k, "accueil")
    for name, page in PG.items():
        need_media(page.get("hero"), f"page {name}")
    for k, m in MEDIA.items():
        if not m.get("file") and not m.get("src"):
            errors.append(f"média « {k} » : aucun fichier")
        need_media(m.get("poster"), f"affiche de la vidéo {k}")
    if errors:
        raise SystemExit("Erreurs de contenu :\n  " + "\n  ".join(errors))


def check_internal_links():
    """Vérifie que chaque lien relatif des pages générées mène à un fichier existant."""
    href_re = re.compile(r'(?:href|src)="([^"]+)"')
    broken = []
    for html_file in OUT.rglob("*.html"):
        if "admin" in html_file.relative_to(OUT).parts:
            continue
        text = html_file.read_text(encoding="utf-8")
        if "[[" in text:
            broken.append(f"{html_file.relative_to(OUT)} → syntaxe [[lien]] non convertie")
        for target in href_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            path = target.split("#", 1)[0]
            if path.startswith("/"):
                if not path.startswith(BASE_PATH):
                    broken.append(f"{html_file.relative_to(OUT)} → {target} (hors de {BASE_PATH})")
                    continue
                base, path = OUT, path[len(BASE_PATH):]
            else:
                base = html_file.parent
            if not (base / path).resolve().exists():
                broken.append(f"{html_file.relative_to(OUT)} → {target}")
    if broken:
        raise SystemExit("Liens internes cassés :\n  " + "\n  ".join(sorted(set(broken))))


# --------------------------------------------------------------------------- Construction

def build():
    validate()
    collect_pages()
    PATHS.update(path for path, _, _ in PAGES)
    menu, cta, footer = resolve_navigation()
    env.globals.update(nav=menu, nav_cta=cta, footer=footer)

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC / "static", OUT / "assets")
    shutil.copytree(SRC / "admin", OUT / "admin")
    (OUT / "admin" / "config.json").write_text(json.dumps({
        "repo": f"{OWNER}/{REPO}",
        "branch": SETTINGS.get("github_branch", "main"),
        "site_url": SITE_URL,
        "content_dir": "content",
        "content_files": CONTENT_FILES,
        "uploads_dir": "site_src/static/uploads",
        "reserved_slugs": sorted(RESERVED_SLUGS),
        "built_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: {BASE_PATH}admin/\nSitemap: {SITE_URL}/sitemap.xml\n",
        encoding="utf-8")
    if CUSTOM_DOMAIN:
        (OUT / "CNAME").write_text(CUSTOM_DOMAIN + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    check_internal_links()
    for warning in sorted(LINK_WARNINGS):
        print("Avertissement :", warning, file=sys.stderr)
    print(f"{len(PAGES)} pages générées dans {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
