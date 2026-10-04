"""Expériences thématiques à vivre dans l'archipel."""

EXPERIENCES = [
    dict(
        slug="nature-et-faune",
        name="Nature & faune sauvage",
        icon="leaf",
        hero="roussette",
        card="lemur_mongoz",
        lead="Cœlacanthes, roussettes géantes, lémuriens, tortues et baleines : l'archipel abrite une biodiversité unique, souvent introuvable ailleurs.",
        sections=[
            dict(title="Des espèces uniques au monde", html="""
<p>Isolées au milieu du canal du Mozambique, les Comores ont vu évoluer une faune et une flore
originales. On y recense des oiseaux endémiques propres à chaque île, des reptiles, des
papillons et des plantes que l'on ne trouve nulle part ailleurs. Les forêts d'altitude de la
Grande Comore, d'Anjouan et de Mohéli sont les derniers refuges de ces espèces.</p>
"""),
            dict(title="Le cœlacanthe, fossile vivant", media="coelacanthe", html="""
<p>Poisson aux nageoires charnues apparu il y a plus de 400 millions d'années, le
<strong>cœlacanthe</strong> vit dans les grottes sous-marines des pentes volcaniques, entre 150
et 250&nbsp;m de profondeur. Les Comores abritent la population la mieux connue de cette espèce,
protégée notamment par le parc national du Cœlacanthe, au large de la Grande Comore. Impossible
à observer en plongée loisir, il reste le grand symbole naturel du pays.</p>
"""),
            dict(title="Roussettes et lémuriens", media="lemur_mongoz", html="""
<p>La <strong>roussette de Livingstone</strong>, chauve-souris frugivore dont l'envergure peut
dépasser 1,40&nbsp;m, ne vit qu'à Anjouan et à Mohéli. Le <strong>lémur mongoz</strong> partage
ces deux îles avec Madagascar, tandis que Mayotte abrite son propre <strong>maki</strong>, un
lémurien brun facile à observer. Tous sont protégés.</p>
"""),
            dict(title="Où observer la faune ?", html="""
<ul>
  <li><strong>Tortues&nbsp;:</strong> [[lieux/itsamia.html|Itsamia]] (Mohéli), [[lieux/ngouja.html|N'Gouja]] et Moya (Mayotte).</li>
  <li><strong>Baleines à bosse&nbsp;:</strong> de juillet à octobre, autour de toutes les îles, en particulier dans le [[lieux/lagon-de-mayotte.html|lagon de Mayotte]] et le [[lieux/parc-national-moheli.html|parc de Mohéli]].</li>
  <li><strong>Roussettes et lémurs&nbsp;:</strong> forêts de [[lieux/forets-et-lacs-de-moheli.html|Mohéli]] et d'[[lieux/lac-dzialandze-et-ntingui.html|Anjouan]].</li>
  <li><strong>Makis&nbsp;:</strong> un peu partout à Mayotte, notamment autour des plages.</li>
</ul>
"""),
        ],
        places=["itsamia", "forets-et-lacs-de-moheli", "lagon-de-mayotte", "ngouja"],
        gallery=["coelacanthe", "roussette", "roussette_2", "lemur_mongoz", "maki", "tortue_ngouja", "baleine", "dugong"],
    ),
    dict(
        slug="plages-et-lagons",
        name="Plages & lagons",
        icon="sun",
        hero="ngouja_2",
        card="itsandra",
        lead="Sable blanc ou sable noir volcanique, criques secrètes, îlots déserts et lagon turquoise : chaque île a sa manière d'aimer la mer.",
        sections=[
            dict(title="Grande Comore : le contraste du sable et de la lave", media="mitsamiouli", html="""
<p>Les plus belles plages de Ngazidja se trouvent au nord&nbsp;: <strong>Mitsamiouli</strong>,
<strong>Maloudja</strong>, le <strong>Trou du Prophète</strong>. Près de Moroni,
<strong>Itsandra</strong> est la plage des familles. À l'est, <strong>Chomoni</strong> séduit par
son sable clair encadré de roches noires.</p>
"""),
            dict(title="Mohéli : les îlots déserts", media="nioumachoua_ilots", html="""
<p>À Mohéli, la plage se vit en mode Robinson&nbsp;: une barque, un îlot rien que pour vous à
Nioumachoua, et un poisson grillé sur le sable. Les plages d'Itsamia sont, elles, réservées aux
tortues la nuit.</p>
"""),
            dict(title="Anjouan : plages du sud", html="""
<p>Plus montagneuse, Anjouan compte moins de plages, mais celles de <strong>Moya</strong> et de la
presqu'île de <strong>Bimbini</strong> valent le détour pour leurs eaux claires et leur
tranquillité.</p>
"""),
            dict(title="Mayotte : le lagon dans toute sa splendeur", media="tahiti_plage", html="""
<p>Autour du lagon, les plages se succèdent&nbsp;: <strong>N'Gouja</strong> et ses tortues,
<strong>Sakouli</strong>, <strong>Tahiti Plage</strong>, <strong>Soulou</strong> et sa cascade,
<strong>Moya</strong> sur Petite-Terre, et les fameux îlots de sable blanc qui apparaissent à
marée basse.</p>
"""),
            dict(title="Se baigner en sécurité", html="""
<ul>
  <li>Renseignez-vous sur les courants, en particulier près des passes et des pointes.</li>
  <li>Protégez-vous du soleil&nbsp;: il est très intense sous ces latitudes.</li>
  <li>Dans les villages, la tenue de plage reste réservée à la plage&nbsp;: couvrez-vous pour circuler.</li>
</ul>
"""),
        ],
        places=["nord-grande-comore", "parc-national-moheli", "ngouja", "lagon-de-mayotte"],
        gallery=["itsandra", "mitsamiouli", "nioumachoua_ilots", "ngouja", "tahiti_plage", "tahiti_plage_2", "soulou", "hamouro", "plage_prefet"],
    ),
    dict(
        slug="plongee-et-ocean",
        name="Plongée & océan",
        icon="wave",
        hero="tortue_pilote",
        card="tortue_pilote",
        lead="Passes coralliennes, tombants volcaniques, baleines à bosse et tortues : les fonds de l'archipel comptent parmi les plus préservés de l'océan Indien.",
        sections=[
            dict(title="Plonger aux Comores", html="""
<p>Autour de la Grande Comore, les tombants volcaniques plongent rapidement dans le bleu et
attirent une faune pélagique. À Mohéli, le parc national offre des jardins de corail peu
fréquentés. À Mayotte, le lagon et ses passes, dont la célèbre <strong>passe en S</strong>,
permettent des plongées pour tous les niveaux.</p>
"""),
            dict(title="La saison des baleines", media="baleine", html="""
<p>Chaque année, de <strong>juillet à octobre</strong>, des baleines à bosse rejoignent les
eaux chaudes de l'archipel pour s'accoupler et mettre bas. Sauts, coups de nageoire et chants
sous-marins&nbsp;: l'observation depuis un bateau est un moment d'émotion intense. Choisissez un
opérateur qui respecte les règles d'approche (distance, vitesse réduite, durée limitée).</p>
"""),
            dict(title="Snorkeling", media="v_recif", html="""
<p>Pas besoin d'être plongeur&nbsp;: masque et tuba suffisent pour découvrir coraux, poissons
perroquets, poissons-clowns et tortues à N'Gouja, Maloudja ou autour des îlots de
Nioumachoua.</p>
"""),
            dict(title="Plonger responsable", html="""
<ul>
  <li>Ne touchez rien, ne prélevez rien&nbsp;: coquillages et coraux sont protégés.</li>
  <li>Maîtrisez votre flottabilité pour ne pas abîmer les récifs.</li>
  <li>Choisissez des centres agréés, qui contrôlent leur matériel et briefent sur la sécurité.</li>
  <li>Respectez un délai de 24&nbsp;h entre votre dernière plongée et un vol.</li>
</ul>
"""),
        ],
        places=["lagon-de-mayotte", "parc-national-moheli", "ngouja", "nord-grande-comore"],
        gallery=["tortue_pilote", "tortue_ngouja", "baleine", "dugong", "lagon_mbouzi", "barriere_choungui"],
    ),
    dict(
        slug="randonnees-et-volcans",
        name="Randonnées & volcans",
        icon="mountain",
        hero="karthala",
        card="choungui",
        lead="Du cratère géant du Karthala au pic du Choungui, en passant par les forêts de nuages d'Anjouan : l'archipel est un terrain de jeu pour les marcheurs.",
        sections=[
            dict(title="Les grandes ascensions", html="""
<ul>
  <li><strong>[[lieux/karthala.html|Karthala]] (2&nbsp;361&nbsp;m)&nbsp;:</strong> deux jours, bivouac, l'aventure ultime.</li>
  <li><strong>[[lieux/lac-dzialandze-et-ntingui.html|Mont Ntingui]] (1&nbsp;595&nbsp;m)&nbsp;:</strong> forêt de nuages et lac de cratère au cœur d'Anjouan.</li>
  <li><strong>[[lieux/mont-choungui.html|Mont Choungui]] (594&nbsp;m)&nbsp;:</strong> le belvédère sur le lagon de Mayotte.</li>
  <li><strong>Mont Bénara (660&nbsp;m)&nbsp;:</strong> le toit de Mayotte, au cœur des réserves forestières.</li>
  <li><strong>Crêtes de Mohéli&nbsp;:</strong> randonnées douces vers le [[lieux/forets-et-lacs-de-moheli.html|lac Dziani Boundouni]].</li>
</ul>
"""),
            dict(title="Paysages volcaniques", media="dziani", html="""
<p>Coulées de lave récentes en Grande Comore, lacs de cratère à Anjouan, Mohéli et Petite-Terre,
pitons et planèzes&nbsp;: l'archipel est un livre ouvert de géologie. Les îles sont d'autant plus
anciennes qu'elles sont à l'est&nbsp;: la Grande Comore est la plus jeune, Mayotte la plus
ancienne.</p>
"""),
            dict(title="Partir bien préparé", html="""
<ul>
  <li>Faites appel à un guide local, surtout pour le Karthala et le Ntingui.</li>
  <li>Partez tôt&nbsp;: la chaleur et les nuages s'installent souvent dès la fin de matinée.</li>
  <li>Emportez beaucoup d'eau, une protection contre la pluie et une lampe frontale.</li>
  <li>Privilégiez la saison sèche, de mai à octobre.</li>
</ul>
"""),
        ],
        places=["karthala", "lac-dzialandze-et-ntingui", "mont-choungui", "forets-et-lacs-de-moheli"],
        gallery=["karthala", "karthala_lave", "choungui", "choungui_2", "dziani", "barriere_choungui"],
    ),
    dict(
        slug="medinas-et-patrimoine",
        name="Médinas & patrimoine",
        icon="dome",
        hero="moroni_ancienne_mosquee",
        card="mutsamudu_escalier",
        lead="Flâner dans les médinas, visiter mosquées anciennes, citadelles et musées : un voyage dans mille ans d'histoire swahilie.",
        sections=[
            dict(title="Les médinas à parcourir à pied", html="""
<p>Les vieilles villes de [[lieux/moroni.html|Moroni]], [[lieux/mutsamudu.html|Mutsamudu]] et
[[lieux/domoni.html|Domoni]] se découvrent à pied, en se laissant guider par les ruelles, les
escaliers de pierre et les passages couverts. Levez les yeux vers les portes sculptées et les
moucharabiehs, entrez dans les cours quand on vous y invite, et prenez le temps d'un thé sur une
place ombragée.</p>
"""),
            dict(title="Mosquées et lieux de mémoire", media="moroni_mosquee", html="""
<ul>
  <li><strong>Ancienne mosquée du Vendredi de Moroni</strong>, fondée au XVe siècle.</li>
  <li><strong>Mosquée de Tsingoni</strong> à Mayotte, dont le mihrab est daté de 1538.</li>
  <li><strong>Citadelle de Mutsamudu</strong>, bâtie à la fin du XVIIIe siècle contre les razzias.</li>
  <li><strong>Remparts de [[lieux/ntsaoueni.html|Ntsaoueni]]</strong> et falaise d'[[lieux/iconi.html|Iconi]], en Grande Comore.</li>
  <li><strong>Rocher de Dzaoudzi</strong>, ancien siège de l'administration coloniale à Mayotte.</li>
</ul>
<p>Pour visiter une mosquée, demandez l'autorisation, portez une tenue couvrante et évitez les
heures de prière.</p>
"""),
            dict(title="Musées et centres culturels", media="manzaraka", html="""
<p>Le <strong>Centre national de documentation et de recherche scientifique</strong> (CNDRS), à
Moroni, et le <strong>musée de Mayotte</strong>, à Dzaoudzi, présentent l'histoire, l'archéologie,
les traditions et la nature de l'archipel. Une bonne introduction avant de partir sur le
terrain.</p>
"""),
            dict(title="Pour aller plus loin", html="""
<p>Découvrez notre rubrique [[histoire/index.html|Histoire]] et notre rubrique
[[culture/index.html|Culture &amp; folklore]] pour comprendre ce que vous verrez.</p>
"""),
        ],
        places=["moroni", "mutsamudu", "domoni", "iconi", "ntsaoueni", "mamoudzou-et-tsingoni"],
        gallery=["moroni_ancienne_mosquee", "moroni_mosquee", "moroni_medina", "mutsamudu_escalier", "mutsamudu_rue", "domoni", "ntsaoueni_rempart", "residence_gouverneur"],
    ),
    dict(
        slug="route-des-parfums",
        name="Route des parfums",
        icon="flower",
        hero="ylang",
        card="ylang_plantation",
        lead="Ylang-ylang, vanille, girofle : partez à la découverte des « îles aux parfums », des plantations aux alambics traditionnels.",
        sections=[
            dict(title="L'ylang-ylang, or jaune des Comores", html="""
<p>L'<strong>ylang-ylang</strong> (<em>Cananga odorata</em>) est un arbre dont les fleurs jaunes
dégagent un parfum puissant, très recherché par la parfumerie. Les Comores, et en particulier
Anjouan, comptent parmi les principaux producteurs mondiaux de son huile essentielle. Les arbres
sont taillés bas pour faciliter la cueillette, qui se fait à la main, tôt le matin.</p>
"""),
            dict(title="Visiter une distillerie", media="ylang_plantation", html="""
<p>Les fleurs sont distillées à la vapeur dans des alambics souvent artisanaux. La distillation
dure de longues heures et l'essence est recueillie par fractions successives, des plus fines
aux plus lourdes. De nombreux producteurs acceptent de montrer leur travail&nbsp;: demandez à
votre hébergeur de vous mettre en relation.</p>
"""),
            dict(title="Vanille et girofle", html="""
<p>Sous les arbres, les lianes de <strong>vanille</strong> sont pollinisées à la main, fleur par
fleur. Les gousses sont ensuite échaudées, étuvées et séchées au soleil pendant des semaines.
Le <strong>giroflier</strong>, lui, embaume les routes au moment du séchage des clous sur des
nattes, devant les maisons.</p>
"""),
            dict(title="Rapporter des souvenirs", html="""
<p>Huile essentielle d'ylang-ylang, gousses de vanille, clous de girofle, savons et
cosmétiques artisanaux&nbsp;: achetez auprès des producteurs ou des coopératives pour garantir
qualité et juste rémunération. Vérifiez les règles d'importation de votre pays de retour.</p>
"""),
        ],
        places=["mutsamudu", "domoni"],
        gallery=["ylang", "ylang_plantation", "domoni", "mutsamudu"],
    ),
]

EXPERIENCES_BY_SLUG = {e["slug"]: e for e in EXPERIENCES}
