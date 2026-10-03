"""Fiches « lieux » : sites incontournables de chaque île."""

PLACES = [
    # ================================================================ Grande Comore
    dict(
        slug="moroni",
        island="grande-comore",
        name="Moroni",
        kicker="Grande Comore · Capitale",
        hero="moroni_mosquee",
        coords=(-11.7022, 43.2551),
        lead="Médina de corail, mosquée blanche sur le port et marchés animés : la capitale de l'Union des Comores se visite à pied, au rythme de l'océan.",
        sections=[
            dict(title="La médina et le vieux port", html="""
<p>Le cœur historique de Moroni s'organise autour du vieux port, où les boutres déchargeaient
autrefois épices et tissus. Derrière le front de mer, la <strong>médina</strong> déroule un
dédale de ruelles bordées de maisons en pierre volcanique et en chaux, de portes en bois sculpté
et de petites mosquées de quartier. Prenez le temps de vous perdre&nbsp;: chaque coin de rue
révèle une cour, un banc de pierre où l'on discute, un enfant qui joue au <em>mraha</em>.</p>
"""),
            dict(title="Les mosquées du Vendredi", media="moroni_ancienne_mosquee", html="""
<p>L'<strong>ancienne mosquée du Vendredi</strong>, fondée au XVe siècle et dotée plus tard de
son minaret, est l'un des monuments les plus anciens de la ville. Sur le port, la grande
mosquée blanche à arcades est devenue l'image emblématique de Moroni. Les visiteurs sont en
général bien accueillis à l'extérieur&nbsp;; pour entrer, demandez l'autorisation, portez une
tenue couvrante et évitez les heures de prière.</p>
"""),
            dict(title="Marchés et artisanat", html="""
<p>Le marché de <strong>Volo Volo</strong> est le plus grand de l'île&nbsp;: fruits tropicaux,
poissons du jour, épices, savons, paniers tressés et tissus imprimés. Vous y trouverez aussi
des <em>kofia</em>, les calottes brodées portées par les hommes, et de l'essence d'ylang-ylang.
Négociez avec le sourire, c'est la règle du jeu.</p>
"""),
            dict(title="Autour de Moroni", media="itsandra", html="""
<p>À quelques minutes au nord, la plage d'<strong>Itsandra</strong>, ancienne cité royale, est le
rendez-vous des familles le week-end. Plus au sud, <strong>Iconi</strong> et sa falaise
rappellent les heures sombres des razzias venues de Madagascar au XVIIIe siècle. Moroni est
aussi le point de départ de l'ascension du [[lieux/karthala.html|Karthala]].</p>
"""),
        ],
        facts=[("Île", "Grande Comore (Ngazidja)"), ("À voir", "Médina, mosquées, Volo Volo"),
               ("Durée conseillée", "1 à 2 jours"), ("Accès", "≈ 30 min de l'aéroport de Hahaya")],
        gallery=["moroni_centre", "moroni_port", "moroni_port_2", "moroni_medina", "moroni_mosquee_2", "moroni_bord_de_mer"],
    ),
    dict(
        slug="karthala",
        island="grande-comore",
        name="Le Karthala",
        kicker="Grande Comore · Volcan",
        hero="karthala",
        coords=(-11.75, 43.38),
        lead="Un des plus vastes cratères actifs du monde, au sommet d'une île entière façonnée par le feu : l'ascension du Karthala est l'aventure ultime de l'archipel.",
        sections=[
            dict(title="Un volcan bouclier toujours actif", html="""
<p>Le Karthala domine la Grande Comore du haut de ses 2&nbsp;361&nbsp;m. C'est un volcan de type
bouclier, comme ceux d'Hawaï ou de La Réunion, dont les pentes douces s'étendent sur des
dizaines de kilomètres. Son sommet est occupé par une immense <strong>caldeira</strong> de
plusieurs kilomètres de long, composée de cratères emboîtés. Il est entré en éruption à
plusieurs reprises au cours des dernières décennies, notamment au milieu des années 2000.</p>
"""),
            dict(title="L'ascension", media="karthala_lave", html="""
<p>La montée se fait généralement depuis le village de <strong>M'vouni</strong>, au-dessus de
Moroni, ou par d'autres villages selon les itinéraires. Comptez entre six et huit heures de
marche pour atteindre le bord du cratère, avec un dénivelé de plus de 1&nbsp;800&nbsp;m. La plupart
des randonneurs bivouaquent près du sommet pour profiter du lever du soleil, puis redescendent
le lendemain.</p>
<ul>
  <li><strong>Guide&nbsp;:</strong> fortement recommandé, les sentiers sont peu balisés et le brouillard fréquent.</li>
  <li><strong>Eau&nbsp;:</strong> aucune source fiable en altitude, prévoyez au moins 4 litres par personne.</li>
  <li><strong>Équipement&nbsp;:</strong> chaussures montantes, vêtements chauds et imperméables, lampe frontale, sac de couchage.</li>
  <li><strong>Saison&nbsp;:</strong> de mai à octobre, en saison sèche.</li>
</ul>
"""),
            dict(title="Paysages traversés", html="""
<p>L'itinéraire traverse successivement champs cultivés, forêt humide où résonnent les chants
d'oiseaux endémiques, puis une lande de bruyères arborescentes avant d'atteindre un univers
minéral de scories et de lave. Au sommet, la vue embrasse toute l'île et, par temps clair, la
silhouette de Mohéli et d'Anjouan.</p>
<div class="notice"><strong>Sécurité&nbsp;:</strong> l'activité du volcan est surveillée par
l'Observatoire volcanologique du Karthala. Renseignez-vous sur le niveau d'alerte avant de
partir et ne descendez jamais dans le cratère.</div>
"""),
        ],
        facts=[("Altitude", "2 361 m"), ("Durée", "2 jours (bivouac)"), ("Difficulté", "Élevée"),
               ("Meilleure période", "Mai à octobre")],
        gallery=["karthala", "karthala_lave", "moroni_panorama"],
    ),
    dict(
        slug="nord-grande-comore",
        island="grande-comore",
        name="Mitsamiouli et le Nord",
        kicker="Grande Comore · Plages",
        hero="mitsamiouli",
        coords=(-11.385, 43.30),
        lead="Sable blanc, eaux turquoise et curiosités volcaniques : le nord de la Grande Comore concentre les plus belles plages de l'île.",
        sections=[
            dict(title="Mitsamiouli et Maloudja", html="""
<p>Ville de pêcheurs animée, <strong>Mitsamiouli</strong> est bordée d'une longue plage de sable
blanc où s'alignent les pirogues à balancier. Un peu plus loin, <strong>Maloudja</strong> offre
une anse plus sauvage, idéale pour la baignade et le snorkeling. Les fonds, riches en coraux,
sont accessibles directement depuis la plage.</p>
"""),
            dict(title="Le Trou du Prophète", html="""
<p>Cette petite baie encerclée de rochers volcaniques noirs tire son nom d'une légende selon
laquelle un prophète y aurait accosté. Le contraste entre la roche sombre, le sable clair et l'eau
cristalline en fait l'un des sites les plus photogéniques de l'île.</p>
"""),
            dict(title="Le lac Salé", html="""
<p>Près de Bangoi-Kouni, un ancien cratère abrite le <strong>lac Salé</strong>, dont l'eau
saumâtre communique avec l'océan par des failles souterraines. Le sentier qui en fait le tour
offre une vue magnifique sur la côte. Selon les traditions locales, le lac est entouré de
légendes&nbsp;; respectez les lieux et les recommandations des habitants.</p>
"""),
            dict(title="Conseils", html="""
<p>Le nord se rejoint en une heure environ depuis Moroni. Pour profiter du calme, privilégiez la
semaine. Pensez à emporter de l'eau et de la crème solaire respectueuse des récifs&nbsp;:
l'ombre est rare sur certaines plages.</p>
"""),
        ],
        facts=[("Île", "Grande Comore"), ("Distance de Moroni", "≈ 40 km"), ("À faire", "Baignade, snorkeling, balade"),
               ("Idéal pour", "Familles, détente")],
        gallery=["mitsamiouli", "itsandra", "moroni_bord_de_mer"],
    ),
    # ================================================================ Mohéli
    dict(
        slug="parc-national-moheli",
        island="moheli",
        name="Parc national de Mohéli",
        kicker="Mohéli · Aire protégée",
        hero="nioumachoua_ilots",
        coords=(-12.36, 43.72),
        lead="Îlots déserts, mangroves, herbiers et récifs : le premier parc marin des Comores est un modèle de conservation pilotée par les communautés.",
        sections=[
            dict(title="Un parc géré avec les villages", html="""
<p>Créé au début des années 2000, le parc marin de Mohéli est devenu un <strong>parc
national</strong> qui protège une grande partie du littoral sud de l'île. Sa particularité&nbsp;:
les villages riverains participent à sa gestion, définissent des zones de pêche et forment des
écoguides. Votre visite contribue directement à cette économie de la conservation.</p>
"""),
            dict(title="Les îlots de Nioumachoua", media="nioumachoua_mangrove", html="""
<p>Depuis le village de <strong>Nioumachoua</strong>, des barques rejoignent en une vingtaine de
minutes les îlots qui ferment la baie. Snorkeling au-dessus des jardins de corail, pique-nique
de poisson grillé sur le sable et baignade dans une eau d'une transparence rare&nbsp;: la journée
passe trop vite. La mangrove voisine, nurserie de nombreux poissons, se découvre à marée
haute.</p>
"""),
            dict(title="Baleines et dauphins", media="baleine", html="""
<p>De juillet à octobre, les <strong>baleines à bosse</strong> remontent du Grand Sud pour se
reproduire dans les eaux chaudes de l'archipel. Les sorties en mer depuis Nioumachoua ou
Fomboni permettent de les observer, ainsi que plusieurs espèces de dauphins présentes toute
l'année.</p>
"""),
        ],
        facts=[("Statut", "Parc national, réserve de biosphère UNESCO"), ("Village d'accès", "Nioumachoua"),
               ("À faire", "Îlots, snorkeling, baleines"), ("Meilleure période", "Mai à novembre")],
        gallery=["nioumachoua_ilots", "nioumachoua_mangrove", "baleine", "tortue_verte"],
    ),
    dict(
        slug="itsamia",
        island="moheli",
        name="Itsamia, la plage des tortues",
        kicker="Mohéli · Faune",
        hero="tortue_verte",
        coords=(-12.345, 43.875),
        lead="Chaque nuit, des tortues vertes viennent pondre sur les plages d'Itsamia. Un spectacle rare, encadré par les écoguides du village.",
        sections=[
            dict(title="Un site de ponte majeur", html="""
<p>Les plages d'<strong>Itsamia</strong>, à la pointe sud-est de Mohéli, comptent parmi les
sites de ponte de <strong>tortues vertes</strong> les plus importants de l'océan Indien
occidental. Les femelles, qui peuvent dépasser un mètre de long, reviennent pondre sur la plage
qui les a vues naître, plusieurs fois par saison.</p>
"""),
            dict(title="Comment observer la ponte", html="""
<p>L'association villageoise organise des sorties nocturnes accompagnées. Le guide repère les
tortues et vous indique quand vous approcher sans les déranger. Les règles sont simples&nbsp;:</p>
<ul>
  <li>pas de lampe blanche ni de flash, seulement une lumière rouge si le guide l'autorise&nbsp;;</li>
  <li>rester derrière la tortue, à distance, et en silence&nbsp;;</li>
  <li>ne jamais toucher les animaux ni les œufs.</li>
</ul>
"""),
            dict(title="Séjourner au village", media="v_bebe_tortue", html="""
<p>Quelques bungalows simples permettent de dormir sur place et de vivre au rythme du
village. Les revenus de l'écotourisme financent la surveillance des plages, qui a permis de
réduire fortement le braconnage. Si vous avez de la chance, vous assisterez à l'émergence des
nouveau-nés, qui filent vers l'océan à la tombée de la nuit.</p>
"""),
        ],
        facts=[("Espèce", "Tortue verte (Chelonia mydas)"), ("Période", "Toute l'année, pics variables"),
               ("Encadrement", "Écoguides du village"), ("Conseil", "Prévoir 1 à 2 nuits")],
        gallery=["tortue_verte", "tortue_ngouja", "tortue_pilote"],
    ),
    dict(
        slug="forets-et-lacs-de-moheli",
        island="moheli",
        name="Forêts et lac Dziani Boundouni",
        kicker="Mohéli · Randonnée",
        hero="roussette",
        coords=(-12.33, 43.82),
        lead="Sous la canopée de Mohéli vivent des espèces que l'on ne voit nulle part ailleurs. Randonnée vers un lac de cratère, à la rencontre des roussettes géantes.",
        sections=[
            dict(title="La forêt des crêtes", html="""
<p>La dorsale centrale de Mohéli, culminant au <strong>Mzé Koukoulé</strong> (790&nbsp;m), est
couverte d'une forêt humide parmi les mieux conservées de l'archipel. Elle abrite des oiseaux
endémiques, des caméléons, des orchidées et la <strong>roussette de Livingstone</strong>, l'une
des plus grandes chauves-souris du monde, aujourd'hui en danger critique d'extinction.</p>
"""),
            dict(title="Le lac Dziani Boundouni", html="""
<p>Niché dans un ancien cratère au sud-est de l'île, le <strong>lac Dziani Boundouni</strong>
attire oiseaux d'eau et randonneurs. Le sentier qui y mène traverse plantations, forêt et
points de vue sur la côte. Comptez une demi-journée avec un guide local.</p>
"""),
            dict(title="Le lémur mongoz", media="lemur_mongoz", html="""
<p>Mohéli et Anjouan sont, avec Madagascar, les seuls territoires où vit naturellement le
<strong>lémur mongoz</strong>. Discret, il est surtout actif au crépuscule. Observez-le sans le
nourrir&nbsp;: c'est une espèce menacée.</p>
"""),
        ],
        facts=[("Point culminant", "Mzé Koukoulé, 790 m"), ("Durée", "Demi-journée à journée"),
               ("Difficulté", "Modérée"), ("Faune", "Roussettes, lémurs, oiseaux endémiques")],
        gallery=["roussette", "roussette_2", "lemur_mongoz", "moheli_banner"],
    ),
    # ================================================================ Anjouan
    dict(
        slug="mutsamudu",
        island="anjouan",
        name="Mutsamudu",
        kicker="Anjouan · Ville historique",
        hero="mutsamudu_vue",
        coords=(-12.169, 44.398),
        lead="Une citadelle qui veille sur le port, une médina en escaliers et des palais de sultans : Mutsamudu est l'une des plus belles cités swahilies de l'océan Indien.",
        sections=[
            dict(title="La citadelle", html="""
<p>Construite à la fin du XVIIIe siècle pour protéger la ville des raids venus de la mer, la
<strong>citadelle</strong> domine Mutsamudu. Ses remparts et ses vieux canons offrent la plus
belle vue sur le port, la médina et les montagnes. Montez-y en fin d'après-midi, quand la
lumière dore les façades.</p>
"""),
            dict(title="La médina", media="mutsamudu_rue", html="""
<p>La vieille ville se parcourt à pied, par un réseau d'escaliers, de passages voûtés et de
ruelles si étroites que deux personnes s'y croisent à peine. On y découvre l'ancien palais des
sultans, des mosquées anciennes et des portes sculptées de motifs floraux, héritage des
échanges avec la côte swahilie, l'Arabie et l'Inde.</p>
"""),
            dict(title="Le port et la ville moderne", media="mutsamudu_port", html="""
<p>Le port en eau profonde fait de Mutsamudu la porte maritime d'Anjouan. C'est d'ici que
partent les bateaux vers Mohéli, la Grande Comore et Mayotte. L'aéroport de l'île se trouve à
Ouani, à quelques kilomètres.</p>
"""),
        ],
        facts=[("Île", "Anjouan (Ndzuwani)"), ("À voir", "Citadelle, médina, palais"),
               ("Durée conseillée", "1 journée"), ("Aéroport", "Ouani, ≈ 10 km")],
        gallery=["mutsamudu", "mutsamudu_vue", "mutsamudu_port", "mutsamudu_escalier", "mutsamudu_rue"],
    ),
    dict(
        slug="domoni",
        island="anjouan",
        name="Domoni",
        kicker="Anjouan · Patrimoine",
        hero="domoni",
        coords=(-12.26, 44.53),
        lead="Sur la côte est d'Anjouan, l'ancienne capitale des sultans garde sa médina, ses tombeaux et l'esprit des grandes cités marchandes.",
        sections=[
            dict(title="Une capitale ancienne", html="""
<p><strong>Domoni</strong> fut pendant des siècles l'un des centres du pouvoir à Anjouan. Sa
médina, plus calme que celle de Mutsamudu, conserve mosquées anciennes, maisons de notables et
tombeaux à coupole. La ville est intimement liée à l'histoire politique des Comores
modernes.</p>
"""),
            dict(title="Le cœlacanthe, fossile vivant", media="coelacanthe", html="""
<p>En décembre 1952, un pêcheur d'Anjouan remonte un poisson étrange&nbsp;: un
<strong>cœlacanthe</strong>, espèce que l'on croyait disparue depuis des dizaines de millions
d'années avant la découverte d'un premier spécimen en Afrique du Sud en 1938. Ce second
exemplaire confirma que les eaux profondes des Comores abritent une population de ce «&nbsp;fossile
vivant&nbsp;», devenu un symbole national.</p>
"""),
            dict(title="Alentours", html="""
<p>Depuis Domoni, la route côtière mène vers des villages de pêcheurs, des plantations
d'ylang-ylang et des vallées où coulent des cascades. Pour une immersion complète, combinez la
visite avec une nuit chez l'habitant.</p>
"""),
        ],
        facts=[("Île", "Anjouan"), ("Côte", "Est"), ("À voir", "Médina, tombeaux, mosquées"), ("Durée", "Demi-journée")],
        gallery=["domoni", "coelacanthe", "ylang_plantation"],
    ),
    dict(
        slug="lac-dzialandze-et-ntingui",
        island="anjouan",
        name="Lac Dzialandzé et mont Ntingui",
        kicker="Anjouan · Randonnée",
        hero="lemur_mongoz",
        coords=(-12.21, 44.43),
        lead="Au cœur des montagnes d'Anjouan, un lac de cratère entouré de forêt de nuages, sur les flancs du point culminant de l'île.",
        sections=[
            dict(title="Le lac Dzialandzé", html="""
<p>Perché à environ 900&nbsp;m d'altitude, le <strong>lac Dzialandzé</strong> occupe un ancien
cratère tapissé de forêt. L'atmosphère y est souvent brumeuse, presque mystique. Le sentier
d'accès, au départ des villages des hauts, grimpe à travers cultures vivrières, girofliers et
fougères arborescentes.</p>
"""),
            dict(title="Vers le mont Ntingui", html="""
<p>Les marcheurs aguerris peuvent prolonger vers le <strong>mont Ntingui</strong>, point
culminant d'Anjouan à 1&nbsp;595&nbsp;m. La montée est exigeante et nécessite un guide, mais la
vue sur l'île entière, et parfois sur Mohéli et Mayotte, récompense l'effort.</p>
"""),
            dict(title="Protéger les sources d'Anjouan", media="roussette_2", html="""
<p>Les forêts du centre de l'île alimentent les rivières qui irriguent toute l'île. Plusieurs
programmes de reboisement et de protection, dont le parc national du mont Ntingui, visent à
enrayer la déforestation. Restez sur les sentiers et confiez-vous à des guides locaux.</p>
"""),
        ],
        facts=[("Altitude du lac", "≈ 900 m"), ("Sommet", "Mont Ntingui, 1 595 m"), ("Difficulté", "Modérée à élevée"),
               ("Guide", "Indispensable")],
        gallery=["lemur_mongoz", "roussette_2", "ylang_plantation"],
    ),
    # ================================================================ Mayotte
    dict(
        slug="lagon-de-mayotte",
        island="mayotte",
        name="Le lagon de Mayotte",
        kicker="Mayotte · Parc naturel marin",
        hero="lagon_choungui",
        coords=(-12.85, 45.10),
        lead="Plus de 1 000 km² d'eaux turquoise ceinturées par une barrière de corail : le lagon de Mayotte est l'un des plus grands lagons fermés de la planète.",
        sections=[
            dict(title="Une double barrière rare", html="""
<p>Le lagon est fermé par une barrière récifale de plusieurs dizaines de kilomètres, percée de
passes où l'océan s'engouffre. Dans le sud-ouest, une <strong>double barrière</strong>, phénomène
rare à l'échelle mondiale, dessine des motifs spectaculaires visibles depuis les sommets. Tout
l'espace marin est protégé par le <strong>parc naturel marin de Mayotte</strong>.</p>
"""),
            dict(title="Plonger dans la passe en S", media="v_recif", html="""
<p>Site de plongée emblématique, la <strong>passe en S</strong> serpente à travers la barrière
et concentre une vie foisonnante&nbsp;: tortues, raies, bancs de carangues, requins de récif.
Plusieurs centres de plongée proposent baptêmes et sorties pour plongeurs confirmés.</p>
"""),
            dict(title="Baleines, dauphins et dugongs", media="dugong", html="""
<p>De juillet à octobre, les <strong>baleines à bosse</strong> viennent mettre bas et allaiter
leurs petits à l'abri du lagon. Des dauphins sont observables toute l'année. Plus discret, le
<strong>dugong</strong>, mammifère marin herbivore, y survit en très petit nombre&nbsp;: une
rencontre exceptionnelle. Les sorties en mer doivent respecter la charte d'approche des
mammifères marins.</p>
"""),
            dict(title="Îlots et bancs de sable", media="mbouzi", html="""
<p>Le lagon est parsemé d'îlots&nbsp;: <strong>M'Bouzi</strong>, réserve naturelle nationale,
<strong>Mtsamboro</strong> au nord, ou encore les célèbres <strong>îlots de sable blanc</strong>
qui n'émergent qu'à marée basse. Une journée en bateau permet de combiner observation des
mammifères marins, snorkeling et pique-nique sur un banc de sable.</p>
"""),
        ],
        facts=[("Superficie", "≈ 1 100 km²"), ("Protection", "Parc naturel marin (2010)"),
               ("Baleines", "Juillet à octobre"), ("À faire", "Plongée, kayak, sorties en mer")],
        gallery=["lagon_choungui", "lagon_dembeni", "lagon_mbouzi", "mbouzi", "dugong", "barriere_choungui", "tortue_pilote"],
    ),
    dict(
        slug="petite-terre-et-lac-dziani",
        island="mayotte",
        name="Petite-Terre et le lac Dziani",
        kicker="Mayotte · Volcan",
        hero="dziani",
        coords=(-12.770, 45.290),
        lead="Un lac émeraude au fond d'un cratère, une plage de ponte des tortues et le vieux rocher de Dzaoudzi : Petite-Terre se découvre en une journée inoubliable.",
        sections=[
            dict(title="Le lac Dziani", html="""
<p>Le <strong>lac Dziani</strong> (ou Dziani Dzaha) occupe un cratère d'explosion de forme
presque circulaire. Ses eaux alcalines, colorées par des micro-organismes, prennent une teinte
vert émeraude unique. Un sentier fait le tour du cratère&nbsp;: comptez environ une heure de
marche, de préférence tôt le matin ou en fin de journée. La baignade y est déconseillée.</p>
"""),
            dict(title="La plage de Moya", media="tortue_verte", html="""
<p>Nichée au pied des falaises, la plage de <strong>Moya</strong> est l'un des principaux sites
de ponte des tortues de Mayotte. Les observations nocturnes se font uniquement dans le respect
des consignes des associations locales. De jour, c'est un lieu de baignade apprécié, à aborder
avec prudence selon l'état de la mer.</p>
"""),
            dict(title="Dzaoudzi et la barge", media="barge", html="""
<p>Ancien chef-lieu de l'île, <strong>Dzaoudzi</strong> occupe un rocher relié à Pamandzi par
une digue. On y voit des bâtiments de l'époque coloniale et le quai de la <strong>barge</strong>
qui assure, en une vingtaine de minutes, la traversée vers Mamoudzou. L'aéroport international
de Mayotte se trouve à Pamandzi.</p>
"""),
            dict(title="Un volcan sous-marin tout proche", html="""
<p>Depuis 2018, Mayotte est au centre d'une activité sismique et volcanique remarquable&nbsp;:
un nouveau volcan sous-marin, baptisé <strong>Fani Maoré</strong>, est apparu à une
cinquantaine de kilomètres à l'est de Petite-Terre. Il est étroitement surveillé par les
scientifiques et ne présente pas de danger pour les visiteurs à terre.</p>
"""),
        ],
        facts=[("Accès", "Barge depuis Mamoudzou"), ("Tour du lac", "≈ 1 h de marche"),
               ("À voir", "Lac Dziani, plage de Moya, Dzaoudzi"), ("Aéroport", "Pamandzi (DZA)")],
        gallery=["dziani", "dziani_aerien", "dziani_2", "dzaoudzi", "barge"],
    ),
    dict(
        slug="ngouja",
        island="mayotte",
        name="La plage de N'Gouja",
        kicker="Mayotte · Snorkeling",
        hero="ngouja",
        coords=(-12.96, 45.08),
        lead="Nager au-dessus des herbiers aux côtés des tortues vertes : à N'Gouja, la rencontre se fait à quelques brasses du rivage.",
        sections=[
            dict(title="Le rendez-vous des tortues", media="tortue_ngouja", html="""
<p>Dans le sud de Grande-Terre, près de Kani-Kéli, la plage de <strong>N'Gouja</strong> est
réputée pour ses <strong>tortues vertes</strong> qui viennent brouter les herbiers marins à
faible profondeur. Avec un simple masque et un tuba, il est fréquent de nager à quelques
mètres de ces reptiles paisibles.</p>
"""),
            dict(title="Bonnes pratiques", html="""
<ul>
  <li>Gardez une distance d'au moins trois mètres et ne coupez jamais la route d'une tortue qui remonte respirer.</li>
  <li>Ne touchez ni les animaux ni les coraux&nbsp;; évitez de vous tenir debout sur les herbiers.</li>
  <li>Utilisez une protection solaire respectueuse des récifs ou, mieux, un lycra.</li>
  <li>Ramenez tous vos déchets.</li>
</ul>
"""),
            dict(title="Aux alentours", media="choungui_2", html="""
<p>N'Gouja se situe au pied du [[lieux/mont-choungui.html|mont Choungui]]&nbsp;: combinez
randonnée matinale et snorkeling l'après-midi. Plus à l'est, la pointe de
<strong>Saziley</strong> offre sentiers côtiers, plages sauvages et sites de ponte.</p>
"""),
        ],
        facts=[("Localisation", "Sud de Grande-Terre, Kani-Kéli"), ("Équipement", "Masque, tuba, palmes"),
               ("Idéal pour", "Familles, snorkeling"), ("Conseil", "Venir à marée haute")],
        gallery=["ngouja", "ngouja_2", "tortue_ngouja", "tortue_pilote"],
    ),
    dict(
        slug="mont-choungui",
        island="mayotte",
        name="Le mont Choungui",
        kicker="Mayotte · Randonnée",
        hero="choungui",
        coords=(-12.947, 45.134),
        lead="Un pain de sucre volcanique qui se dresse au-dessus du lagon : l'ascension la plus emblématique de Mayotte.",
        sections=[
            dict(title="L'ascension", html="""
<p>Avec ses 594&nbsp;m, le <strong>mont Choungui</strong> n'est pas le plus haut sommet de l'île
(c'est le mont Bénara, 660&nbsp;m), mais c'est de loin le plus spectaculaire. Le sentier part du
col au-dessus du village de Choungui&nbsp;; la montée, d'environ 1&nbsp;h&nbsp;30, devient très
raide sur la fin. Des cordes facilitent parfois le passage des sections les plus pentues.</p>
"""),
            dict(title="Le panorama", media="barriere_choungui", html="""
<p>Au sommet, la vue à 360° embrasse le lagon, la double barrière de corail du sud-ouest, les
îlots et, par temps clair, les reliefs d'Anjouan. Partez tôt pour profiter de la fraîcheur et
d'une lumière douce.</p>
"""),
            dict(title="Conseils", html="""
<ul>
  <li>Partez au lever du jour et emportez au moins deux litres d'eau.</li>
  <li>Évitez la randonnée par temps de pluie&nbsp;: la terre devient glissante.</li>
  <li>Ne partez pas seul et informez votre hébergeur de votre itinéraire.</li>
</ul>
"""),
        ],
        facts=[("Altitude", "594 m"), ("Durée", "≈ 3 h aller-retour"), ("Difficulté", "Soutenue"),
               ("Meilleur moment", "Lever du soleil")],
        gallery=["choungui", "choungui_2", "lagon_choungui", "barriere_choungui"],
    ),
    dict(
        slug="mamoudzou-et-tsingoni",
        island="mayotte",
        name="Mamoudzou et Tsingoni",
        kicker="Mayotte · Ville & patrimoine",
        hero="mamoudzou",
        coords=(-12.78, 45.23),
        lead="La ville la plus animée de Mayotte et, à l'ouest, la plus ancienne mosquée en activité du territoire français.",
        sections=[
            dict(title="Mamoudzou", html="""
<p>Principale ville et pôle économique de l'île, <strong>Mamoudzou</strong> s'étire le long du
lagon. On y vient pour son <strong>marché couvert</strong>, ses étals d'épices, de vanille et
de <em>salouva</em> (le pagne traditionnel des Mahoraises), et pour son front de mer d'où part
la barge. Le soir, les brochettes et <em>mabawa</em> (ailes de poulet grillées) se dégustent
sur le pouce.</p>
"""),
            dict(title="La mosquée de Tsingoni", media="mtsapere", html="""
<p>Ancienne capitale des sultans de Mayotte, <strong>Tsingoni</strong> abrite une mosquée dont
le mihrab porte une inscription de 1538. Classée monument historique, elle est considérée
comme la plus ancienne mosquée en activité de France. Les visites se font avec respect, en
dehors des heures de prière et en tenue couvrante.</p>
"""),
            dict(title="Le maki, mascotte de l'île", media="maki", html="""
<p>Partout sur l'île, des groupes de <strong>makis</strong> (lémuriens bruns) se laissent
observer dans les arbres, notamment autour des villages et des plages. Protégés, ils ne doivent
pas être nourris.</p>
"""),
        ],
        facts=[("Statut", "Chef-lieu de Mayotte"), ("À voir", "Marché, front de mer, mosquées"),
               ("Tsingoni", "≈ 30 min de Mamoudzou"), ("Mihrab", "Daté de 1538")],
        gallery=["mamoudzou", "mamoudzou_2", "mtsapere", "coucher_mamoudzou", "maki"],
    ),
]

PLACES_BY_SLUG = {p["slug"]: p for p in PLACES}
