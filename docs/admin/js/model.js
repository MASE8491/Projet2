// Modèle du contenu : types de pages, schémas des formulaires, adresses, références et impacts.
// Toutes les fonctions travaillent sur `data` : { nomDuFichier: contenuJSON }.

export const ICONS = {
  leaf: "Feuille", sun: "Soleil", wave: "Vague", mountain: "Montagne", dome: "Coupole", bowl: "Bol",
  flower: "Fleur", plane: "Avion", passport: "Passeport", calendar: "Calendrier", boat: "Bateau",
  health: "Santé", coin: "Pièce", bed: "Lit", chat: "Bulle", pin: "Repère", clock: "Horloge",
  globe: "Globe", scroll: "Parchemin", drum: "Tambour", people: "Personnes", flag: "Drapeau",
  star: "Étoile", moon: "Lune", rings: "Alliances", needle: "Aiguille", book: "Livre",
  compass: "Boussole", question: "Question", list: "Liste",
};

export const TALE_KINDS = { mythe: "Mythe des origines", legende: "Légende de lieu", recit: "Récit d'hier et d'aujourd'hui", conte: "Conte du soir" };
export const QUIZ_LEVELS = { Facile: "Facile", Moyen: "Moyen", Difficile: "Difficile" };
export const BIBLIO_KINDS = { comorien: "Voix de l'archipel (source ou auteur comorien)", exterieur: "Regard extérieur" };
export const BIBLIO_CATEGORIES = {
  chronique: "Chroniques et manuscrits", tradition: "Traditions orales et littérature", histoire: "Études historiques",
  anthropologie: "Anthropologie et société", archeologie: "Archéologie et sciences", temoins: "Voyageurs et témoins",
  contes: "Recueils de contes", documents: "Textes officiels et rapports",
};

export const SPOT_CATEGORIES = {
  marche: "Marchés & commerces", artisanat: "Artisanat & savoir-faire", saveurs: "Saveurs & tables",
  plage: "Plages & îlots", nature: "Nature & randonnée", patrimoine: "Patrimoine & histoire", culture: "Culture & sorties",
};
export const SPOT_FAME = { incontournable: "Incontournable (lieu connu)", meconnu: "Secret local (lieu méconnu)" };
export const INSTITUTION_CATEGORIES = {
  politique: "Pouvoirs publics", justice: "Justice", religion: "Autorités religieuses", coutume: "Coutume & notabilité",
  environnement: "Environnement", culture: "Savoir, culture & médias", sport: "Sport", societe: "Associations & société civile",
};
export const INSTITUTION_STATUS = {
  officiel: "Institution officielle", coutume: "Autorité coutumière ou religieuse (non officielle)", associatif: "Association",
};
export const INSTITUTION_SCOPES = {
  ile: "Propre à l'île (page « Vie publique » de l'île)",
  union: "Union des Comores (affichée pour Grande Comore, Anjouan et Mohéli)",
  archipel: "Tout l'archipel (affichée pour les quatre îles)",
};
/** Pages d'une île générées automatiquement à partir de ses spots et de ses institutions. */
export const islandSubPaths = (slug) => [`iles/${slug}/bons-plans.html`, `iles/${slug}/vie-publique.html`];

const iconField = { key: "icon", label: "Icône", type: "icon" };
const refsField = { key: "refs", label: "Références bibliographiques", type: "reflist", ref: "source",
  help: "Ouvrages cités en bas de la page. Pour en ajouter un nouveau, complétez d'abord la liste « Bibliographie »." };
const heroField = { key: "hero", label: "Image principale (bandeau)", type: "media", required: true,
  help: "Grande image affichée en haut de la page." };
const cardField = { key: "card", label: "Image de vignette", type: "media", required: true,
  help: "Petite image utilisée dans les listes et les cartes qui mènent à cette page." };
const leadField = { key: "lead", label: "Chapeau (résumé)", type: "textarea", required: true,
  help: "Une ou deux phrases sous le titre. Elles servent aussi de résumé dans les listes et pour les moteurs de recherche." };
const sectionsField = { key: "sections", label: "Sections de la page", type: "list", itemLabel: "title",
  addLabel: "Ajouter une section", help: "Chaque section a un titre, une image facultative et un texte.",
  fields: [
    { key: "title", label: "Titre de la section", type: "text", required: true },
    { key: "media", label: "Image de la section (facultative)", type: "media", optional: true },
    { key: "html", label: "Texte", type: "richtext" },
  ] };
const factsField = { key: "facts", label: "Encadré « En bref »", type: "list", itemLabel: "label",
  addLabel: "Ajouter une ligne", fields: [
    { key: "label", label: "Intitulé", type: "text" },
    { key: "value", label: "Valeur", type: "text" },
  ] };
const galleryField = { key: "gallery", label: "Galerie d'images", type: "medialist",
  help: "Images affichées dans la galerie en bas de la page." };

// ------------------------------------------------------------------ Types de pages (collections)

export const TYPES = {
  island: {
    label: "Île", plural: "Îles", file: "islands", emoji: "🏝️",
    path: (e) => `iles/${e.slug}.html`,
    fields: [
      { key: "name", label: "Nom de l'île", type: "text", required: true },
      { key: "local", label: "Nom en comorien", type: "text" },
      { key: "tagline", label: "Surnom", type: "text" },
      { key: "status", label: "Statut", type: "text" },
      { key: "chef_lieu", label: "Chef-lieu", type: "text" },
      { key: "area", label: "Superficie", type: "text" },
      { key: "summit", label: "Point culminant", type: "text" },
      { key: "language", label: "Langue", type: "text" },
      { key: "accent", label: "Couleur de l'île", type: "color" },
      heroField, cardField, leadField,
      { key: "intro", label: "Introduction", type: "richtext" },
      { key: "themes", label: "Thèmes (géographie, histoire, culture…)", type: "list", itemLabel: "title",
        addLabel: "Ajouter un thème", fields: [
          { key: "key", label: "Ancre (identifiant court, sans espace)", type: "text", help: "Exemple : histoire. Sert au sommaire de la page." },
          { key: "title", label: "Titre", type: "text", required: true },
          { key: "media", label: "Image", type: "media" },
          { key: "html", label: "Texte", type: "richtext" },
        ] },
      { key: "places", label: "Ordre des lieux de l'île", type: "reflist", ref: "place", sameIsland: true,
        help: "Pour rattacher un lieu à une autre île, utilisez « Déplacer » dans l'arborescence." },
      galleryField,
      { key: "tips", label: "Conseils pour le voyageur", type: "stringlist", addLabel: "Ajouter un conseil" },
      { key: "map", label: "Centre de la carte", type: "coords", zoom: true },
      { key: "union_member", label: "Cette île fait partie de l'Union des Comores", type: "checkbox",
        help: "Sa page « Vie publique » affiche alors aussi les institutions communes à l'Union." },
      { key: "spots_hero", label: "Page « Spots & bons plans » : image du bandeau", type: "media", optional: true,
        help: "Les spots eux-mêmes se gèrent dans l'arborescence, sous l'île (⭐ Spots & bons plans)." },
      { key: "spots_lead", label: "Page « Spots & bons plans » : chapeau", type: "textarea" },
      { key: "spots_intro", label: "Page « Spots & bons plans » : introduction", type: "richtext" },
      { key: "spots_tips", label: "Page « Spots & bons plans » : bons plans pratiques", type: "stringlist", addLabel: "Ajouter un bon plan" },
      { key: "public_hero", label: "Page « Vie publique » : image du bandeau", type: "media", optional: true,
        help: "Les institutions elles-mêmes se gèrent dans l'arborescence, sous l'île (🏛️ Vie publique)." },
      { key: "public_lead", label: "Page « Vie publique » : chapeau", type: "textarea" },
      { key: "public_intro", label: "Page « Vie publique » : introduction", type: "richtext" },
    ],
  },
  place: {
    label: "Lieu", plural: "Lieux", file: "places", emoji: "📍", parentType: "island", parentKey: "island",
    path: (e) => `lieux/${e.slug}.html`,
    fields: [
      { key: "name", label: "Nom du lieu", type: "text", required: true },
      { key: "kicker", label: "Surtitre", type: "text", help: "Exemple : Grande Comore · Volcan" },
      heroField,
      { key: "coords", label: "Position sur la carte", type: "coords" },
      leadField, sectionsField, factsField, galleryField,
    ],
  },
  topic: {
    label: "Rubrique", plural: "Rubriques", file: "topics", emoji: "📚",
    path: (e) => `${e.slug}/index.html`, prefix: (e) => `${e.slug}/`,
    fields: [
      { key: "name", label: "Nom de la rubrique", type: "text", required: true },
      iconField, heroField, cardField, leadField,
      { key: "intro", label: "Introduction", type: "richtext" },
      { ...factsField, label: "Encadré « Repères »" },
      { key: "show_timeline", label: "Afficher la frise chronologique sur cette rubrique", type: "checkbox" },
    ],
  },
  topicpage: {
    label: "Article", plural: "Articles", file: "topics", emoji: "📄", parentType: "topic",
    path: (e, parent) => `${parent.slug}/${e.slug}.html`,
    fields: [
      { key: "name", label: "Titre de l'article", type: "text", required: true },
      { key: "period", label: "Période ou sous-titre (facultatif)", type: "text", help: "Exemple : XVe – XIXe siècle" },
      iconField, heroField, leadField, sectionsField, factsField,
      { key: "didyouknow", label: "Encadré « Le saviez-vous ? »", type: "textarea" },
      galleryField, refsField,
    ],
  },
  experience: {
    label: "Expérience", plural: "Expériences", file: "experiences", emoji: "🌊",
    path: (e) => `experiences/${e.slug}.html`,
    fields: [
      { key: "name", label: "Nom de l'expérience", type: "text", required: true },
      iconField, heroField, cardField, leadField, sectionsField,
      { key: "places", label: "Lieux où la vivre", type: "reflist", ref: "place" },
      galleryField,
    ],
  },
  itinerary: {
    label: "Itinéraire", plural: "Itinéraires", file: "itineraries", emoji: "🧭",
    path: (e) => `itineraires/${e.slug}.html`,
    fields: [
      { key: "name", label: "Nom de l'itinéraire", type: "text", required: true },
      { key: "theme", label: "Thème", type: "text" },
      { key: "duration", label: "Durée", type: "text" },
      { key: "islands", label: "Îles traversées", type: "reflist", ref: "island" },
      heroField, cardField, leadField,
      { key: "days", label: "Étapes", type: "list", itemLabel: "title", addLabel: "Ajouter une étape", fields: [
        { key: "when", label: "Jours", type: "text", help: "Exemple : Jours 1-2" },
        { key: "title", label: "Titre de l'étape", type: "text", required: true },
        { key: "text", label: "Description", type: "textarea" },
        { key: "place", label: "Lieu associé (facultatif)", type: "ref", ref: "place", optional: true },
      ] },
      { key: "tips", label: "Conseil", type: "textarea" },
    ],
  },
  practical: {
    label: "Info pratique", plural: "Infos pratiques", file: "practical", emoji: "🧳",
    path: (e) => `preparer-son-voyage/${e.slug}.html`,
    fields: [
      { key: "name", label: "Titre", type: "text", required: true },
      iconField, heroField,
      { key: "summary", label: "Résumé", type: "textarea", required: true },
      sectionsField,
    ],
  },
};

TYPES.tale = {
  label: "Conte ou récit", plural: "Contes et récits (Hale halele)", file: "tales", emoji: "🌙",
  path: (e) => `contes/${e.slug}.html`,
  fields: [
    { key: "name", label: "Titre du récit", type: "text", required: true },
    { key: "kind", label: "Genre", type: "select", options: TALE_KINDS,
      help: "Détermine la catégorie dans laquelle le récit est rangé sur la page « Hale halele »." },
    { key: "local", label: "Autre nom (facultatif)", type: "text", help: "Nom comorien du lieu ou du récit, par exemple « Niamawi »." },
    { key: "island", label: "Île", type: "ref", ref: "island", optional: true, emptyLabel: "— Tout l'archipel —" },
    { key: "place", label: "Lieu associé (facultatif)", type: "ref", ref: "place", optional: true,
      help: "Une carte vers la page du lieu s'affiche à côté du récit." },
    heroField, leadField,
    { key: "text", label: "Le récit", type: "richtext", required: true,
      help: "Racontez avec vos mots. La formule « Hale ! – Halele ! » est ajoutée automatiquement en tête." },
    { key: "moral", label: "Morale (facultatif)", type: "textarea" },
    { key: "about", label: "Encadré « Ce que l'on en sait »", type: "richtext",
      help: "Variantes, origine du récit, ce qu'en disent historiens ou scientifiques." },
    { ...refsField, label: "Pour aller plus loin (références)" },
    { key: "featured", label: "Mettre en avant sur la page d'accueil (4 récits au maximum)", type: "checkbox" },
  ],
};

TYPES.quiz = {
  label: "Quiz", plural: "Quiz (Loisirs)", file: "quizzes", emoji: "❓",
  path: (e) => `loisirs/${e.slug}.html`,
  fields: [
    { key: "name", label: "Titre du quiz", type: "text", required: true },
    iconField,
    { key: "hero", label: "Image de vignette", type: "media", required: true },
    { key: "level", label: "Niveau", type: "select", options: QUIZ_LEVELS },
    { key: "lead", label: "Présentation", type: "textarea", required: true },
    { key: "questions", label: "Questions", type: "list", itemLabel: "q", addLabel: "Ajouter une question", fields: [
      { key: "q", label: "Question", type: "text", required: true },
      { key: "choices", label: "Réponses proposées", type: "stringlist", addLabel: "Ajouter une réponse" },
      { key: "answer", label: "Numéro de la bonne réponse (1 = la première)", type: "answer",
        help: "Sur le site, l'ordre des réponses est mélangé à chaque partie : la bonne réponse peut être écrite à n'importe quelle place." },
      { key: "explain", label: "Explication affichée après la réponse", type: "textarea" },
      { key: "link", label: "Page pour en savoir plus (facultatif)", type: "link", optional: true },
    ] },
  ],
};

TYPES.spot = {
  label: "Spot ou bon plan", plural: "Spots & bons plans", file: "spots", emoji: "⭐", parentType: "island", parentKey: "island",
  path: (e) => `iles/${e.island}/bons-plans.html#${e.slug}`,
  fields: [
    { key: "name", label: "Nom du spot", type: "text", required: true },
    { key: "category", label: "Catégorie", type: "select", options: SPOT_CATEGORIES },
    { key: "fame", label: "Notoriété", type: "select", options: SPOT_FAME,
      help: "Les visiteurs peuvent filtrer les incontournables et les secrets locaux." },
    { key: "where", label: "Où ? (village, quartier, côte…)", type: "text" },
    { key: "text", label: "Description", type: "textarea", required: true,
      help: "Quelques phrases. Pour un lien vers une page du site : [[chemin/de/la/page.html|texte du lien]]." },
    { key: "tip", label: "Bon plan (conseil pratique)", type: "textarea" },
    { key: "media", label: "Image (facultative)", type: "media", optional: true,
      help: "Sans image, celle du lieu associé est utilisée." },
    { key: "place", label: "Lieu associé (facultatif)", type: "ref", ref: "place", optional: true,
      help: "Ajoute un lien « Voir la fiche du lieu »." },
  ],
};

TYPES.institution = {
  label: "Institution ou autorité", plural: "Vie publique & institutions", file: "institutions", emoji: "🏛️",
  parentType: "island", parentKey: "island",
  path: (e) => (e.scope && e.scope !== "ile" ? `iles/vie-publique.html#${e.slug}` : `iles/${e.island}/vie-publique.html#${e.slug}`),
  fields: [
    { key: "name", label: "Nom", type: "text", required: true },
    { key: "scope", label: "Portée", type: "select", options: INSTITUTION_SCOPES,
      help: "L'île choisie dans l'arborescence est celle du siège. Une institution de l'Union s'affiche sur les pages des trois îles de l'Union." },
    { key: "category", label: "Domaine", type: "select", options: INSTITUTION_CATEGORIES },
    { key: "status", label: "Statut", type: "select", options: INSTITUTION_STATUS,
      help: "Distingue les institutions officielles des autorités coutumières ou religieuses et des associations." },
    { key: "seat", label: "Siège ou lieu", type: "text" },
    { key: "text", label: "Présentation", type: "textarea", required: true,
      help: "Rôle, histoire, poids réel dans la vie des habitants. Liens : [[chemin/de/la/page.html|texte du lien]]." },
    { key: "media", label: "Image (facultative)", type: "media", optional: true },
    { ...refsField, label: "Sources (bibliographie)" },
  ],
};

// ------------------------------------------------------------------ Pages fixes (content/pages.json)

const fixedBase = [
  { key: "title", label: "Titre", type: "text", required: true },
  { key: "kicker", label: "Surtitre", type: "text" },
  { key: "hero", label: "Image du bandeau", type: "media" },
  { key: "lead", label: "Chapeau", type: "textarea" },
  { key: "description", label: "Description pour les moteurs de recherche", type: "textarea" },
];
const pick = (...keys) => fixedBase.filter((f) => keys.includes(f.key));

export const FIXED = {
  iles: { label: "Les îles (page d'ensemble)", path: "iles/index.html", fields: fixedBase },
  bonsplans: { label: "Spots & bons plans (page des quatre îles)", path: "iles/bons-plans.html", fields: [...fixedBase,
    { key: "intro", label: "Introduction", type: "richtext" }] },
  viepublique: { label: "Vie publique & institutions (page des quatre îles)", path: "iles/vie-publique.html", fields: [...fixedBase,
    { key: "intro", label: "Introduction", type: "richtext" }] },
  voyager: { label: "Voyager (page d'ensemble)", path: "voyager/index.html", fields: fixedBase },
  experiences: { label: "Expériences (page d'ensemble)", path: "experiences/index.html", fields: fixedBase },
  itineraires: { label: "Itinéraires (page d'ensemble)", path: "itineraires/index.html", fields: fixedBase },
  preparer: { label: "Préparer son voyage (page d'ensemble)", path: "preparer-son-voyage/index.html", fields: [
    ...fixedBase,
    { key: "intro_title", label: "Titre du bloc d'introduction", type: "text" },
    { key: "intro", label: "Bloc d'introduction", type: "richtext" },
  ] },
  agenda: { label: "Agenda & saisons", path: "agenda.html", fields: [...fixedBase,
    { key: "notice", label: "Encadré en bas de page", type: "richtext" }] },
  galerie: { label: "Galerie photos", path: "galerie.html", fields: fixedBase },
  videos: { label: "Vidéos", path: "videos.html", fields: [...fixedBase,
    { key: "feature_text", label: "Texte de la vidéo à la une", type: "richtext" },
    { key: "notice", label: "Encadré en bas de page", type: "richtext" }] },
  glossaire: { label: "Glossaire (page)", path: "glossaire.html", fields: pick("title", "kicker", "lead", "description") },
  contes: { label: "Hale halele (page d'ensemble des contes)", path: "contes/index.html", fields: [...fixedBase,
    { key: "intro", label: "Introduction (formule Hale halele)", type: "richtext" },
    { key: "sections", label: "Sections « L'art du conte » (bas de page)", type: "list", itemLabel: "title", addLabel: "Ajouter une section", fields: [
      { key: "title", label: "Titre", type: "text", required: true },
      { key: "html", label: "Texte", type: "richtext" }] }] },
  loisirs: { label: "Loisirs (page d'ensemble des quiz)", path: "loisirs/index.html", fields: [...fixedBase,
    { key: "intro", label: "Introduction", type: "richtext" }] },
  bibliographie: { label: "Sources & bibliographie (page)", path: "bibliographie.html", fields: [
    ...pick("title", "kicker", "lead", "description"),
    { key: "intro", label: "Introduction", type: "richtext" }] },
  credits: { label: "Crédits", path: "credits.html", fields: [
    { key: "title", label: "Titre", type: "text", required: true },
    { key: "lead", label: "Introduction", type: "richtext" },
    { key: "description", label: "Description pour les moteurs de recherche", type: "textarea" },
    { key: "body", label: "Texte sous le tableau", type: "richtext" }] },
  mentions: { label: "Mentions légales", path: "mentions-legales.html", fields: [
    { key: "title", label: "Titre", type: "text", required: true },
    { key: "description", label: "Description pour les moteurs de recherche", type: "textarea" },
    { key: "body", label: "Texte", type: "richtext" }] },
  contact: { label: "Contact", path: "contact.html", fields: [
    { key: "title", label: "Titre", type: "text", required: true },
    { key: "lead", label: "Chapeau", type: "textarea" },
    { key: "description", label: "Description pour les moteurs de recherche", type: "textarea" },
    { key: "no_email_text", label: "Texte affiché tant qu'aucune adresse e-mail n'est réglée", type: "richtext" },
    { key: "aside_title", label: "Titre de l'encadré", type: "text" },
    { key: "aside", label: "Texte de l'encadré", type: "richtext" }] },
  plan: { label: "Plan du site", path: "plan-du-site.html", fields: pick("title", "description") },
  "404": { label: "Page d'erreur 404", path: "404.html", fields: pick("kicker", "title", "lead", "description") },
};

// ------------------------------------------------------------------ Documents uniques

export const DOCS = {
  home: { label: "Page d'accueil", file: "home", path: "index.html", emoji: "🏠", fields: [
    { key: "title", label: "Grand titre", type: "text", required: true },
    { key: "kicker", label: "Surtitre", type: "text" },
    { key: "lead", label: "Texte d'accroche", type: "textarea" },
    { key: "hero", label: "Image principale", type: "media", required: true },
    { key: "stats", label: "Chiffres clés", type: "list", itemLabel: "value", addLabel: "Ajouter un chiffre", fields: [
      { key: "value", label: "Chiffre", type: "text" }, { key: "label", label: "Légende", type: "text" }] },
    { key: "features", label: "Blocs mis en avant", type: "list", itemLabel: "title", addLabel: "Ajouter un bloc", fields: [
      { key: "media", label: "Image", type: "media" },
      { key: "kicker", label: "Surtitre", type: "text" },
      { key: "title", label: "Titre", type: "text" },
      { key: "text", label: "Texte", type: "textarea" },
      { key: "href", label: "Lien « Lire la suite »", type: "link" }] },
    { key: "facts", label: "« Le saviez-vous ? »", type: "stringlist", addLabel: "Ajouter une anecdote" },
    { key: "gallery", label: "Images de la mosaïque", type: "medialist" },
  ] },
  settings: { label: "Réglages du site", file: "settings", path: null, emoji: "⚙️", fields: [
    { key: "site_name", label: "Nom du site", type: "text", required: true },
    { key: "tagline", label: "Slogan", type: "text" },
    { key: "description", label: "Description (moteurs de recherche, page d'accueil)", type: "textarea" },
    { key: "footer_about", label: "Texte du pied de page", type: "textarea" },
    { key: "updated_label", label: "Date de mise à jour affichée (infos pratiques)", type: "text" },
    { key: "contact_email", label: "Adresse e-mail de contact", type: "text",
      help: "Laissez vide pour masquer le formulaire de contact." },
    { key: "media_categories", label: "Catégories de la galerie", type: "keyvalue",
      help: "Code court (sans espace) et libellé affiché." },
    { key: "custom_domain", label: "Nom de domaine personnel (avancé)", type: "text", danger: true,
      help: "À remplir seulement si vous possédez ce domaine et l'avez configuré chez votre registraire." },
    { key: "github_repo", label: "Dépôt GitHub (avancé)", type: "text", danger: true },
    { key: "github_branch", label: "Branche publiée (avancé)", type: "text", danger: true },
  ] },
  navigation: { label: "Menu et pied de page", file: "navigation", path: null, emoji: "🧭", fields: [
    { key: "menu", label: "Menu principal", type: "list", itemLabel: "label", addLabel: "Ajouter une entrée de menu", fields: [
      { key: "label", label: "Libellé", type: "text", required: true },
      { key: "link", label: "Page ouverte au clic", type: "link" },
      { key: "auto_children", label: "Sous-menu automatique", type: "autochildren" },
      { key: "children", label: "Sous-menu manuel", type: "list", itemLabel: "label", addLabel: "Ajouter un lien", fields: [
        { key: "label", label: "Libellé", type: "text" },
        { key: "note", label: "Petite note (facultatif)", type: "text" },
        { key: "link", label: "Page", type: "link" }] },
    ] },
    { key: "cta", label: "Bouton mis en avant (en haut à droite)", type: "group", fields: [
      { key: "label", label: "Texte du bouton", type: "text" },
      { key: "link", label: "Page", type: "link" }] },
    { key: "footer", label: "Colonnes du pied de page", type: "list", itemLabel: "title", addLabel: "Ajouter une colonne", fields: [
      { key: "title", label: "Titre de la colonne", type: "text" },
      { key: "links", label: "Liens", type: "list", itemLabel: "label", addLabel: "Ajouter un lien", fields: [
        { key: "label", label: "Libellé", type: "text" },
        { key: "link", label: "Page", type: "link" }] }] },
  ] },
  videos: { label: "Vidéos (liste)", file: "videos", path: "videos.html", emoji: "🎬", fields: [
    { key: "items", label: "Vidéos affichées (la première est mise à la une)", type: "medialist", kind: "video" }] },
};

// Listes simples (le fichier JSON est un tableau)
export const LISTS = {
  timeline: { label: "Frise chronologique", file: "timeline", path: "histoire/index.html", emoji: "🕰️",
    itemLabel: "title", addLabel: "Ajouter une date", fields: [
      { key: "date", label: "Date", type: "text", required: true },
      { key: "title", label: "Titre", type: "text", required: true },
      { key: "text", label: "Texte", type: "textarea" },
      { key: "highlight", label: "Afficher aussi sur la page d'accueil", type: "checkbox" }] },
  events: { label: "Agenda", file: "events", path: "agenda.html", emoji: "📅",
    itemLabel: "title", addLabel: "Ajouter un événement", fields: [
      { key: "when", label: "Quand", type: "text" },
      { key: "title", label: "Titre", type: "text", required: true },
      { key: "text", label: "Texte", type: "textarea" },
      { key: "tag", label: "Étiquette", type: "text" }] },
  glossary: { label: "Glossaire", file: "glossary", path: "glossaire.html", emoji: "🔤",
    itemLabel: "term", addLabel: "Ajouter un mot", fields: [
      { key: "term", label: "Mot", type: "text", required: true },
      { key: "definition", label: "Définition", type: "textarea" },
      { key: "link", label: "Page à lire (facultatif)", type: "link", optional: true }] },
  bibliography: { label: "Bibliographie", file: "bibliography", path: "bibliographie.html", emoji: "📖",
    itemLabel: "title", addLabel: "Ajouter une référence", fields: [
      { key: "id", label: "Identifiant court (sans espace)", type: "text", required: true,
        help: "Exemple : walker-2019. Il sert à citer l'ouvrage dans les pages : ne le modifiez pas s'il est déjà cité." },
      { key: "author", label: "Auteur(s)", type: "text", required: true },
      { key: "title", label: "Titre", type: "text", required: true },
      { key: "year", label: "Année", type: "text" },
      { key: "publisher", label: "Éditeur, revue ou précisions", type: "text" },
      { key: "kind", label: "Point de vue", type: "select", options: BIBLIO_KINDS },
      { key: "category", label: "Catégorie", type: "select", options: BIBLIO_CATEGORIES },
      { key: "note", label: "Note de présentation", type: "textarea" },
      { key: "url", label: "Lien vers le texte en ligne (facultatif)", type: "text" }] },
};

export const MEDIA_FIELDS = [
  { key: "caption", label: "Légende", type: "textarea", required: true },
  { key: "island", label: "Catégorie (filtre de la galerie)", type: "category" },
  { key: "author", label: "Auteur / crédit", type: "text" },
  { key: "license", label: "Licence", type: "text" },
  { key: "gallery", label: "Afficher dans la galerie photos", type: "checkbox" },
  { key: "poster", label: "Image d'aperçu (vidéos)", type: "media", optional: true, videoOnly: true },
];

// ------------------------------------------------------------------ Identifiants d'éléments
// island:slug · place:slug · topic:slug · topicpage:topic/slug · experience:slug · itinerary:slug
// practical:slug · fixed:clé · doc:home|settings|navigation|videos · list:timeline|events|glossary|quiz · media:clé

export function parseId(id) {
  const i = id.indexOf(":");
  const type = id.slice(0, i);
  const rest = id.slice(i + 1);
  if (type === "topicpage") {
    const [topic, slug] = rest.split("/");
    return { type, topic, slug };
  }
  return { type, slug: rest };
}

export function idOf(type, entity, parent) {
  return type === "topicpage" ? `topicpage:${parent.slug}/${entity.slug}` : `${type}:${entity.slug}`;
}

export function getEntity(data, id) {
  const p = parseId(id);
  if (p.type === "topicpage") {
    const topic = data.topics.find((t) => t.slug === p.topic);
    return topic && topic.pages.find((pg) => pg.slug === p.slug);
  }
  if (TYPES[p.type]) return data[TYPES[p.type].file].find((e) => e.slug === p.slug);
  if (p.type === "fixed") return data.pages[p.slug];
  if (p.type === "doc") return data[DOCS[p.slug].file];
  if (p.type === "list") return { items: data[LISTS[p.slug].file] };
  if (p.type === "media") return data.media[p.slug];
  return null;
}

export function setEntity(data, id, value) {
  const p = parseId(id);
  if (p.type === "topicpage") {
    const topic = data.topics.find((t) => t.slug === p.topic);
    topic.pages[topic.pages.findIndex((pg) => pg.slug === p.slug)] = value;
  } else if (TYPES[p.type]) {
    const arr = data[TYPES[p.type].file];
    arr[arr.findIndex((e) => e.slug === p.slug)] = value;
  } else if (p.type === "fixed") data.pages[p.slug] = value;
  else if (p.type === "doc") data[DOCS[p.slug].file] = value;
  else if (p.type === "list") data[LISTS[p.slug].file] = value.items;
  else if (p.type === "media") data.media[p.slug] = value;
}

export function fileOf(id) {
  const p = parseId(id);
  if (TYPES[p.type]) return TYPES[p.type].file;
  if (p.type === "fixed") return "pages";
  if (p.type === "doc") return DOCS[p.slug].file;
  if (p.type === "list") return LISTS[p.slug].file;
  if (p.type === "media") return "media";
  return null;
}

export function schemaOf(id) {
  const p = parseId(id);
  if (TYPES[p.type]) return TYPES[p.type].fields;
  if (p.type === "fixed") return FIXED[p.slug].fields;
  if (p.type === "doc") return DOCS[p.slug].fields;
  if (p.type === "list") {
    const l = LISTS[p.slug];
    return [{ key: "items", label: l.label, type: "list", itemLabel: l.itemLabel, addLabel: l.addLabel, fields: l.fields }];
  }
  if (p.type === "media") return MEDIA_FIELDS;
  return [];
}

export function typeLabel(id) {
  const p = parseId(id);
  if (TYPES[p.type]) return TYPES[p.type].label;
  return { fixed: "Page", doc: "Document", list: "Liste", media: "Média" }[p.type] || p.type;
}

export function titleOf(data, id) {
  const p = parseId(id);
  const e = getEntity(data, id);
  if (!e) return id;
  if (TYPES[p.type]) return e.name || e.slug;
  if (p.type === "fixed") return FIXED[p.slug].label;
  if (p.type === "doc") return DOCS[p.slug].label;
  if (p.type === "list") return LISTS[p.slug].label;
  if (p.type === "media") return e.caption || p.slug;
  return id;
}

export function pathOf(data, id) {
  const p = parseId(id);
  if (p.type === "topicpage") {
    const topic = data.topics.find((t) => t.slug === p.topic);
    return `${topic.slug}/${p.slug}.html`;
  }
  if (TYPES[p.type]) return TYPES[p.type].path(getEntity(data, id) || { slug: p.slug });
  if (p.type === "fixed") return FIXED[p.slug].path;
  if (p.type === "doc") return DOCS[p.slug].path;
  if (p.type === "list") return LISTS[p.slug].path;
  return null;
}

export const isPublished = (e) => !e || e.published !== false;

/** Toutes les pages éditoriales, dans l'ordre de l'arborescence. */
export function allEntityIds(data) {
  const ids = [];
  data.islands.forEach((i) => ids.push(`island:${i.slug}`));
  data.places.forEach((p) => ids.push(`place:${p.slug}`));
  data.topics.forEach((t) => {
    ids.push(`topic:${t.slug}`);
    t.pages.forEach((pg) => ids.push(`topicpage:${t.slug}/${pg.slug}`));
  });
  ["experiences", "itineraries", "practical", "tales", "quizzes", "spots", "institutions"].forEach((file) => {
    const type = Object.keys(TYPES).find((k) => TYPES[k].file === file);
    data[file].forEach((e) => ids.push(`${type}:${e.slug}`));
  });
  return ids;
}

/** Une page est réellement en ligne si elle et ses parents sont publiés. */
export function isOnline(data, id) {
  const p = parseId(id);
  const e = getEntity(data, id);
  if (!e || !isPublished(e)) return false;
  if (p.type === "place" || p.type === "spot") return isOnline(data, `island:${e.island}`);
  if (p.type === "institution" && (e.scope || "ile") === "ile") return isOnline(data, `island:${e.island}`);
  if (p.type === "topicpage") return isOnline(data, `topic:${p.topic}`);
  return true;
}

/** Liste des pages du site pour les sélecteurs de liens. */
export function sitePages(data) {
  const pages = [{ path: "index.html", title: "Accueil", group: "Général" }];
  pages.push({ path: "iles/index.html", title: data.pages.iles.title, group: "Les îles" });
  data.islands.forEach((i) => {
    pages.push({ path: `iles/${i.slug}.html`, title: i.name, group: "Les îles", hidden: !isPublished(i) });
    pages.push({ path: `iles/${i.slug}/bons-plans.html`, title: `${i.name} : spots & bons plans`, group: "Les îles", hidden: !isPublished(i) });
    pages.push({ path: `iles/${i.slug}/vie-publique.html`, title: `${i.name} : vie publique & institutions`, group: "Les îles", hidden: !isPublished(i) });
  });
  pages.push({ path: "iles/bons-plans.html", title: data.pages.bonsplans.title + " (les quatre îles)", group: "Les îles" });
  pages.push({ path: "iles/vie-publique.html", title: data.pages.viepublique.title + " (les quatre îles)", group: "Les îles" });
  data.places.forEach((p) => pages.push({ path: `lieux/${p.slug}.html`, title: p.name, group: "Lieux", hidden: !isOnline(data, `place:${p.slug}`) }));
  data.topics.forEach((t) => {
    pages.push({ path: `${t.slug}/index.html`, title: `${t.name} (vue d'ensemble)`, group: t.name, hidden: !isPublished(t) });
    t.pages.forEach((pg) => pages.push({ path: `${t.slug}/${pg.slug}.html`, title: pg.name, group: t.name,
      hidden: !isOnline(data, `topicpage:${t.slug}/${pg.slug}`) }));
  });
  pages.push({ path: "voyager/index.html", title: data.pages.voyager.title, group: "Voyager" });
  pages.push({ path: "experiences/index.html", title: data.pages.experiences.title, group: "Voyager" });
  data.experiences.forEach((e) => pages.push({ path: `experiences/${e.slug}.html`, title: e.name, group: "Expériences", hidden: !isPublished(e) }));
  pages.push({ path: "itineraires/index.html", title: data.pages.itineraires.title, group: "Voyager" });
  data.itineraries.forEach((e) => pages.push({ path: `itineraires/${e.slug}.html`, title: e.name, group: "Itinéraires", hidden: !isPublished(e) }));
  pages.push({ path: "preparer-son-voyage/index.html", title: data.pages.preparer.title, group: "Voyager" });
  data.practical.forEach((e) => pages.push({ path: `preparer-son-voyage/${e.slug}.html`, title: e.name, group: "Infos pratiques", hidden: !isPublished(e) }));
  pages.push({ path: "contes/index.html", title: data.pages.contes.title, group: "Hale halele (contes)" });
  data.tales.forEach((e) => pages.push({ path: `contes/${e.slug}.html`, title: e.name, group: "Hale halele (contes)", hidden: !isPublished(e) }));
  pages.push({ path: "loisirs/index.html", title: data.pages.loisirs.title, group: "Loisirs" });
  data.quizzes.forEach((e) => pages.push({ path: `loisirs/${e.slug}.html`, title: `Quiz : ${e.name}`, group: "Loisirs", hidden: !isPublished(e) }));
  [["agenda.html", data.pages.agenda.title], ["galerie.html", data.pages.galerie.title], ["videos.html", data.pages.videos.title],
   ["glossaire.html", data.pages.glossaire.title], ["bibliographie.html", data.pages.bibliographie.title], ["contact.html", data.pages.contact.title],
   ["credits.html", data.pages.credits.title], ["mentions-legales.html", data.pages.mentions.title],
   ["plan-du-site.html", data.pages.plan.title]].forEach(([path, title]) => pages.push({ path, title, group: "Pages annexes" }));
  return pages;
}

export function pageTitleByPath(data, path) {
  const clean = (path || "").split("#")[0];
  const p = sitePages(data).find((x) => x.path === clean);
  return p ? p.title : null;
}

// ------------------------------------------------------------------ Parcours génériques

const MEDIA_KEYS = new Set(["hero", "card", "media", "poster", "spots_hero", "public_hero"]);
const MEDIA_LIST_KEYS = new Set(["gallery"]);

/** Documents et éléments à parcourir pour trouver des références, avec un identifiant lisible. */
function* owners(data) {
  for (const id of allEntityIds(data)) {
    const e = getEntity(data, id);
    if (parseId(id).type === "topic") {
      const { pages, ...rest } = e; // les articles sont parcourus séparément
      yield [id, rest];
    } else yield [id, e];
  }
  for (const key of Object.keys(FIXED)) yield [`fixed:${key}`, data.pages[key]];
  for (const key of Object.keys(DOCS)) yield [`doc:${key}`, data[DOCS[key].file]];
  for (const key of Object.keys(LISTS)) yield [`list:${key}`, data[LISTS[key].file]];
  for (const [key, m] of Object.entries(data.media)) yield [`media:${key}`, m];
}

function walk(value, visit, key = null) {
  if (Array.isArray(value)) value.forEach((v) => walk(v, visit, key));
  else if (value && typeof value === "object") Object.entries(value).forEach(([k, v]) => { visit(k, v); walk(v, visit, k); });
}

/** Où une image est-elle utilisée ? → [{ id, title }] */
export function mediaUsages(data, key) {
  const out = [];
  for (const [id, obj] of owners(data)) {
    if (id === `media:${key}`) continue;
    let used = false;
    walk(obj, (k, v) => {
      if (MEDIA_KEYS.has(k) && v === key) used = true;
      if ((MEDIA_LIST_KEYS.has(k) || (id === "doc:videos" && k === "items")) && Array.isArray(v) && v.includes(key)) used = true;
    });
    if (used) out.push({ id, title: titleOf(data, id) });
  }
  return out;
}

/** Pages qui contiennent un lien vers `path` (champ lien ou lien dans un texte). */
export function inboundLinks(data, path, { prefix = false } = {}) {
  const out = [];
  const matches = (v) => {
    if (typeof v !== "string") return false;
    if (prefix) return v.startsWith(path) || v.includes(`[[${path}`);
    return v === path || v.startsWith(path + "#") || v.includes(`[[${path}|`) || v.includes(`[[${path}#`);
  };
  for (const [id, obj] of owners(data)) {
    let n = 0;
    walk(obj, (k, v) => { if (matches(v)) n += 1; });
    if (n) out.push({ id, title: titleOf(data, id), count: n });
  }
  return out;
}

/** Références typées par adresse courte (slug) : lieux et îles. */
export function slugReferences(data, id) {
  const p = parseId(id);
  const out = [];
  if (p.type === "place") {
    data.islands.forEach((i) => { if ((i.places || []).includes(p.slug)) out.push({ id: `island:${i.slug}`, title: i.name, how: "liste des lieux de l'île" }); });
    data.experiences.forEach((e) => { if ((e.places || []).includes(p.slug)) out.push({ id: `experience:${e.slug}`, title: e.name, how: "lieux de l'expérience" }); });
    data.itineraries.forEach((it) => { if (it.days.some((d) => d.place === p.slug)) out.push({ id: `itinerary:${it.slug}`, title: it.name, how: "étape de l'itinéraire" }); });
    data.tales.forEach((t) => { if (t.place === p.slug) out.push({ id: `tale:${t.slug}`, title: t.name, how: "lieu associé au récit" }); });
    data.spots.forEach((x) => { if (x.place === p.slug) out.push({ id: `spot:${x.slug}`, title: x.name, how: "lieu associé au spot" }); });
  }
  if (p.type === "island") {
    data.places.forEach((pl) => { if (pl.island === p.slug) out.push({ id: `place:${pl.slug}`, title: pl.name, how: "lieu de cette île" }); });
    data.itineraries.forEach((it) => { if ((it.islands || []).includes(p.slug)) out.push({ id: `itinerary:${it.slug}`, title: it.name, how: "île traversée" }); });
    data.tales.forEach((t) => { if (t.island === p.slug) out.push({ id: `tale:${t.slug}`, title: t.name, how: "île du récit" }); });
    data.spots.forEach((x) => { if (x.island === p.slug) out.push({ id: `spot:${x.slug}`, title: x.name, how: "spot de cette île" }); });
    data.institutions.forEach((x) => { if (x.island === p.slug) out.push({ id: `institution:${x.slug}`, title: x.name, how: "institution dont le siège est sur cette île" }); });
  }
  return out;
}

/** Pages du site sur lesquelles un élément apparaît (sa page, listes, menus…). */
export function appearsOn(data, id) {
  const p = parseId(id);
  const e = getEntity(data, id);
  const list = [];
  const add = (path, why) => { if (path && !list.some((x) => x.path === path)) list.push({ path, why, title: pageTitleByPath(data, path) || path }); };
  const own = pathOf(data, id);
  if (own) add(own, "sa propre page");
  switch (p.type) {
    case "island":
      add("index.html", "cartes des îles de l'accueil"); add("iles/index.html", "tableau comparatif et carte");
      add("voyager/index.html", "liste des lieux par île");
      data.islands.filter((i) => i.slug !== p.slug).forEach((i) => add(`iles/${i.slug}.html`, "« Continuer vers les autres îles »"));
      data.places.filter((pl) => pl.island === p.slug).forEach((pl) => add(`lieux/${pl.slug}.html`, "fil d'Ariane du lieu"));
      islandSubPaths(p.slug).forEach((path) => add(path, "page de l'île (onglets, fil d'Ariane)"));
      add("iles/bons-plans.html", "page des bons plans des quatre îles"); add("iles/vie-publique.html", "page de la vie publique des quatre îles");
      data.islands.filter((i) => i.slug !== p.slug).forEach((i) => islandSubPaths(i.slug).forEach((path) => add(path, "menu latéral « autres îles »")));
      break;
    case "spot":
      add(`iles/${e.island}.html`, "aperçu « Spots & bons plans » de l'île (6 premiers)"); add("iles/bons-plans.html", "page des bons plans des quatre îles");
      break;
    case "institution":
      add(`iles/${e.island}.html`, "compteurs « Vie publique » de l'île"); add("iles/vie-publique.html", "page de la vie publique des quatre îles");
      if ((e.scope || "ile") !== "ile") {
        data.islands.filter((i) => e.scope === "archipel" || i.union_member).forEach((i) => {
          add(`iles/${i.slug}/vie-publique.html`, e.scope === "union" ? "bloc « Union des Comores »" : "bloc « Tout l'archipel »");
          add(`iles/${i.slug}.html`, "compteurs « Vie publique » de l'île");
        });
      }
      break;
    case "place":
      add(`iles/${e.island}.html`, "« À voir » de l'île"); add("iles/index.html", "carte des îles"); add("voyager/index.html", "lieux incontournables");
      data.places.filter((pl) => pl.island === e.island && pl.slug !== p.slug).forEach((pl) => add(`lieux/${pl.slug}.html`, "« Autres lieux »"));
      data.experiences.filter((x) => (x.places || []).includes(p.slug)).forEach((x) => add(`experiences/${x.slug}.html`, "« Où vivre cette expérience ? »"));
      data.itineraries.filter((x) => x.days.some((d) => d.place === p.slug)).forEach((x) => add(`itineraires/${x.slug}.html`, "étape d'itinéraire"));
      break;
    case "topic":
      add("index.html", "tuiles « Explorer par thème »");
      e.pages.forEach((pg) => add(`${p.slug}/${pg.slug}.html`, "article de la rubrique"));
      data.topics.filter((t) => t.slug !== p.slug).forEach((t) => add(`${t.slug}/index.html`, "« Explorer d'autres rubriques »"));
      break;
    case "topicpage": {
      const topic = data.topics.find((t) => t.slug === p.topic);
      add(`${topic.slug}/index.html`, "liste des articles de la rubrique");
      topic.pages.filter((pg) => pg.slug !== p.slug).forEach((pg) => add(`${topic.slug}/${pg.slug}.html`, "menu latéral de la rubrique"));
      break;
    }
    case "experience":
      add("experiences/index.html", "liste des expériences"); add("voyager/index.html", "tuiles expériences");
      data.experiences.filter((x) => x.slug !== p.slug).forEach((x) => add(`experiences/${x.slug}.html`, "« Autres expériences »"));
      break;
    case "itinerary":
      add("itineraires/index.html", "liste des itinéraires"); add("voyager/index.html", "itinéraires"); add("index.html", "itinéraires de l'accueil (4 premiers)");
      data.itineraries.filter((x) => x.slug !== p.slug).forEach((x) => add(`itineraires/${x.slug}.html`, "« Autres itinéraires »"));
      break;
    case "practical":
      add("preparer-son-voyage/index.html", "liste des infos pratiques"); add("voyager/index.html", "tuiles infos pratiques");
      data.practical.filter((x) => x.slug !== p.slug).forEach((x) => add(`preparer-son-voyage/${x.slug}.html`, "menu latéral"));
      break;
    case "tale":
      add("contes/index.html", "liste des contes et récits");
      if (e.featured) add("index.html", "« Les contes du soir » de l'accueil");
      data.tales.filter((x) => x.slug !== p.slug && x.kind === e.kind).forEach((x) => add(`contes/${x.slug}.html`, "menu latéral des récits du même genre"));
      {
        const i = data.tales.findIndex((x) => x.slug === p.slug);
        [data.tales[i - 1], data.tales[i + 1]].filter(Boolean).forEach((x) => add(`contes/${x.slug}.html`, "« Récit précédent / suivant »"));
      }
      break;
    case "quiz": {
      add("loisirs/index.html", "liste des quiz");
      const i = data.quizzes.findIndex((x) => x.slug === p.slug);
      const prev = data.quizzes[(i - 1 + data.quizzes.length) % data.quizzes.length];
      if (prev && prev.slug !== p.slug) add(`loisirs/${prev.slug}.html`, "bouton « Quiz suivant »");
      break;
    }
    case "list":
      if (p.slug === "bibliography") citingPages(data).forEach((x) => add(x.path, "références en bas de page"));
      break;
    case "media":
      mediaUsages(data, p.slug).forEach((u) => add(pathOf(data, u.id), `utilisée par « ${u.title} »`));
      if (e && e.gallery !== false && (e.kind || "image") === "image") add("galerie.html", "galerie photos");
      add("credits.html", "page des crédits");
      break;
    default:
      break;
  }
  if (TYPES[p.type]) inboundLinks(data, own).forEach((l) => add(pathOf(data, l.id), `lien dans « ${l.title} »`));
  return list;
}

/** Entrées du menu (et pied de page) qui pointent vers une page ou affichent un sous-menu automatique. */
export function menuMentions(data, id) {
  const p = parseId(id);
  const path = pathOf(data, id);
  const out = [];
  const nav = data.navigation;
  nav.menu.forEach((m) => {
    if (m.link === path) out.push(`Menu : « ${m.label} »`);
    (m.children || []).forEach((c) => { if (c.link === path) out.push(`Sous-menu « ${m.label} » : « ${c.label} »`); });
    if (p.type === "island" && m.auto_children === "iles") out.push(`Sous-menu automatique « ${m.label} »`);
    if (p.type === "topic" && m.auto_children === `rubrique:${p.slug}`) out.push(`Sous-menu automatique « ${m.label} »`);
    if (p.type === "topicpage" && m.auto_children === `rubrique:${p.topic}`) out.push(`Sous-menu automatique « ${m.label} »`);
    if (p.type === "experience" && m.auto_children === "experiences") out.push(`Sous-menu automatique « ${m.label} »`);
    if (p.type === "itinerary" && m.auto_children === "itineraires") out.push(`Sous-menu automatique « ${m.label} »`);
    if (p.type === "practical" && m.auto_children === "pratique") out.push(`Sous-menu automatique « ${m.label} »`);
    if (p.type === "tale" && m.auto_children === "contes") out.push(`Sous-menu automatique « ${m.label} » (catégories)`);
    if (p.type === "quiz" && m.auto_children === "loisirs") out.push(`Sous-menu automatique « ${m.label} »`);
  });
  if (nav.cta && nav.cta.link === path) out.push("Bouton du menu");
  nav.footer.forEach((col) => col.links.forEach((l) => { if (l.link === path) out.push(`Pied de page « ${col.title} » : « ${l.label} »`); }));
  return out;
}

// ------------------------------------------------------------------ Modifications de structure

export function slugify(text) {
  return (text || "").normalize("NFKD").replace(/[̀-ͯ]/g, "").toLowerCase()
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

export function uniqueSlug(existing, base) {
  let slug = slugify(base) || "page";
  let n = 2;
  const taken = new Set(existing);
  const root = slug;
  while (taken.has(slug)) slug = `${root}-${n++}`;
  return slug;
}

export function siblingsSlugs(data, type, parentSlug) {
  if (type === "topicpage") return data.topics.find((t) => t.slug === parentSlug).pages.map((p) => p.slug);
  return data[TYPES[type].file].map((e) => e.slug);
}

/** Remplace partout un chemin (lien) par un autre. Renvoie le nombre de remplacements. */
export function replacePaths(data, oldPath, newPath, { prefix = false } = {}) {
  let count = 0;
  const fix = (s) => {
    let out = s;
    if (prefix) {
      if (out.startsWith(oldPath)) { out = newPath + out.slice(oldPath.length); }
      out = out.split(`[[${oldPath}`).join(`[[${newPath}`);
    } else {
      if (out === oldPath || out.startsWith(oldPath + "#")) out = newPath + out.slice(oldPath.length);
      out = out.split(`[[${oldPath}|`).join(`[[${newPath}|`).split(`[[${oldPath}#`).join(`[[${newPath}#`);
    }
    if (out !== s) count += 1;
    return out;
  };
  const rec = (v) => {
    if (Array.isArray(v)) return v.map(rec);
    if (v && typeof v === "object") { for (const k of Object.keys(v)) v[k] = rec(v[k]); return v; }
    return typeof v === "string" ? fix(v) : v;
  };
  for (const f of Object.keys(data)) data[f] = rec(data[f]);
  return count;
}

/** Change l'adresse (slug) d'un élément et met à jour toutes les références. */
export function renameSlug(data, id, newSlug) {
  const p = parseId(id);
  const e = getEntity(data, id);
  const oldPath = pathOf(data, id);
  const oldSlug = e.slug;
  if (p.type === "topic") {
    e.slug = newSlug;
    const n = replacePaths(data, `${oldSlug}/`, `${newSlug}/`, { prefix: true });
    data.navigation.menu.forEach((m) => { if (m.auto_children === `rubrique:${oldSlug}`) m.auto_children = `rubrique:${newSlug}`; });
    return n;
  }
  e.slug = newSlug;
  const newPath = pathOf(data, p.type === "topicpage" ? `topicpage:${p.topic}/${newSlug}` : `${p.type}:${newSlug}`);
  const n = replacePaths(data, oldPath, newPath);
  if (p.type === "place") {
    data.islands.forEach((i) => { i.places = (i.places || []).map((s) => (s === oldSlug ? newSlug : s)); });
    data.experiences.forEach((x) => { x.places = (x.places || []).map((s) => (s === oldSlug ? newSlug : s)); });
    data.itineraries.forEach((it) => it.days.forEach((d) => { if (d.place === oldSlug) d.place = newSlug; }));
    data.tales.forEach((t) => { if (t.place === oldSlug) t.place = newSlug; });
    data.spots.forEach((x) => { if (x.place === oldSlug) x.place = newSlug; });
  }
  if (p.type === "island") {
    replacePaths(data, `iles/${oldSlug}/`, `iles/${newSlug}/`, { prefix: true });
    data.places.forEach((pl) => { if (pl.island === oldSlug) pl.island = newSlug; });
    data.spots.forEach((x) => { if (x.island === oldSlug) x.island = newSlug; });
    data.institutions.forEach((x) => { if (x.island === oldSlug) x.island = newSlug; });
    data.itineraries.forEach((it) => { it.islands = (it.islands || []).map((s) => (s === oldSlug ? newSlug : s)); });
    data.tales.forEach((t) => { if (t.island === oldSlug) t.island = newSlug; });
  }
  return n;
}

/** Supprime un élément et nettoie ses références typées. */
export function deleteEntity(data, id) {
  const p = parseId(id);
  if (p.type === "topicpage") {
    const topic = data.topics.find((t) => t.slug === p.topic);
    topic.pages = topic.pages.filter((pg) => pg.slug !== p.slug);
    return;
  }
  const file = TYPES[p.type].file;
  data[file] = data[file].filter((e) => e.slug !== p.slug);
  if (p.type === "place") {
    data.islands.forEach((i) => { i.places = (i.places || []).filter((s) => s !== p.slug); });
    data.experiences.forEach((x) => { x.places = (x.places || []).filter((s) => s !== p.slug); });
    data.itineraries.forEach((it) => it.days.forEach((d) => { if (d.place === p.slug) d.place = ""; }));
    data.tales.forEach((t) => { if (t.place === p.slug) t.place = ""; });
    data.spots.forEach((x) => { if (x.place === p.slug) x.place = ""; });
  }
  if (p.type === "island") {
    data.itineraries.forEach((it) => { it.islands = (it.islands || []).filter((s) => s !== p.slug); });
    data.tales.forEach((t) => { if (t.island === p.slug) t.island = ""; });
  }
  if (p.type === "topic") {
    data.navigation.menu = data.navigation.menu.map((m) => (m.auto_children === `rubrique:${p.slug}` ? { ...m, auto_children: "" } : m));
  }
}

/** Déplace un élément d'un cran dans sa liste (dir = -1 ou +1). */
export function moveInList(data, id, dir) {
  const p = parseId(id);
  let arr;
  if (p.type === "topicpage") arr = data.topics.find((t) => t.slug === p.topic).pages;
  else if (p.type === "place") {
    const place = getEntity(data, id);
    const island = data.islands.find((i) => i.slug === place.island);
    arr = island.places;
    const idx = arr.indexOf(p.slug);
    const to = idx + dir;
    if (idx < 0 || to < 0 || to >= arr.length) return false;
    [arr[idx], arr[to]] = [arr[to], arr[idx]];
    return true;
  } else if (p.type === "spot" || p.type === "institution") {
    arr = data[TYPES[p.type].file];
    const idx = arr.findIndex((e) => e.slug === p.slug);
    const island = arr[idx] && arr[idx].island;
    let to = idx + dir;
    while (to >= 0 && to < arr.length && arr[to].island !== island) to += dir;
    if (idx < 0 || to < 0 || to >= arr.length) return false;
    [arr[idx], arr[to]] = [arr[to], arr[idx]];
    return true;
  } else arr = data[TYPES[p.type].file];
  const idx = arr.findIndex((e) => e.slug === p.slug);
  const to = idx + dir;
  if (idx < 0 || to < 0 || to >= arr.length) return false;
  [arr[idx], arr[to]] = [arr[to], arr[idx]];
  return true;
}

/** Rattache un lieu à une autre île. */
export function movePlace(data, placeSlug, islandSlug) {
  const place = data.places.find((p) => p.slug === placeSlug);
  const from = data.islands.find((i) => i.slug === place.island);
  const to = data.islands.find((i) => i.slug === islandSlug);
  if (from) from.places = (from.places || []).filter((s) => s !== placeSlug);
  to.places = [...(to.places || []), placeSlug];
  place.island = islandSlug;
}

/** Rattache un spot ou une institution à une autre île (son ancre change de page). Renvoie le nombre de liens mis à jour. */
export function moveToIsland(data, id, islandSlug) {
  const e = getEntity(data, id);
  const oldPath = pathOf(data, id);
  e.island = islandSlug;
  const newPath = pathOf(data, id);
  return oldPath === newPath ? 0 : replacePaths(data, oldPath, newPath);
}

/** Déplace un article vers une autre rubrique (son adresse change). Renvoie le nouvel identifiant. */
export function moveTopicPage(data, id, targetTopicSlug) {
  const p = parseId(id);
  const from = data.topics.find((t) => t.slug === p.topic);
  const to = data.topics.find((t) => t.slug === targetTopicSlug);
  const page = from.pages.find((pg) => pg.slug === p.slug);
  let slug = page.slug;
  if (to.pages.some((pg) => pg.slug === slug)) slug = uniqueSlug(to.pages.map((x) => x.slug), slug);
  const oldPath = `${from.slug}/${page.slug}.html`;
  from.pages = from.pages.filter((pg) => pg !== page);
  page.slug = slug;
  to.pages.push(page);
  replacePaths(data, oldPath, `${to.slug}/${slug}.html`);
  return `topicpage:${to.slug}/${slug}`;
}

/** Modèle d'un nouvel élément. */
export function blankEntity(data, type, title, parentSlug) {
  const firstMedia = Object.keys(data.media).find((k) => (data.media[k].kind || "image") === "image");
  const slug = uniqueSlug(siblingsSlugs(data, type, parentSlug), title);
  const section = { title: "Première section", html: "<p>Écrivez ici le texte de la section.</p>" };
  const base = { slug, name: title, published: false };
  switch (type) {
    case "island":
      return { ...base, local: "", tagline: "", status: "", chef_lieu: "", area: "", summit: "", language: "", accent: "#0b4f5c",
        hero: firstMedia, card: firstMedia, map: [-12.2, 44.2, 10], lead: "Résumé de l'île.", intro: "<p>Présentation de l'île.</p>",
        themes: [{ key: "geo", title: "Géographie", media: firstMedia, html: "<p>Texte.</p>" }], places: [], gallery: [], tips: [] };
    case "place": {
      const island = data.islands.find((i) => i.slug === parentSlug);
      return { ...base, island: parentSlug, kicker: island ? island.name : "", hero: firstMedia,
        coords: island && island.map ? [island.map[0], island.map[1]] : [-12.2, 44.2],
        lead: "Résumé du lieu.", sections: [section], facts: [], gallery: [] };
    }
    case "topic":
      return { ...base, icon: "book", hero: firstMedia, card: firstMedia, lead: "Résumé de la rubrique.",
        intro: "<p>Introduction de la rubrique.</p>", facts: [], show_timeline: false, pages: [] };
    case "topicpage":
      return { ...base, icon: "book", hero: firstMedia, lead: "Résumé de l'article.", sections: [section], gallery: [] };
    case "experience":
      return { ...base, icon: "leaf", hero: firstMedia, card: firstMedia, lead: "Résumé de l'expérience.", sections: [section], places: [], gallery: [] };
    case "itinerary":
      return { ...base, theme: "", duration: "", islands: [], hero: firstMedia, card: firstMedia, lead: "Résumé de l'itinéraire.",
        days: [{ when: "Jour 1", title: "Première étape", text: "", place: "" }], tips: "" };
    case "practical":
      return { ...base, icon: "list", hero: firstMedia, summary: "Résumé de la page.", sections: [section] };
    case "tale":
      return { ...base, kind: "conte", local: "", island: "", place: "", hero: firstMedia, lead: "Résumé du récit.",
        text: "<p>Il était une fois…</p>", moral: "", about: "<p>Origine du récit, variantes, ce qu'en disent les historiens.</p>",
        refs: [], featured: false };
    case "spot":
      return { ...base, island: parentSlug, category: "marche", fame: "incontournable", where: "",
        text: "Décrivez le lieu en quelques phrases.", tip: "", media: "", place: "" };
    case "institution":
      return { ...base, island: parentSlug, scope: "ile", category: "politique", status: "officiel", seat: "",
        text: "Présentez son rôle et son poids dans la vie des habitants.", media: "", refs: [] };
    case "quiz":
      return { ...base, icon: "question", hero: firstMedia, level: "Facile", lead: "Présentation du quiz.",
        questions: [{ q: "Première question ?", choices: ["Réponse A", "Réponse B"], answer: 0, explain: "", link: "" }] };
    default:
      return base;
  }
}

export function insertEntity(data, type, entity, parentSlug) {
  if (type === "topicpage") data.topics.find((t) => t.slug === parentSlug).pages.push(entity);
  else data[TYPES[type].file].push(entity);
  if (type === "place") {
    const island = data.islands.find((i) => i.slug === parentSlug);
    island.places = [...(island.places || []), entity.slug];
  }
  return type === "topicpage" ? `topicpage:${parentSlug}/${entity.slug}` : `${type}:${entity.slug}`;
}

// ------------------------------------------------------------------ Différences entre deux versions

export function diffFields(fields, before, after) {
  const changes = [];
  for (const f of fields) {
    // Un champ facultatif vide peut valoir "", null ou être absent : ce n'est pas une modification
    const empty = (v) => (v === "" || v === null || v === undefined ? undefined : v);
    const a = JSON.stringify(empty(before ? before[f.key] : undefined));
    const b = JSON.stringify(empty(after ? after[f.key] : undefined));
    if (a === b) continue;
    if (f.type === "list" && Array.isArray(before && before[f.key]) && Array.isArray(after[f.key])) {
      const n0 = before[f.key].length;
      const n1 = after[f.key].length;
      const detail = n1 > n0 ? `${n1 - n0} ajout(s)` : n1 < n0 ? `${n0 - n1} suppression(s)` : "contenu ou ordre modifié";
      changes.push(`${f.label} : ${detail}`);
    } else changes.push(f.label);
  }
  return changes;
}

// ------------------------------------------------------------------ Bibliographie

/** Pages qui citent des références : [{ id, title, path, refs }] */
export function citingPages(data) {
  const out = [];
  data.topics.forEach((t) => t.pages.forEach((pg) => {
    if ((pg.refs || []).length) out.push({ id: `topicpage:${t.slug}/${pg.slug}`, title: pg.name, path: `${t.slug}/${pg.slug}.html`, refs: pg.refs });
  }));
  data.tales.forEach((t) => {
    if ((t.refs || []).length) out.push({ id: `tale:${t.slug}`, title: t.name, path: `contes/${t.slug}.html`, refs: t.refs });
  });
  data.institutions.forEach((x) => {
    if ((x.refs || []).length) out.push({ id: `institution:${x.slug}`, title: x.name, path: TYPES.institution.path(x).split("#")[0], refs: x.refs });
  });
  return out;
}

/** Pages qui citent une référence donnée. */
export function citationsOf(data, rid) {
  return citingPages(data).filter((pg) => pg.refs.includes(rid));
}

// ------------------------------------------------------------------ Vérifications avant publication

export function validate(data, reserved = []) {
  const errors = [];
  const warnings = [];
  const media = data.media;
  const needMedia = (key, where, optional) => {
    if (!key) { if (!optional) errors.push(`${where} : image manquante`); return; }
    if (!media[key]) errors.push(`${where} : l'image « ${key} » n'existe plus dans la médiathèque`);
  };
  const unique = (items, where) => {
    const seen = new Set();
    items.forEach((it) => {
      if (!it.slug) errors.push(`${where} : un élément n'a pas d'adresse`);
      else if (seen.has(it.slug)) errors.push(`${where} : l'adresse « ${it.slug} » est utilisée deux fois`);
      seen.add(it.slug);
    });
  };
  unique(data.islands, "Îles"); unique(data.places, "Lieux"); unique(data.topics, "Rubriques");
  unique(data.experiences, "Expériences"); unique(data.itineraries, "Itinéraires"); unique(data.practical, "Infos pratiques");
  unique(data.tales, "Contes et récits"); unique(data.quizzes, "Quiz");
  unique(data.spots, "Spots & bons plans"); unique(data.institutions, "Institutions");
  data.islands.forEach((i) => {
    if (["index", "bons-plans", "vie-publique"].includes(i.slug)) errors.push(`Île « ${i.name} » : l'adresse « ${i.slug} » est réservée par le site`);
  });
  data.spots.forEach((x) => {
    if (!data.islands.some((i) => i.slug === x.island)) errors.push(`Spot « ${x.name} » : île inconnue`);
    if (!SPOT_CATEGORIES[x.category]) errors.push(`Spot « ${x.name} » : catégorie inconnue`);
    if (!SPOT_FAME[x.fame]) errors.push(`Spot « ${x.name} » : notoriété inconnue`);
    if (x.place && !data.places.some((pl) => pl.slug === x.place)) warnings.push(`Spot « ${x.name} » : le lieu associé n'existe plus (le lien sera retiré)`);
  });
  data.institutions.forEach((x) => {
    if ((x.scope || "ile") === "ile" && !data.islands.some((i) => i.slug === x.island)) errors.push(`Institution « ${x.name} » : île inconnue`);
    if (x.scope && !INSTITUTION_SCOPES[x.scope]) errors.push(`Institution « ${x.name} » : portée inconnue`);
    if (!INSTITUTION_CATEGORIES[x.category]) errors.push(`Institution « ${x.name} » : domaine inconnu`);
    if (!INSTITUTION_STATUS[x.status]) errors.push(`Institution « ${x.name} » : statut inconnu`);
  });
  if (data.institutions.some((x) => x.scope === "union") && !data.islands.some((i) => i.union_member))
    warnings.push("Des institutions sont rattachées à l'Union des Comores, mais aucune île n'est cochée « fait partie de l'Union » : elles n'apparaîtront que sur la page des quatre îles.");
  data.topics.forEach((t) => {
    unique(t.pages, `Rubrique « ${t.name} »`);
    if (reserved.includes(t.slug)) errors.push(`Rubrique « ${t.name} » : l'adresse « ${t.slug} » est réservée par le site`);
  });
  for (const id of allEntityIds(data)) {
    const e = getEntity(data, id);
    const label = `${typeLabel(id)} « ${e.name || e.slug} »`;
    if (!e.name) errors.push(`${label} : titre manquant`);
    for (const f of schemaOf(id)) {
      if (f.type === "media") needMedia(e[f.key], `${label} (${f.label})`, !f.required);
      if (f.type === "medialist") (e[f.key] || []).forEach((k) => needMedia(k, `${label} (${f.label})`));
      if (f.type === "list") (e[f.key] || []).forEach((item) => (f.fields || []).forEach((sf) => {
        if (sf.type === "media") needMedia(item[sf.key], `${label} (${f.label})`, true);
      }));
    }
  }
  data.places.forEach((p) => { if (!data.islands.some((i) => i.slug === p.island)) errors.push(`Lieu « ${p.name} » : île inconnue`); });
  needMedia(data.home.hero, "Accueil (image principale)");
  (data.home.features || []).forEach((f) => needMedia(f.media, "Accueil (blocs mis en avant)"));
  (data.home.gallery || []).forEach((k) => needMedia(k, "Accueil (mosaïque)"));
  Object.entries(data.pages).forEach(([k, pg]) => { if (pg.hero) needMedia(pg.hero, `Page « ${FIXED[k] ? FIXED[k].label : k} »`); });
  Object.entries(media).forEach(([k, m]) => { if (!m.file && !m.src) errors.push(`Média « ${k} » : aucun fichier`); });
  data.quizzes.forEach((quiz) => {
    if (!(quiz.questions || []).length) errors.push(`Quiz « ${quiz.name} » : aucune question`);
    (quiz.questions || []).forEach((q, i) => {
      if (!q.choices || q.choices.length < 2) errors.push(`Quiz « ${quiz.name} », question ${i + 1} : il faut au moins deux réponses`);
      else if (q.answer < 0 || q.answer >= q.choices.length) errors.push(`Quiz « ${quiz.name} », question ${i + 1} : la bonne réponse n'existe pas`);
    });
  });
  data.tales.forEach((t) => { if (!TALE_KINDS[t.kind]) errors.push(`Récit « ${t.name} » : genre inconnu`); });
  if (data.tales.filter((t) => t.featured && isPublished(t)).length > 4) warnings.push("Plus de 4 récits sont mis en avant : seuls les 4 premiers apparaîtront sur l'accueil.");
  // Bibliographie : identifiants uniques et références existantes
  const ids = new Set();
  data.bibliography.forEach((b, i) => {
    if (!b.id) errors.push(`Bibliographie, référence ${i + 1} : identifiant manquant`);
    else if (ids.has(b.id)) errors.push(`Bibliographie : l'identifiant « ${b.id} » est utilisé deux fois`);
    else if (!/^[a-z0-9-]+$/.test(b.id)) errors.push(`Bibliographie : l'identifiant « ${b.id} » ne doit contenir que des minuscules, chiffres et tirets`);
    ids.add(b.id);
  });
  citingPages(data).forEach((pg) => pg.refs.forEach((rid) => {
    if (!ids.has(rid)) errors.push(`« ${pg.title} » cite la référence « ${rid} », qui n'existe plus dans la bibliographie`);
  }));
  // Liens vers des pages masquées ou absentes (ils deviendront du texte simple)
  const online = new Set(sitePages(data).filter((p) => !p.hidden).map((p) => p.path));
  for (const [id, obj] of owners(data)) {
    walk(obj, (k, v) => {
      if (typeof v !== "string") return;
      const re = /\[\[([^|\]]+)\|/g;
      let m;
      while ((m = re.exec(v))) {
        const target = m[1].split("#")[0];
        if (!/^https?:|^mailto:/.test(target) && !online.has(target)) warnings.push(`« ${titleOf(data, id)} » : le lien vers « ${target} » mène à une page absente ou masquée (il s'affichera comme texte simple)`);
      }
    });
  }
  return { errors: [...new Set(errors)], warnings: [...new Set(warnings)] };
}
