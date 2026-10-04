"""Rubrique Géographie : relief, climat, océan, nature, population."""

GEOGRAPHIE = dict(
    slug="geographie",
    name="Géographie",
    icon="globe",
    hero="lagon_choungui",
    card="karthala",
    lead=(
        "Quatre volcans sortis de l'océan Indien, posés à l'entrée nord du canal du Mozambique. "
        "Relief, climat, océan, faune, flore et population : comprendre l'archipel par ses paysages."
    ),
    intro="""
<p>L'archipel des Comores s'étire sur environ 300&nbsp;km, du nord-ouest au sud-est, à mi-chemin
entre la côte du Mozambique et la pointe nord de Madagascar. Ses quatre îles principales, la
<strong>Grande Comore</strong>, <strong>Mohéli</strong>, <strong>Anjouan</strong> et
<strong>Mayotte</strong>, sont accompagnées d'une multitude d'îlots. Toutes sont d'origine
volcanique, mais chacune raconte une étape différente de la vie d'une île&nbsp;: la naissance au
nord-ouest, la vieillesse au sud-est.</p>
""",
    facts=[
        ("Situation", "Canal du Mozambique, océan Indien"),
        ("Coordonnées", "≈ 11° à 13° sud, 43° à 45° est"),
        ("Superficie totale", "≈ 2 030 km² (4 îles)"),
        ("Point culminant", "Karthala, 2 361 m"),
        ("Climat", "Tropical maritime"),
        ("Fuseau horaire", "UTC+3"),
    ],
    pages=[
        dict(
            slug="volcans-et-reliefs",
            name="Volcans & reliefs",
            icon="mountain",
            hero="karthala",
            lead="Des îles nées du feu, dont l'âge diminue d'est en ouest : de Mayotte l'ancienne à la Grande Comore, encore en pleine croissance.",
            sections=[
                dict(title="Un archipel volcanique", html="""
<p>Les Comores sont des îles <strong>volcaniques</strong> nées de remontées de magma à travers le
plancher océanique. L'origine exacte de ce volcanisme fait encore débat chez les géologues&nbsp;:
point chaud, failles liées à l'ouverture du canal du Mozambique, ou combinaison des deux. Ce qui
est certain, c'est l'ordre de naissance des îles&nbsp;: <strong>Mayotte</strong> est la plus
ancienne, puis viennent <strong>Anjouan</strong> et <strong>Mohéli</strong>, et enfin la
<strong>Grande Comore</strong>, la plus jeune.</p>
"""),
                dict(title="Le cycle de vie d'une île", media="lagon_choungui", html="""
<p>Les quatre îles illustrent les étapes d'un même processus. La Grande Comore, jeune et encore
active, présente des pentes régulières, des coulées récentes et presque aucun cours d'eau
permanent&nbsp;: la lave poreuse absorbe la pluie. Anjouan et Mohéli, plus âgées, ont été
profondément entaillées par l'érosion, qui a creusé vallées, cirques et cascades. Mayotte, la
doyenne, s'est affaissée lentement&nbsp;: ses reliefs se sont adoucis et les coraux ont eu le temps
de construire autour d'elle un immense lagon fermé par une barrière récifale.</p>
"""),
                dict(title="Le Karthala, l'un des volcans les plus actifs de la région", media="karthala_lave", html="""
<p>Le <strong>Karthala</strong> (2&nbsp;361&nbsp;m) occupe toute la moitié sud de la Grande
Comore. C'est un volcan bouclier, comme ceux d'Hawaï ou de La Réunion, couronné d'une
<strong>caldeira</strong> de plusieurs kilomètres, l'une des plus vastes du monde pour un volcan
actif. Ses éruptions, fréquentes à l'échelle géologique, ont parfois projeté des cendres jusqu'à
Moroni, comme au milieu des années 2000. Au nord, le massif plus ancien de la
<strong>Grille</strong> est parsemé de cônes de scories.</p>
<p>[[lieux/karthala.html|Voir la fiche du Karthala →]]</p>
"""),
                dict(title="Lacs de cratère et curiosités", media="dziani", html="""
<ul>
  <li><strong>Lac Salé</strong> (Grande Comore)&nbsp;: un cratère proche de la mer, rempli d'eau saumâtre.</li>
  <li><strong>Lac Dzialandzé</strong> (Anjouan)&nbsp;: un lac d'altitude dans un cratère forestier, vers 900&nbsp;m.</li>
  <li><strong>Lac Dziani Boundouni</strong> (Mohéli)&nbsp;: un cratère lacustre fréquenté par les oiseaux d'eau.</li>
  <li><strong>Lac Dziani</strong> (Mayotte)&nbsp;: un maar de Petite-Terre aux eaux alcalines vert émeraude.</li>
</ul>
"""),
                dict(title="Fani Maoré, le volcan né en 2018", html="""
<p>En mai 2018, une série de séismes inhabituels a secoué Mayotte. Les campagnes scientifiques
menées ensuite ont révélé la naissance d'un <strong>nouveau volcan sous-marin</strong>, baptisé
<strong>Fani Maoré</strong>, à une cinquantaine de kilomètres à l'est de Petite-Terre, par plus de
3&nbsp;000&nbsp;m de fond. Il s'agit de l'une des plus importantes éruptions sous-marines jamais
observées. Ce phénomène s'est accompagné d'un léger affaissement de l'île, aujourd'hui suivi en
permanence par un réseau de surveillance.</p>
"""),
            ],
            facts=[("Plus jeune île", "Grande Comore"), ("Plus ancienne île", "Mayotte"),
                   ("Sommets", "Karthala 2 361 m · Ntingui 1 595 m · Mzé Koukoulé 790 m · Bénara 660 m"),
                   ("Volcan récent", "Fani Maoré (2018)")],
            didyouknow="La Grande Comore n'a pratiquement aucune rivière permanente : la roche volcanique, très poreuse, laisse s'infiltrer l'eau de pluie, qui ressort parfois en sources sur le littoral.",
            gallery=["karthala", "karthala_lave", "dziani_aerien", "choungui", "barriere_choungui"],
        ),
        dict(
            slug="climat-et-saisons",
            name="Climat & saisons",
            icon="sun",
            hero="itsandra",
            lead="Deux grandes saisons rythment la vie de l'archipel : le kashkazi, chaud et humide, et le kusi, frais et sec.",
            sections=[
                dict(title="Un climat tropical maritime", html="""
<p>Situé entre 11° et 13° de latitude sud, l'archipel bénéficie d'un climat <strong>tropical
maritime</strong>&nbsp;: températures chaudes toute l'année, forte humidité et contrastes marqués
selon l'altitude et l'exposition. Les versants exposés aux vents reçoivent bien plus de pluie que
les côtes abritées, et les sommets comme le Karthala ou le Ntingui sont souvent pris dans les
nuages.</p>
"""),
                dict(title="Kashkazi et kusi", html="""
<table class="table">
  <thead><tr><th>Saison</th><th>Période</th><th>Caractéristiques</th></tr></thead>
  <tbody>
    <tr><td><strong>Kashkazi</strong></td><td>Novembre à avril</td><td>Mousson de nord-ouest&nbsp;: chaleur (28 à 32&nbsp;°C), fortes pluies, orages, risque cyclonique.</td></tr>
    <tr><td><strong>Kusi</strong></td><td>Mai à octobre</td><td>Alizés de sud-est&nbsp;: temps plus sec et plus frais (23 à 28&nbsp;°C), mer parfois agitée.</td></tr>
  </tbody>
</table>
<p>Ces deux mots, partagés avec le swahili de la côte africaine, désignent aussi bien les vents
que les saisons. Ils ont longtemps réglé la navigation des boutres, qui profitaient de la mousson
pour relier l'Arabie, l'Afrique et Madagascar.</p>
"""),
                dict(title="Les cyclones", html="""
<p>Pendant le kashkazi, des dépressions tropicales se forment dans le sud-ouest de l'océan Indien.
L'archipel, situé en bordure de leur trajectoire habituelle, est moins souvent touché que
Madagascar ou La Réunion, mais certains épisodes ont été dévastateurs. En avril 2019, le cyclone
<strong>Kenneth</strong> a frappé la Grande Comore et Mohéli. En décembre 2024, le cyclone
<strong>Chido</strong> a ravagé Mayotte, causant d'importantes destructions.</p>
"""),
                dict(title="Quand voyager ?", html="""
<p>La saison sèche, de mai à octobre, est la plus agréable pour randonner et plonger, et coïncide
avec la présence des baleines à bosse. La saison chaude offre une végétation luxuriante et des
fruits en abondance. Voir aussi [[preparer-son-voyage/quand-partir.html|Quand partir&nbsp;?]].</p>
"""),
            ],
            facts=[("Saison chaude", "Novembre à avril (kashkazi)"), ("Saison fraîche", "Mai à octobre (kusi)"),
                   ("Température de la mer", "≈ 25 à 29 °C"), ("Risque cyclonique", "Janvier à mars surtout")],
            didyouknow="Les noms des saisons, kashkazi et kusi, sont communs à toute la côte swahilie, de la Somalie au Mozambique : ils rappellent que l'archipel a toujours vécu au rythme des moussons.",
            gallery=["itsandra", "coucher_mamoudzou", "mitsamiouli", "lagon_dembeni"],
        ),
        dict(
            slug="ocean-et-lagons",
            name="Océan, récifs & lagons",
            icon="wave",
            hero="lagon_dembeni",
            lead="Le canal du Mozambique, ses récifs coralliens et l'un des plus grands lagons fermés du monde : l'archipel vit tourné vers la mer.",
            sections=[
                dict(title="Le canal du Mozambique", html="""
<p>Les Comores ferment l'entrée nord du <strong>canal du Mozambique</strong>, bras de mer large
d'environ 400&nbsp;km qui sépare l'Afrique de Madagascar. Les eaux y sont chaudes et traversées
de tourbillons qui favorisent la remontée de nutriments. Cette richesse attire thons, dauphins,
baleines et oiseaux marins, et fait de la région l'un des foyers de biodiversité marine de
l'océan Indien occidental.</p>
"""),
                dict(title="Des récifs jeunes et des récifs anciens", media="tortue_pilote", html="""
<p>Autour de la Grande Comore, les côtes volcaniques récentes n'offrent que des récifs frangeants
étroits&nbsp;: les fonds plongent rapidement vers les abysses. À Mohéli et Anjouan, les récifs sont
plus développés. À Mayotte, l'île la plus ancienne, les coraux ont construit un véritable
<strong>lagon</strong> d'environ 1&nbsp;100&nbsp;km², fermé par une barrière longue de plus de
150&nbsp;km et doublée, au sud-ouest, d'une rare <strong>double barrière</strong>.</p>
"""),
                dict(title="Les grands hôtes de l'océan", media="baleine", html="""
<ul>
  <li><strong>Baleines à bosse</strong>&nbsp;: de juillet à octobre, elles viennent s'accoupler et mettre bas dans les eaux chaudes de l'archipel.</li>
  <li><strong>Tortues vertes et imbriquées</strong>&nbsp;: elles pondent sur de nombreuses plages, notamment à Mohéli et Mayotte.</li>
  <li><strong>Dugongs</strong>&nbsp;: ces mammifères herbivores survivent en très petit nombre dans le lagon de Mayotte.</li>
  <li><strong>Cœlacanthes</strong>&nbsp;: ces poissons «&nbsp;fossiles vivants&nbsp;» habitent les grottes des pentes volcaniques, entre 150 et 250&nbsp;m de profondeur.</li>
</ul>
"""),
                dict(title="Protéger la mer", html="""
<p>Plusieurs aires marines protégées ont été créées&nbsp;: le <strong>parc national de
Mohéli</strong>, premier parc marin des Comores, le <strong>parc national du Cœlacanthe</strong>
au large de la Grande Comore et le <strong>parc naturel marin de Mayotte</strong>, qui couvre
toute la zone économique de l'île. Elles associent souvent les pêcheurs à la gestion des
ressources.</p>
"""),
            ],
            facts=[("Lagon de Mayotte", "≈ 1 100 km²"), ("Barrière de Mayotte", "> 150 km"),
                   ("Aires marines", "Mohéli, Cœlacanthe, Mayotte"), ("Baleines", "Juillet à octobre")],
            didyouknow="La double barrière de corail de Mayotte est un phénomène rare : on n'en compte qu'une poignée dans le monde.",
            gallery=["lagon_dembeni", "lagon_mbouzi", "barriere_choungui", "dugong", "tortue_ngouja", "nioumachoua_ilots"],
        ),
        dict(
            slug="faune-et-flore",
            name="Faune & flore",
            icon="leaf",
            hero="roussette",
            lead="Isolées au milieu de l'océan, les îles ont vu naître des espèces uniques : roussettes géantes, lémuriens, oiseaux endémiques et forêts de nuages.",
            sections=[
                dict(title="Un laboratoire de l'évolution", html="""
<p>Les Comores n'ont jamais été reliées à un continent. Toutes les espèces terrestres qui y vivent
sont arrivées par la mer ou par les airs, portées par les vents, les courants ou des radeaux de
végétation. Isolées, certaines ont évolué jusqu'à former des <strong>espèces endémiques</strong>,
parfois propres à une seule île&nbsp;: oiseaux, reptiles, papillons, plantes.</p>
"""),
                dict(title="Les mammifères emblématiques", media="lemur_mongoz", html="""
<ul>
  <li><strong>Roussette de Livingstone</strong>&nbsp;: chauve-souris frugivore géante, endémique d'Anjouan et de Mohéli, classée en danger critique.</li>
  <li><strong>Autres roussettes</strong>&nbsp;: une espèce plus petite et plus répandue survole les quatre îles au crépuscule.</li>
  <li><strong>Lémur mongoz</strong>&nbsp;: présent à Anjouan et à Mohéli, ainsi qu'à Madagascar.</li>
  <li><strong>Maki de Mayotte</strong>&nbsp;: lémurien brun, symbole de l'île, probablement introduit il y a plusieurs siècles.</li>
</ul>
"""),
                dict(title="Les oiseaux", html="""
<p>Chaque île possède ses propres espèces ou sous-espèces d'oiseaux&nbsp;: drongos, souïmangas,
lunettes, petits-ducs… Le <strong>petit-duc du Karthala</strong> ne vit que dans les forêts
d'altitude du volcan, et le <strong>petit-duc d'Anjouan</strong>, longtemps cru disparu, a été
redécouvert à la fin du XXe siècle. Ces oiseaux discrets dépendent entièrement de la survie des
forêts.</p>
"""),
                dict(title="Forêts, mangroves et plantes à parfum", media="ylang", html="""
<p>Les forêts humides d'altitude, riches en fougères arborescentes, mousses et orchidées, ne
subsistent plus que sur les sommets. En bord de mer, les <strong>mangroves</strong> abritent les
jeunes poissons. Les hommes ont introduit des plantes devenues emblématiques&nbsp;:
<strong>ylang-ylang</strong>, <strong>vanillier</strong>, <strong>giroflier</strong>, cocotier,
manguier, baobab.</p>
"""),
                dict(title="Menaces et protection", html="""
<p>La croissance démographique, la déforestation et l'érosion des sols menacent les forêts et les
sources d'eau, en particulier à Anjouan. Plusieurs parcs nationaux ont été créés dans l'Union des
Comores (Karthala, mont Ntingui, Mohéli, Shisiwani, Cœlacanthe) et Mayotte compte une réserve
naturelle nationale des forêts. L'île de Mohéli est réserve de biosphère de l'UNESCO depuis 2020.</p>
"""),
            ],
            facts=[("Espèce phare", "Cœlacanthe (Latimeria chalumnae)"), ("Chauve-souris géante", "Roussette de Livingstone"),
                   ("Lémuriens", "Mongoz (Anjouan, Mohéli), maki (Mayotte)"), ("Réserve de biosphère", "Mohéli (UNESCO, 2020)")],
            didyouknow="Le cœlacanthe, apparu il y a plus de 400 millions d'années, était connu uniquement par des fossiles avant 1938. Les Comores abritent sa population la mieux étudiée.",
            gallery=["coelacanthe", "roussette", "roussette_2", "lemur_mongoz", "maki", "ylang", "ylang_plantation", "nioumachoua_mangrove"],
        ),
        dict(
            slug="population-et-territoires",
            name="Population & territoires",
            icon="people",
            hero="moroni_panorama",
            lead="Un peuple, deux statuts : l'Union des Comores et le département de Mayotte partagent une langue, une religion et des familles.",
            sections=[
                dict(title="Deux entités politiques", html="""
<table class="table">
  <thead><tr><th></th><th>Union des Comores</th><th>Mayotte</th></tr></thead>
  <tbody>
    <tr><th>Îles</th><td>Grande Comore, Mohéli, Anjouan</td><td>Grande-Terre, Petite-Terre et îlots</td></tr>
    <tr><th>Statut</th><td>État indépendant depuis 1975</td><td>Département français depuis 2011</td></tr>
    <tr><th>Capitale / chef-lieu</th><td>Moroni</td><td>Mamoudzou</td></tr>
    <tr><th>Monnaie</th><td>Franc comorien (KMF)</td><td>Euro</td></tr>
    <tr><th>Langues officielles</th><td>Comorien, français, arabe</td><td>Français</td></tr>
  </tbody>
</table>
<p>L'Union des Comores revendique la souveraineté sur Mayotte. Cette question, débattue depuis
l'indépendance, fait l'objet de positions divergentes entre les deux pays.</p>
"""),
                dict(title="Une population jeune et dense", media="moroni_medina", html="""
<p>L'archipel compte au total un peu plus d'un million d'habitants&nbsp;: environ 850&nbsp;000 dans
l'Union des Comores et plus de 300&nbsp;000 à Mayotte selon les estimations récentes. Les
densités sont parmi les plus élevées d'Afrique, en particulier à Anjouan. La population est très
jeune&nbsp;: près de la moitié des habitants a moins de vingt ans.</p>
"""),
                dict(title="Villes et villages", html="""
<p>Les principales villes sont <strong>Moroni</strong> (Grande Comore), <strong>Mutsamudu</strong>
(Anjouan), <strong>Fomboni</strong> (Mohéli) et <strong>Mamoudzou</strong> (Mayotte). Mais la vie
sociale s'organise d'abord autour du <strong>village</strong>, avec sa mosquée, sa place publique
et ses notables. Chacun reste attaché à son village d'origine, même après des années passées à
l'étranger.</p>
"""),
                dict(title="La diaspora", html="""
<p>Une importante <strong>diaspora</strong> vit hors de l'archipel, en France métropolitaine
(Marseille est souvent présentée comme la «&nbsp;cinquième île&nbsp;»), à La Réunion, à Mayotte,
en Afrique de l'Est et dans le Golfe. Ses transferts d'argent jouent un rôle majeur dans
l'économie, et son retour estival rythme la saison des grands mariages.</p>
"""),
                dict(title="Économie", html="""
<p>L'agriculture vivrière (manioc, bananes, fruit à pain, riz), la pêche artisanale et les
cultures d'exportation (<strong>ylang-ylang</strong>, <strong>vanille</strong>,
<strong>girofle</strong>) restent essentielles dans l'Union des Comores. À Mayotte, l'économie
repose largement sur les services publics, le commerce et le BTP. Le tourisme, encore modeste,
offre un fort potentiel grâce aux paysages et à la culture de l'archipel.</p>
"""),
            ],
            facts=[("Habitants (archipel)", "≈ 1,1 à 1,2 million"), ("Union des Comores", "≈ 850 000 hab."),
                   ("Mayotte", "> 300 000 hab."), ("Religion", "Islam sunnite (rite chaféite)")],
            didyouknow="Marseille est parfois surnommée la « cinquième île » des Comores, tant la communauté comorienne y est nombreuse.",
            gallery=["moroni_panorama", "mutsamudu_vue", "mamoudzou", "fomboni", "marche_tissus"],
        ),
    ],
)
