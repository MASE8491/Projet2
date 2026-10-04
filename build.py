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
import itertools
import json
import posixpath
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, StrictUndefined, pass_context
from markupsafe import Markup, escape

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
                  "credits", "contact", "mentions-legales", "plan-du-site", "404", "contes", "loisirs",
                  "bibliographie"}

CONTENT_FILES = ["settings", "navigation", "media", "home", "pages", "islands", "places", "topics",
                 "timeline", "experiences", "itineraries", "practical", "events", "glossary", "quizzes",
                 "videos", "tales", "bibliography", "spots", "institutions"]

# Adresses occupées dans le dossier iles/ : une île ne peut pas porter ces noms.
RESERVED_ISLAND_SLUGS = {"index", "bons-plans", "vie-publique"}

# Catégories des récits de la zone « Hale halele », dans l'ordre d'affichage
TALE_KINDS = {"mythe": "Mythes des origines", "legende": "Légendes de lieux",
              "recit": "Récits d'hier et d'aujourd'hui", "conte": "Contes du soir"}
TALE_KIND_SINGULAR = {"mythe": "Mythe des origines", "legende": "Légende de lieu",
                      "recit": "Récit", "conte": "Conte"}
# Spots & bons plans : catégories (avec leur icône) et notoriété
SPOT_CATEGORIES = {"marche": ("Marchés & commerces", "basket"), "artisanat": ("Artisanat & savoir-faire", "needle"),
                   "saveurs": ("Saveurs & tables", "bowl"), "plage": ("Plages & îlots", "wave"),
                   "nature": ("Nature & randonnée", "leaf"), "patrimoine": ("Patrimoine & histoire", "dome"),
                   "culture": ("Culture & sorties", "drum")}
SPOT_FAME = {"incontournable": "Incontournable", "meconnu": "Secret local"}
# Vie publique & institutions : catégories (avec leur icône), statuts et portée
INSTITUTION_CATEGORIES = {"politique": ("Pouvoirs publics", "building"), "justice": ("Justice", "scale"),
                          "religion": ("Autorités religieuses", "dome"), "coutume": ("Coutume & notabilité", "people"),
                          "environnement": ("Environnement", "leaf"), "culture": ("Savoir, culture & médias", "book"),
                          "sport": ("Sport", "ball"), "societe": ("Associations & société civile", "chat")}
INSTITUTION_STATUS = {"officiel": "Institution officielle", "coutume": "Autorité coutumière ou religieuse",
                      "associatif": "Association"}
INSTITUTION_SCOPES = {"ile": "Propre à l'île", "union": "Union des Comores", "archipel": "Tout l'archipel"}
# Catégories de la bibliographie, dans l'ordre d'affichage
BIBLIO_CATEGORIES = {"chronique": "Chroniques et manuscrits", "tradition": "Traditions orales et littérature",
                     "histoire": "Études historiques", "anthropologie": "Anthropologie et société",
                     "archeologie": "Archéologie et sciences", "temoins": "Voyageurs et témoins",
                     "contes": "Recueils de contes", "documents": "Textes officiels et rapports"}


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
QUIZZES = [q for q in RAW["quizzes"] if is_published(q)]
TALES = [t for t in RAW["tales"] if is_published(t)]
for _t in TALES:
    if _t.get("island") not in ISLANDS_BY_SLUG:
        _t["island"] = ""
    if _t.get("place") not in PLACES_BY_SLUG:
        _t["place"] = ""
    if _t.get("kind") not in TALE_KINDS:
        _t["kind"] = "conte"
TALES_BY_KIND = [(k, label, [t for t in TALES if t["kind"] == k]) for k, label in TALE_KINDS.items()]
TALES_BY_KIND = [g for g in TALES_BY_KIND if g[2]]
SPOTS = [dict({"where": "", "tip": "", "media": "", "place": ""}, **s)
         for s in RAW["spots"] if is_published(s) and s.get("island") in ISLANDS_BY_SLUG]
for _s in SPOTS:
    if _s.get("category") not in SPOT_CATEGORIES:
        _s["category"] = "culture"
    if _s.get("fame") not in SPOT_FAME:
        _s["fame"] = "incontournable"
    if _s["place"] not in PLACES_BY_SLUG:
        _s["place"] = ""
INSTITUTIONS = []
for _inst in RAW["institutions"]:
    _inst = dict({"seat": "", "media": "", "refs": [], "scope": "ile"}, **_inst)
    if not is_published(_inst) or (_inst["scope"] == "ile" and _inst.get("island") not in ISLANDS_BY_SLUG):
        continue
    if _inst["scope"] not in INSTITUTION_SCOPES:
        _inst["scope"] = "ile"
    if _inst.get("island") not in ISLANDS_BY_SLUG:
        _inst["island"] = ""
    if _inst.get("category") not in INSTITUTION_CATEGORIES:
        _inst["category"] = "societe"
    if _inst.get("status") not in INSTITUTION_STATUS:
        _inst["status"] = "officiel"
    INSTITUTIONS.append(_inst)
for _island in ISLANDS:
    _island.setdefault("union_member", False)
    for _k in ("spots_lead", "spots_intro", "public_lead", "public_intro"):
        _island.setdefault(_k, "")
    _island.setdefault("spots_tips", [])
    _island["spots_hero"] = _island.get("spots_hero") or _island["hero"]
    _island["public_hero"] = _island.get("public_hero") or _island["hero"]
BIBLIO = {b["id"]: dict({"year": "", "publisher": "", "kind": "exterieur", "category": "", "note": "", "url": ""}, **b)
          for b in RAW["bibliography"] if b.get("id")}
REF_WARNINGS = set()
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


@pass_context
def textlinks_filter(ctx, text):
    """Texte simple (échappé) dans lequel la syntaxe [[chemin|libellé]] devient un lien."""
    return Markup(links_filter(ctx, str(escape(text or ""))))


@pass_context
def refs_of(ctx, item):
    """Références bibliographiques d'un élément (les identifiants inconnus sont ignorés)."""
    out = []
    for rid in (item.get("refs") or []):
        if rid in BIBLIO:
            out.append(BIBLIO[rid])
        else:
            REF_WARNINGS.add(f"{ctx['page_path']} : référence bibliographique inconnue « {rid} »")
    return out


env.globals.update(
    refs_of=refs_of, tale_kinds=TALE_KINDS, tale_kind_singular=TALE_KIND_SINGULAR, tales=TALES, quizzes=QUIZZES,
    featured_tales=[t for t in TALES if t.get("featured")][:4],
    url=url, img_url=img_url, img_srcset=img_srcset, img_abs=img_abs, file_url=file_url,
    commons_page=commons_page, credit_text=credit_text,
    media=MEDIA, settings=SETTINGS, site_url=SITE_URL, contact_email=CONTACT_EMAIL,
    year=datetime.date.today().year, updated=SETTINGS.get("updated_label", ""),
    islands=ISLANDS, islands_by_slug=ISLANDS_BY_SLUG, places=PLACES_BY_SLUG,
    experiences=EXPERIENCES, itineraries=ITINERARIES, practical=PRACTICAL,
    events=EVENTS, videos=VIDEOS, home=HOME, island_labels=MEDIA_LABELS, pg=PG,
    topics=TOPICS, timeline=None, facts=HOME.get("facts", []),
    spot_categories=SPOT_CATEGORIES, spot_fame=SPOT_FAME, institution_categories=INSTITUTION_CATEGORIES,
    institution_status=INSTITUTION_STATUS, institution_scopes=INSTITUTION_SCOPES,
)
env.filters["links"] = links_filter
env.filters["textlinks"] = textlinks_filter
# Choix des filtres (valeur, libellé) pour les pastilles des pages de spots et d'institutions
env.filters["spot_choice"] = lambda key: (key, SPOT_CATEGORIES[key][0])
env.filters["institution_choice"] = lambda key: (key, INSTITUTION_CATEGORIES[key][0])
env.filters["island_choice"] = lambda slug: (slug, ISLANDS_BY_SLUG[slug]["name"])
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
            island["lead"], og_image=island["hero"], section="iles", island=island,
            island_spots=spots_of(island), island_institutions=institutions_of(island))

    # Spots & bons plans, vie publique & institutions : pages d'ensemble et pages par île
    add("iles/bons-plans.html", "spots_hub.html", PG["bonsplans"]["title"], PG["bonsplans"]["description"],
        og_image=PG["bonsplans"]["hero"], section="iles",
        spot_islands=[(i, spots_of(i)) for i in ISLANDS if spots_of(i)])
    add("iles/vie-publique.html", "public_hub.html", PG["viepublique"]["title"], PG["viepublique"]["description"],
        og_image=PG["viepublique"]["hero"], section="iles",
        union_groups=institution_groups([x for x in INSTITUTIONS if x["scope"] == "union"]),
        archipel_groups=institution_groups([x for x in INSTITUTIONS if x["scope"] == "archipel"]),
        island_blocks=[(i, institution_groups([x for x in INSTITUTIONS if x["scope"] == "ile" and x["island"] == i["slug"]]))
                       for i in ISLANDS],
        page_refs=refs_ids(INSTITUTIONS))
    for island in ISLANDS:
        own = spots_of(island)
        add(f"iles/{island['slug']}/bons-plans.html", "island_spots.html", f"Spots & bons plans — {island['name']}",
            island["spots_lead"] or island["lead"], og_image=island["spots_hero"], section="iles", island=island,
            groups=spot_groups(own), spot_count=len(own))
        own_inst = [x for x in INSTITUTIONS if x["scope"] == "ile" and x["island"] == island["slug"]]
        union = [x for x in INSTITUTIONS if x["scope"] == "union"] if island["union_member"] else []
        archipel = [x for x in INSTITUTIONS if x["scope"] == "archipel"]
        add(f"iles/{island['slug']}/vie-publique.html", "island_public.html",
            f"Vie publique & institutions — {island['name']}", island["public_lead"] or island["lead"],
            og_image=island["public_hero"], section="iles", island=island,
            groups=institution_groups(own_inst), union_groups=institution_groups(union),
            archipel_groups=institution_groups(archipel), page_refs=refs_ids(own_inst + union + archipel))
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
        og_image=PG["galerie"]["hero"], section="loisirs", gallery_keys=gallery_keys)
    add("videos.html", "videos.html", PG["videos"]["title"], PG["videos"]["description"],
        og_image=PG["videos"]["hero"], section="loisirs")
    add("glossaire.html", "glossaire.html", PG["glossaire"]["title"], PG["glossaire"]["description"],
        section="loisirs", glossary=GLOSSARY,
        glossary_letters=sorted({slugify(g["term"])[0].upper() for g in GLOSSARY}))

    # Hale halele : contes et récits
    add("contes/index.html", "tales_index.html", PG["contes"]["title"], PG["contes"]["description"],
        og_image=PG["contes"]["hero"], section="contes", groups=TALES_BY_KIND)
    for idx, tale in enumerate(TALES):
        add(f"contes/{tale['slug']}.html", "tale.html", tale["name"], tale["lead"], og_image=tale["hero"],
            section="contes", tale=tale,
            prev_tale=TALES[idx - 1] if idx > 0 else None,
            next_tale=TALES[idx + 1] if idx + 1 < len(TALES) else None)

    # Loisirs : quiz
    add("loisirs/index.html", "loisirs.html", PG["loisirs"]["title"], PG["loisirs"]["description"],
        og_image=PG["loisirs"]["hero"], section="loisirs")
    for idx, q in enumerate(QUIZZES):
        add(f"loisirs/{q['slug']}.html", "quiz.html", f"Quiz : {q['name']}", q["lead"], og_image=q["hero"],
            section="loisirs", quiz=q, next_quiz=QUIZZES[(idx + 1) % len(QUIZZES)] if len(QUIZZES) > 1 else None)
    # Ancienne adresse du quiz : page de redirection (hors plan du site)
    add("quiz.html", "redirect.html", "Quiz", PG["loisirs"]["description"], target="loisirs/index.html")

    # Bibliographie
    add("bibliographie.html", "bibliography.html", PG["bibliographie"]["title"], PG["bibliographie"]["description"],
        section="histoire", biblio_groups=biblio_groups())

    # Pages annexes
    add("credits.html", "credits.html", PG["credits"]["title"], PG["credits"]["description"])
    add("mentions-legales.html", "legal.html", PG["mentions"]["title"], PG["mentions"]["description"])
    add("contact.html", "contact.html", PG["contact"]["title"], PG["contact"]["description"])
    add("plan-du-site.html", "plan.html", PG["plan"]["title"], PG["plan"]["description"],
        sitemap_groups=sitemap_groups())
    add("404.html", "404.html", "Page introuvable", PG["404"]["description"], absolute_urls=True)


def spots_of(island):
    return [s for s in SPOTS if s["island"] == island["slug"]]


def institutions_of(island):
    """Institutions affichées pour une île : les siennes, celles de l'Union (si elle en fait partie) et de l'archipel."""
    return [x for x in INSTITUTIONS
            if (x["scope"] == "ile" and x["island"] == island["slug"])
            or (x["scope"] == "union" and island["union_member"]) or x["scope"] == "archipel"]


def spot_groups(items):
    return [dict(key=k, label=label, icon=icon, entries=[s for s in items if s["category"] == k])
            for k, (label, icon) in SPOT_CATEGORIES.items() if any(s["category"] == k for s in items)]


def institution_groups(items):
    return [dict(key=k, label=label, icon=icon, entries=[x for x in items if x["category"] == k])
            for k, (label, icon) in INSTITUTION_CATEGORIES.items() if any(x["category"] == k for x in items)]


def refs_ids(items):
    """Identifiants bibliographiques cités par une liste d'éléments, sans doublon et dans l'ordre."""
    return list(dict.fromkeys(rid for x in items for rid in (x.get("refs") or [])))


def biblio_groups():
    """Références groupées par catégorie, avec le nombre de pages qui les citent."""
    cited = {}
    for t in TOPICS:
        for pg in t["pages"]:
            for rid in pg.get("refs") or []:
                cited.setdefault(rid, []).append((pg["name"], f"{t['slug']}/{pg['slug']}.html"))
    for tale in TALES:
        for rid in tale.get("refs") or []:
            cited.setdefault(rid, []).append((tale["name"], f"contes/{tale['slug']}.html"))
    for inst in INSTITUTIONS:
        page = (f"iles/{inst['island']}/vie-publique.html" if inst["scope"] == "ile" else "iles/vie-publique.html")
        for rid in inst.get("refs") or []:
            entry = (PG["viepublique"]["title"] if inst["scope"] != "ile"
                     else f"{PG['viepublique']['title']} — {ISLANDS_BY_SLUG[inst['island']]['name']}", page)
            if entry not in cited.setdefault(rid, []):
                cited[rid].append(entry)
    groups = []
    known = list(BIBLIO_CATEGORIES)
    for cat in known + sorted({b.get("category") for b in BIBLIO.values()} - set(known)):
        items = [dict(b, cited=cited.get(b["id"], [])) for b in BIBLIO.values() if b.get("category") == cat]
        if items:
            groups.append(dict(key=cat, title=BIBLIO_CATEGORIES.get(cat, cat or "Autres"), entries=items))
    return groups


def sitemap_groups():
    groups = [
        dict(title="Les îles", links=[(PG["iles"]["title"], "iles/index.html")]
             + [(i["name"], f"iles/{i['slug']}.html") for i in ISLANDS]),
        dict(title=PG["bonsplans"]["title"], links=[("Les quatre îles", "iles/bons-plans.html")]
             + [(i["name"], f"iles/{i['slug']}/bons-plans.html") for i in ISLANDS]),
        dict(title=PG["viepublique"]["title"], links=[("Les quatre îles", "iles/vie-publique.html")]
             + [(i["name"], f"iles/{i['slug']}/vie-publique.html") for i in ISLANDS]),
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
        dict(title=PG["contes"]["title"], links=[("Tous les récits", "contes/index.html")]
             + [(t["name"], f"contes/{t['slug']}.html") for t in TALES]),
        dict(title=PG["loisirs"]["title"], links=[("Tous les quiz", "loisirs/index.html")]
             + [(q["name"], f"loisirs/{q['slug']}.html") for q in QUIZZES]
             + [("Glossaire", "glossaire.html"), ("Galerie photos", "galerie.html"), ("Vidéos", "videos.html")]),
        dict(title=SETTINGS.get("site_name", "Komori"), links=[
            ("Sources & bibliographie", "bibliographie.html"), ("Contact", "contact.html"),
            ("Crédits", "credits.html"), ("Mentions légales", "mentions-legales.html")]),
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
    if kind == "contes":
        return [dict(label="Tous les récits", note=None, href="contes/index.html")] + [
            dict(label=label, note=f"{len(items)} récit{'s' if len(items) > 1 else ''}", href=f"contes/index.html#{key}")
            for key, label, items in TALES_BY_KIND]
    if kind == "loisirs":
        return [dict(label="Tous les quiz", note=None, href="loisirs/index.html")] + [
            dict(label=q["name"], note=f"Quiz · {q.get('level') or ''}".rstrip(" ·"), href=f"loisirs/{q['slug']}.html")
            for q in QUIZZES]
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
    if first == "loisirs" or link in ("galerie.html", "videos.html", "glossaire.html", "quiz.html"):
        return "loisirs"
    if link == "bibliographie.html":
        return "histoire"
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


# --------------------------------------------------------------------------- Menu tiroir (toutes les pages)

def island_branch(island):
    slug = island["slug"]
    return ([dict(label="Présentation", href=f"iles/{slug}.html"),
             dict(label=PG["bonsplans"]["title"], href=f"iles/{slug}/bons-plans.html"),
             dict(label=PG["viepublique"]["title"], href=f"iles/{slug}/vie-publique.html")]
            + [dict(label=PLACES_BY_SLUG[s]["name"], note="Lieu", href=f"lieux/{s}.html") for s in island["places"]])


def deep_children(kind):
    """Branches du tiroir : comme les sous-menus automatiques, mais sur plusieurs niveaux."""
    if kind == "iles":
        return [dict(label=PG["iles"]["title"], href="iles/index.html")] + [
            dict(label=i["name"], href=f"iles/{i['slug']}.html", children=island_branch(i)) for i in ISLANDS]
    if kind == "contes":
        return [dict(label="Tous les récits", href="contes/index.html")] + [
            dict(label=label, href=f"contes/index.html#{key}",
                 children=[dict(label=t["name"], href=f"contes/{t['slug']}.html") for t in items])
            for key, label, items in TALES_BY_KIND]
    return [dict(label=c["label"], href=c["href"]) for c in auto_children(kind)]


def link_children(href):
    """Pages filles d'une page d'ensemble ajoutée à la main dans le menu."""
    lists = {
        "experiences/index.html": [(e["name"], f"experiences/{e['slug']}.html") for e in EXPERIENCES],
        "itineraires/index.html": [(i["name"], f"itineraires/{i['slug']}.html") for i in ITINERARIES],
        "preparer-son-voyage/index.html": [(p["name"], f"preparer-son-voyage/{p['slug']}.html") for p in PRACTICAL],
        "iles/bons-plans.html": [(i["name"], f"iles/{i['slug']}/bons-plans.html") for i in ISLANDS],
        "iles/vie-publique.html": [(i["name"], f"iles/{i['slug']}/vie-publique.html") for i in ISLANDS],
    }
    return [dict(label=label, href=h) for label, h in lists.get(href, [])] or None


def drawer_tree():
    """Arborescence complète du site pour le menu tiroir, dans l'ordre du menu principal."""
    counter = itertools.count(1)

    def finish(node):
        children = [finish(c) for c in node.get("children") or [] if link_ok(c.get("href"))]
        own = node["href"].split("#", 1)[0] if node.get("href") else None
        paths = {own} if own else set()
        for c in children:
            paths |= c["paths"]
        # La page courante n'est signalée qu'une fois : pas sur un parent dont un enfant mène à la même page
        current = bool(own) and "#" not in node["href"] and not any(c.get("href") == node["href"] for c in children)
        return dict(label=node["label"], href=node.get("href"), note=node.get("note"), children=children or None,
                    paths=paths, own=own if current else None, id=next(counter))

    roots = [dict(label="Accueil", href="index.html")]
    for item in NAVIGATION["menu"]:
        if not link_ok(item.get("link")):
            continue
        children = deep_children(item.get("auto_children") or "")
        seen = {c["href"] for c in children}
        for c in item.get("children", []):
            if link_ok(c.get("link")) and c["link"] not in seen:
                children.append(dict(label=c["label"], href=c["link"], children=link_children(c["link"])))
                seen.add(c["link"])
        roots.append(dict(label=item["label"], href=item["link"], children=children))
    nodes = [finish(n) for n in roots]
    present = set().union(*(n["paths"] for n in nodes))
    extra = []
    for col in NAVIGATION.get("footer", []):
        for link in col["links"]:
            href = link.get("link")
            if link_ok(href) and href.split("#", 1)[0] not in present and all(e["href"] != href for e in extra):
                extra.append(dict(label=link["label"], href=href))
    if extra:
        nodes.append(finish(dict(label="À propos", href=None, children=extra)))
    return nodes


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
    unique(RAW["tales"], "Contes et récits")
    unique(RAW["quizzes"], "Quiz")
    unique(RAW["spots"], "Spots & bons plans")
    unique(RAW["institutions"], "Institutions")
    for i in RAW["islands"]:
        if i.get("slug") in RESERVED_ISLAND_SLUGS:
            errors.append(f"Île : l'adresse « {i['slug']} » est réservée par le site")
    for s in RAW["spots"]:
        if is_published(s) and s.get("island") not in ISLANDS_BY_SLUG:
            errors.append(f"spot {s.get('slug')} : île inconnue ou masquée « {s.get('island')} »")
    for s in SPOTS:
        need_media(s["media"], f"spot {s['slug']}")
    for x in INSTITUTIONS:
        need_media(x["media"], f"institution {x['slug']}")
    ids = [b.get("id") for b in RAW["bibliography"]]
    for rid in {i for i in ids if ids.count(i) > 1}:
        errors.append(f"Bibliographie : l'identifiant « {rid} » est utilisé deux fois")
    for tale in TALES:
        need_media(tale.get("hero"), f"récit {tale['slug']}")
        if not tale.get("hero"):
            errors.append(f"récit {tale['slug']} : image manquante")
    for q in QUIZZES:
        need_media(q.get("hero"), f"quiz {q['slug']}")
        if not q.get("questions"):
            errors.append(f"quiz {q['slug']} : aucune question")
        for n, item in enumerate(q.get("questions", []), 1):
            if len(item.get("choices", [])) < 2:
                errors.append(f"quiz {q['slug']}, question {n} : il faut au moins deux réponses")
            elif not 0 <= item.get("answer", -1) < len(item["choices"]):
                errors.append(f"quiz {q['slug']}, question {n} : la bonne réponse n'existe pas")
    for t in RAW["topics"]:
        unique(t.get("pages", []), f"Rubrique {t.get('slug')}")
        if t.get("slug") in RESERVED_SLUGS:
            errors.append(f"Rubrique : l'adresse « {t['slug']} » est réservée par le site")

    for i in ISLANDS:
        for k in [i["hero"], i["card"], i["spots_hero"], i["public_hero"], *i.get("gallery", []),
                  *(t.get("media") for t in i["themes"])]:
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
    env.globals.update(nav=menu, nav_cta=cta, footer=footer, url_ok=link_ok, drawer=drawer_tree())

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
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for path, template, ctx in PAGES:
        html = env.get_template(template).render(page_path=path, **ctx)
        target = OUT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")

    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}/{path}</loc><lastmod>{today}</lastmod></url>"
        for path, template, _ in PAGES if path != "404.html" and template != "redirect.html"
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
    for warning in sorted(LINK_WARNINGS | REF_WARNINGS):
        print("Avertissement :", warning, file=sys.stderr)
    print(f"{len(PAGES)} pages générées dans {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
