# Komori — komori.com

Site de découverte des quatre îles de l'archipel des Comores : **Grande Comore (Ngazidja)**,
**Mohéli (Mwali)**, **Anjouan (Ndzuwani)** et **Mayotte (Maore)**. Géographie, histoire,
culture et folklore, et un volet tourisme pour préparer son voyage.

Les textes sont originaux et le design est propre au site.

## Contenu (76 pages)

| Rubrique | Pages |
| --- | --- |
| Accueil | îles, thèmes, frise, « Le saviez-vous ? », itinéraires, médiathèque |
| Les îles | tableau comparatif + carte, 4 pages îles par thème (géographie, histoire, culture, nature, à voir) |
| Lieux | 16 fiches (Moroni, Karthala, Iconi, Ntsaoueni, Mutsamudu, Domoni, lagon de Mayotte, Tsingoni…) |
| Géographie | volcans et reliefs, climat et saisons, océan et lagons, faune et flore, population et territoires |
| Histoire | premiers peuplements, temps des sultans, période coloniale, indépendance, grandes figures, frise chronologique |
| Culture & folklore | langues, musique et danses, contes et légendes, coutumes et grand mariage, artisanat et costumes, cuisine, fêtes et religion, littérature et arts |
| Voyager | hub, 6 expériences, 5 itinéraires, 8 pages pratiques, agenda |
| Médiathèque | galerie filtrable, vidéos, glossaire (recherche), quiz interactif |
| Divers | contact, crédits, mentions légales, plan du site, 404 |

## Photos et vidéos

Tous les médias viennent de **Wikimedia Commons** (licences libres ou domaine public) et sont
chargés depuis Commons via `Special:FilePath`. La liste, avec auteurs et licences, est dans
`site_src/media.py` et sur la page `credits.html`. Si une image ne répond pas, un aplat aux
couleurs du site affiche sa légende. Pour la production, il est conseillé d'héberger les médias
avec le site en conservant les mentions d'auteur et de licence.

## Structure

```
build.py                    générateur statique (Jinja2) + vérification des liens
site_src/
  media.py                  médiathèque (fichiers Commons, légendes, crédits)
  content_islands.py        les 4 îles, par thème
  content_places.py         fiches des lieux
  content_geographie.py     rubrique Géographie
  content_histoire.py       rubrique Histoire + frise chronologique
  content_culture.py        rubrique Culture & folklore
  content_extras.py         glossaire, quiz, « Le saviez-vous ? »
  content_experiences.py    expériences
  content_itineraries.py    itinéraires
  content_practical.py      préparer son voyage
  content_misc.py           accueil, agenda, vidéos
  templates/                gabarits HTML
  static/                   CSS, JS, favicon
docs/                       site généré (GitHub Pages, CNAME = komori.com)
```

## Générer le site

```bash
pip install -r requirements.txt
python3 build.py          # régénère docs/ et vérifie les liens internes
python3 -m http.server -d docs 8000
```

Pour publier : *Settings → Pages → Branch : main, dossier `/docs`* (dépôt public ou offre
payante requise), puis faire pointer le DNS de komori.com vers GitHub Pages.

Les informations pratiques (visas, santé, transports) sont indicatives et datées d'octobre 2026.
