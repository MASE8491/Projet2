# Komori — komori.com

Guide de voyage des quatre îles de l'archipel des Comores : **Grande Comore (Ngazidja)**,
**Mohéli (Mwali)**, **Anjouan (Ndzuwani)** et **Mayotte (Maore)**.

Le site suit l'organisation classique d'un portail de tourisme national
(destinations, expériences, itinéraires, médiathèque, préparer son voyage). Les
textes sont originaux et le design est propre au site.

## Contenu (52 pages)

| Rubrique | Pages |
| --- | --- |
| Accueil | `index.html` |
| Destinations | index avec carte interactive, 4 pages îles, « Découvrir l'archipel » |
| Lieux | 14 fiches (Moroni, Karthala, Nord de la Grande Comore, parc de Mohéli, Itsamia, forêts de Mohéli, Mutsamudu, Domoni, lac Dzialandzé, lagon de Mayotte, Petite-Terre, N'Gouja, mont Choungui, Mamoudzou & Tsingoni) |
| Expériences | index + 7 thèmes (nature, plages, plongée, randonnées, culture, gastronomie, route des parfums) |
| Itinéraires | index + 5 routes (5 à 16 jours) |
| Préparer son voyage | index + 8 pages (venir, formalités, saisons, transports, santé, budget, hébergement, savoir-vivre) |
| Médias | galerie filtrable par île, page vidéos |
| Divers | agenda, contact, crédits, mentions légales, plan du site, 404 |

## Photos et vidéos

Tous les médias viennent de **Wikimedia Commons** (licences libres ou domaine
public) et sont chargés depuis Commons via `Special:FilePath`. La liste, avec
auteurs et licences, est dans `site_src/media.py` et sur la page `credits.html`.

- Si une image ne répond pas, un aplat aux couleurs du site affiche sa légende.
- Les vidéos sont des vidéos d'illustration (baleines, tortues, récifs) au format WebM.
- Pour la production, il est conseillé de télécharger les médias et de les héberger
  avec le site, en conservant les mentions d'auteur et de licence.

## Structure

```
build.py                 générateur statique (Jinja2)
site_src/
  media.py               médiathèque (fichiers Commons, légendes, crédits)
  content_*.py           textes : îles, lieux, expériences, itinéraires, infos pratiques, agenda
  templates/             gabarits HTML
  static/                CSS, JS, favicon
docs/                    site généré (prêt pour GitHub Pages, CNAME = komori.com)
```

## Générer le site

```bash
pip install -r requirements.txt
python3 build.py          # régénère docs/ et vérifie les liens internes
python3 -m http.server -d docs 8000
```

Pour publier sur GitHub Pages : *Settings → Pages → Branch : main, dossier `/docs`*,
puis faire pointer le DNS de komori.com vers GitHub Pages.

Les informations pratiques (visas, santé, transports) sont indicatives et datées
d'octobre 2026 : elles doivent être revérifiées régulièrement.
