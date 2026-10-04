# Komori

Site de découverte des quatre îles de l'archipel des Comores : **Grande Comore (Ngazidja)**,
**Mohéli (Mwali)**, **Anjouan (Ndzuwani)** et **Mayotte (Maore)**. Géographie, histoire documentée
et sourcée, culture, contes et légendes (**Hale halele**), quiz (**Loisirs**) et un volet tourisme
pour préparer son voyage.

Les textes sont originaux et le design est propre au site. Tout le contenu est administrable
depuis un **back-office** intégré, sans connaissances techniques.

## Administration du site (back-office)

Adresse : **`/admin/`** du site publié, par exemple https://mase8491.github.io/Projet2/admin/

### Ce que permet l'administration

- **Arborescence** : voir toutes les pages, les modifier, les réordonner (↑ ↓), rattacher un lieu,
  un spot ou une institution à une autre île ou un article à une autre rubrique, changer l'adresse
  d'une page, la masquer, la supprimer, ou ajouter îles, lieux, spots, institutions, rubriques,
  articles, expériences, itinéraires et infos pratiques.
- **Éditeur de page** : tous les champs (titre, chapeau, sections, encadrés, galerie…) avec un
  éditeur de texte simple (gras, listes, liens vers les pages du site, encadré « Bon à savoir »)
  et un **aperçu** avant enregistrement.
- **Médiathèque** : téléverser une image depuis l'ordinateur (réduite automatiquement pour le web),
  ajouter un média de Wikimedia Commons, modifier légendes et crédits, voir où une image est
  utilisée, la remplacer partout.
- **Hale halele** : contes et récits (genre, île, lieu associé, encadré « Ce que l'on en sait »,
  références, mise en avant sur l'accueil).
- **Loisirs** : quiz (questions, réponses, explications, lien « en savoir plus »).
- **Spots & bons plans** (sous chaque île) : marchés, artisans, plages, sites connus ou méconnus,
  avec catégorie, notoriété (incontournable / secret local), bon plan pratique, image et lieu associé.
- **Vie publique & institutions** (sous chaque île) : institutions officielles, autorités coutumières
  ou religieuses et associations, avec domaine, statut, portée (île, Union des Comores, tout
  l'archipel) et sources.
- **Bibliographie** : références citées dans les articles d'histoire et les contes, classées en
  « voix de l'archipel » et « regards extérieurs ».
- **Menu et pied de page**, **page d'accueil**, **pages fixes** (contact, mentions légales…),
  **frise**, **agenda**, **glossaire**, **vidéos** et **réglages** du site.
- **Publication** en un clic, **historique** des versions et **restauration** d'une version précédente.

### Garde-fous

- **Chaque modification** (enregistrement, déplacement, masquage, changement d'adresse,
  suppression, ajout d'image, modification du menu, publication, restauration) ouvre d'abord une
  **fenêtre d'impact**. Elle indique les pages touchées, les liens mis à jour automatiquement, les
  menus concernés et le niveau de risque (faible, important, risqué).
- Les actions risquées demandent de **cocher une case** ou de **recopier un mot** (SUPPRIMER,
  RESTAURER, ANNULER, CONFIRMER).
- Certaines actions sont **bloquées** quand elles casseraient le site. Par exemple, supprimer
  une île qui contient encore des lieux, des spots ou des institutions, ou une image encore utilisée.
- Les nouvelles pages sont créées **masquées**. Les modifications restent en **brouillon**
  (enregistré dans le navigateur) jusqu'à la publication.
- Avant publication, une **vérification** bloque les erreurs : image manquante, adresse en double,
  adresse réservée, bonne réponse de quiz inexistante, référence bibliographique citée mais supprimée.
  Elle signale aussi les liens vers des pages masquées.
- Si le contenu a été modifié ailleurs en même temps, la publication est **refusée** plutôt que
  d'écraser ce travail.

### Mise en route (une seule fois)

1. **GitHub Pages** : *Settings → Pages → Deploy from a branch → `main` / `/docs`*. Le dépôt
   doit être public, sauf offre payante.
2. **Génération automatique** : le workflow `.github/workflows/build-site.yml` régénère `docs/`
   à chaque publication. Si la génération échoue avec une erreur de droits, ouvrez
   *Settings → Actions → General → Workflow permissions* et choisissez **Read and write permissions**.
3. **Jeton d'accès** de l'administrateur : https://github.com/settings/personal-access-tokens/new
   - *Repository access* : seulement ce dépôt ;
   - *Permissions* : **Contents : Read and write**, **Actions : Read-only** ;
   - collez le jeton dans l'écran de connexion de `/admin/`. Ne le partagez jamais. Vous pouvez
     le révoquer à tout moment depuis GitHub.

### Fonctionnement

L'administration est une application web statique, publiée avec le site, sans serveur. Elle lit
et écrit les fichiers `content/*.json` via l'API GitHub, avec le jeton de l'administrateur. Chaque
publication crée un commit sur `main`. GitHub Actions lance alors `build.py`, qui régénère `docs/`,
puis GitHub Pages met le site à jour (1 à 3 minutes). Les images téléversées sont stockées dans
`site_src/static/uploads/`.

## Contenu (139 pages)

| Rubrique | Pages |
| --- | --- |
| Accueil | îles, thèmes, contes du soir, frise, « Le saviez-vous ? », itinéraires, médiathèque |
| Les îles | tableau comparatif + carte, 4 pages îles par thème, chacune avec ses pages « Spots & bons plans » et « Vie publique & institutions », et deux pages d'ensemble filtrables (56 spots, 39 institutions) |
| Lieux | 16 fiches |
| Géographie | volcans, climat, océan et lagons, faune et flore, population |
| Histoire | 11 articles sourcés (sources et méthodes, peuplement, islam, sultans, escales et pirates, traite et esclavage, colonisation, indépendance, Comores depuis 1975, Mayotte : regards croisés, portraits), frise de 51 dates, bibliographie de 67 références |
| Culture & folklore | langues, musique, contes et légendes, coutumes, artisanat, cuisine, fêtes, littérature |
| Hale halele | 38 contes, mythes, légendes et récits des quatre îles (dont 10 de Mohéli), avec leurs sources et leurs variantes |
| Loisirs | 6 quiz (réponses mélangées à chaque partie), glossaire, galerie, vidéos |
| Voyager | expériences, itinéraires, infos pratiques, agenda |

### Navigation

Le bouton **Menu**, en haut à gauche de chaque page, ouvre un **tiroir vertical** qui donne accès à
toutes les pages du site : menus et sous-menus dépliables (îles et leurs pages, lieux, articles,
contes par genre, quiz, expériences…), page courante mise en évidence et recherche par titre. Il est
généré à partir du menu principal (« Menu et pied de page » dans l'administration) et du contenu.
Sur grand écran, le menu horizontal reste disponible.

### Méthode pour l'histoire et les contes

Les articles d'histoire croisent les sources de l'archipel (chroniques en caractères arabes,
traditions orales, historiens comoriens) et les regards extérieurs (voyageurs, archives, historiens,
archéologues, généticiens). Les points débattus et sensibles (islamisation, esclavage, statut de
Mayotte) présentent les différents points de vue. Les contes sont des réécritures originales, pas
des traductions ; chacun indique ce que l'on sait de son origine et des ouvrages pour aller plus loin.
Les pages « Vie publique » distinguent institutions officielles, autorités coutumières ou religieuses
et associations, et décrivent des fonctions plutôt que des personnes en poste. Les bons plans
privilégient les lieux durables (marchés, ateliers, sites) plutôt que les enseignes commerciales.

## Structure

```
content/*.json              tout le contenu éditorial (modifié par l'administration)
site_src/templates/         gabarits HTML (Jinja2)
site_src/static/            CSS, JS, favicon, images téléversées (uploads/)
site_src/admin/             application d'administration
build.py                    générateur statique + vérifications
.github/workflows/          régénération automatique du site
docs/                       site généré (publié par GitHub Pages)
```

## Générer le site à la main

```bash
pip install -r requirements.txt
python3 build.py          # régénère docs/ et vérifie les liens internes
python3 -m http.server -d docs 8000
```

## Médias et domaine

Les médias proviennent de Wikimedia Commons (licences libres) ou sont téléversés par
l'administrateur, avec légende, auteur et licence. Ils sont listés sur la page des crédits.

Le domaine komori.com appartient à une autre organisation (Komori Corporation). Pour utiliser un
domaine qui vous appartient, renseignez-le dans *Réglages → Nom de domaine personnel* puis
configurez son DNS vers GitHub Pages.
