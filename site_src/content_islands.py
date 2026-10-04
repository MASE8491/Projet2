"""Les quatre îles de l'archipel des Comores.

Syntaxe des liens internes dans les textes : [[chemin/page.html|libellé]].
"""

ISLANDS = [
    dict(
        slug="grande-comore",
        name="Grande Comore",
        local="Ngazidja",
        tagline="L'île du volcan",
        status="Union des Comores",
        chef_lieu="Moroni",
        area="≈ 1 025 km²",
        summit="Karthala, 2 361 m",
        accent="#c65a3a",
        hero="moroni_panorama",
        card="moroni_centre",
        map=(-11.65, 43.33, 10),
        lead=(
            "La plus vaste et la plus jeune des quatre îles vit au rythme de son volcan, "
            "le Karthala. Entre coulées de lave noire, criques de sable blanc et médinas "
            "aux portes sculptées, Ngazidja est le cœur battant de l'archipel."
        ),
        intro="""
<p>Vue du ciel, la Grande Comore ressemble à une vaste coulée figée dans l'océan. L'île est
née des éruptions successives du <strong>Karthala</strong>, qui occupe toute sa moitié sud, et
du massif plus ancien de la Grille au nord. Le relief y est jeune&nbsp;: peu de rivières, des
champs de lave couverts de lichens, des forêts d'altitude et un littoral déchiqueté où le basalte
plonge directement dans l'eau bleu nuit.</p>
<p>C'est aussi l'île la plus peuplée et la plus urbaine de l'Union. <strong>Moroni</strong>, la
capitale, garde dans sa médina la mémoire des cités swahilies et des sultanats qui se
partageaient autrefois l'île. Chaque été, la diaspora revient célébrer les <em>grands
mariages</em>, et les villages s'emplissent de musique, de tissus brodés et de parfums de
jasmin.</p>
""",
        sections=[
            dict(title="Moroni, la ville au croissant de lune", media="moroni_centre", html="""
<p>Son nom signifierait «&nbsp;au cœur du feu&nbsp;», et la ville porte bien la trace du volcan
voisin. On y flâne entre le vieux port, la blanche <strong>mosquée du Vendredi</strong> à
arcades et les ruelles de la médina, où les maisons de corail et de chaux se serrent autour de
petites places. Le marché de Volo Volo, bruyant et coloré, est l'endroit idéal pour goûter aux
fruits de saison et repérer vanille, clous de girofle et tissus.</p>
<p>[[lieux/moroni.html|Découvrir Moroni en détail →]]</p>
"""),
            dict(title="Le Karthala, géant actif", media="karthala", html="""
<p>Culminant à 2&nbsp;361&nbsp;m, le Karthala est l'un des volcans les plus actifs de l'océan
Indien. Sa caldeira sommitale, longue de plusieurs kilomètres, figure parmi les plus vastes
cratères actifs du globe. Son ascension, qui se fait généralement en deux jours avec un guide,
traverse forêts de bruyères arborescentes et paysages lunaires avant d'atteindre le bord du
cratère.</p>
<p>[[lieux/karthala.html|Préparer l'ascension du Karthala →]]</p>
"""),
            dict(title="Le Nord : sable blanc et lac salé", media="mitsamiouli", html="""
<p>Contrairement au sud volcanique, le nord de l'île offre quelques-unes des plus belles plages
de l'archipel. <strong>Mitsamiouli</strong>, <strong>Maloudja</strong> et leurs criques bordées de
cocotiers alternent avec des curiosités géologiques comme le <strong>Trou du Prophète</strong>,
anse cernée de roches noires, ou le <strong>lac Salé</strong>, un cratère rempli d'eau
saumâtre à deux pas de l'océan.</p>
<p>[[lieux/nord-grande-comore.html|Explorer le Nord de la Grande Comore →]]</p>
"""),
            dict(title="Iconi, Chindini et le Sud", media="karthala_lave", html="""
<p>Ancienne capitale de sultanat, <strong>Iconi</strong> se dresse au pied d'une falaise chargée
d'histoire. Plus au sud, la région du Badjini, plus sèche et plus rurale, mène jusqu'à la plage
de <strong>Chindini</strong>, d'où l'on aperçoit par temps clair la silhouette de Mohéli. Les
coulées de lave du Karthala y dessinent un littoral sauvage, idéal pour les road-trips.</p>
"""),
            dict(title="Le grand mariage, cœur de la vie sociale", media="moroni_medina", html="""
<p>Institution unique au monde, le <em>anda</em> ou grand mariage marque l'entrée d'un homme
dans le cercle des notables de son village. Les festivités peuvent durer plusieurs jours&nbsp;:
cortèges, danses, chants et repas partagés par des centaines d'invités. Si vous êtes convié,
acceptez&nbsp;: c'est l'une des plus belles portes d'entrée dans la culture comorienne.</p>
<p>[[experiences/culture-et-patrimoine.html|Culture et patrimoine des Comores →]]</p>
"""),
        ],
        places=["moroni", "karthala", "nord-grande-comore"],
        gallery=["moroni_panorama", "moroni_mosquee", "moroni_ancienne_mosquee", "moroni_port",
                 "itsandra", "karthala", "karthala_lave", "mitsamiouli", "moroni_medina",
                 "moroni_port_2", "moroni_mosquee_2", "moroni_bord_de_mer"],
        tips=[
            "L'aéroport international Prince Saïd Ibrahim se trouve à Hahaya, à une vingtaine de kilomètres au nord de Moroni.",
            "Prévoyez de bonnes chaussures : les sentiers volcaniques sont abrasifs.",
            "Les plages du nord sont plus calmes en semaine qu'en fin de semaine.",
        ],
    ),
    dict(
        slug="moheli",
        name="Mohéli",
        local="Mwali",
        tagline="L'île nature",
        status="Union des Comores",
        chef_lieu="Fomboni",
        area="≈ 211 km²",
        summit="Mzé Koukoulé, 790 m",
        accent="#2f7d55",
        hero="nioumachoua_ilots",
        card="nioumachoua_ilots",
        map=(-12.32, 43.74, 11),
        lead=(
            "La plus petite et la plus sauvage des îles comoriennes. Forêts primaires, plages "
            "de ponte des tortues, îlots déserts et villages paisibles : Mohéli est une "
            "réserve de biosphère à ciel ouvert."
        ),
        intro="""
<p>On arrive à Mohéli comme on entre dans un jardin. L'île, peu peuplée, a gardé une grande
partie de ses forêts et de ses mangroves, et son littoral sud est protégé au sein du
<strong>parc national de Mohéli</strong>, le premier parc marin créé aux Comores. Depuis 2020,
l'île entière est reconnue par l'UNESCO comme <strong>réserve de biosphère</strong>, un modèle
où les villages participent directement à la protection de la nature.</p>
<p>Ici, pas de grands hôtels mais des écolodges, des bungalows chez l'habitant et des
pêcheurs prêts à vous emmener vers les îlots. C'est le lieu rêvé pour observer les tortues
vertes, croiser des baleines à bosse en saison, ou simplement ralentir.</p>
""",
        sections=[
            dict(title="Le parc national et les îlots de Nioumachoua", media="nioumachoua_ilots", html="""
<p>Face au village de <strong>Nioumachoua</strong>, un chapelet d'îlots couverts de végétation
émerge d'une eau limpide. Snorkeling sur les patates de corail, pique-nique sur une plage déserte,
observation des oiseaux marins&nbsp;: la sortie en barque vers les îlots est l'expérience
incontournable de Mohéli.</p>
<p>[[lieux/parc-national-moheli.html|Le parc national de Mohéli →]]</p>
"""),
            dict(title="Itsamia, la plage des tortues", media="tortue_verte", html="""
<p>À l'extrémité sud-est de l'île, la plage d'<strong>Itsamia</strong> accueille l'un des plus
importants sites de ponte de tortues vertes de l'océan Indien occidental. La nuit, accompagné
d'un écoguide du village, on peut assister à la ponte ou, avec un peu de chance, à l'émergence
des nouveau-nés.</p>
<p>[[lieux/itsamia.html|Observer les tortues à Itsamia →]]</p>
"""),
            dict(title="Forêts, lac de cratère et roussettes", media="roussette", html="""
<p>Les crêtes centrales abritent une forêt humide où vivent des espèces rares, dont la
<strong>roussette de Livingstone</strong>, une chauve-souris frugivore géante, et le
<strong>lémur mongoz</strong>. Au cœur de l'île, le lac de cratère de
<strong>Dziani Boundouni</strong> se découvre au terme d'une belle randonnée.</p>
<p>[[lieux/forets-et-lacs-de-moheli.html|Randonner dans les forêts de Mohéli →]]</p>
"""),
            dict(title="Fomboni et la mémoire de Djoumbé Fatima", media="djoumbe_fatima", html="""
<p>Petit chef-lieu tranquille, <strong>Fomboni</strong> garde le souvenir de la reine
<strong>Djoumbé Fatima</strong>, figure du XIXe siècle qui dut composer avec les ambitions des
puissances européennes dans le canal du Mozambique. On y trouve le port, le marché et
l'essentiel des services de l'île.</p>
"""),
        ],
        places=["parc-national-moheli", "itsamia", "forets-et-lacs-de-moheli"],
        gallery=["nioumachoua_ilots", "nioumachoua_mangrove", "moheli_banner", "fomboni",
                 "djoumbe_fatima", "roussette", "lemur_mongoz", "tortue_verte"],
        tips=[
            "Les distributeurs automatiques sont très rares : emportez suffisamment d'espèces.",
            "L'observation des tortues se fait uniquement avec les écoguides des villages.",
            "La meilleure saison pour les baleines s'étend de juillet à octobre.",
        ],
    ),
    dict(
        slug="anjouan",
        name="Anjouan",
        local="Ndzuwani",
        tagline="L'île aux parfums",
        status="Union des Comores",
        chef_lieu="Mutsamudu",
        area="≈ 424 km²",
        summit="Mont Ntingui, 1 595 m",
        accent="#b0861f",
        hero="mutsamudu",
        card="domoni",
        map=(-12.21, 44.43, 10),
        lead=(
            "Montagnes abruptes, cascades, champs d'ylang-ylang et cités de sultans : Anjouan "
            "est l'île la plus spectaculaire par son relief et la plus parfumée de l'archipel."
        ),
        intro="""
<p>Anjouan a la forme d'un triangle dont chaque pointe se termine par une presqu'île. Son centre
est un enchevêtrement de crêtes vertigineuses dominées par le <strong>mont Ntingui</strong>, où
naissent des dizaines de rivières et de cascades. Sur les pentes, les plantations
d'<strong>ylang-ylang</strong>, de girofliers et de vanille ont valu aux Comores le surnom
d'«&nbsp;îles aux parfums&nbsp;».</p>
<p>L'île fut aussi le siège de sultanats prospères, tournés vers le commerce de l'océan Indien.
Les médinas de <strong>Mutsamudu</strong> et de <strong>Domoni</strong>, avec leurs ruelles
étroites, leurs portes sculptées et leurs mosquées anciennes, comptent parmi les ensembles
urbains swahilis les mieux préservés de la région.</p>
""",
        sections=[
            dict(title="Mutsamudu, la citadelle et la médina", media="mutsamudu_escalier", html="""
<p>Agrippée entre l'océan et la montagne, <strong>Mutsamudu</strong> se découvre à pied. Une
<strong>citadelle</strong> de la fin du XVIIIe siècle surplombe la ville et offre une vue
splendide sur le port. En contrebas, la médina dévoile escaliers de pierre, passages couverts
et l'ancien palais des sultans.</p>
<p>[[lieux/mutsamudu.html|Visiter Mutsamudu →]]</p>
"""),
            dict(title="Domoni, berceau des sultans", media="domoni", html="""
<p>Sur la côte est, <strong>Domoni</strong> fut l'une des premières capitales de l'île. Sa
vieille ville, ses tombeaux et ses mosquées racontent cinq siècles d'histoire. C'est aussi au
large d'Anjouan qu'a été pêché en 1952 l'un des tout premiers cœlacanthes étudiés par la
science.</p>
<p>[[lieux/domoni.html|Découvrir Domoni →]]</p>
"""),
            dict(title="Lac Dzialandzé et mont Ntingui", media="lemur_mongoz", html="""
<p>Au cœur de l'île, le <strong>lac Dzialandzé</strong> repose dans un ancien cratère cerné de
forêt, à environ 900&nbsp;m d'altitude. La randonnée qui y mène, puis vers les crêtes du
Ntingui, est l'une des plus belles de l'archipel&nbsp;: forêt de nuages, fougères arborescentes et,
parfois, lémurs mongoz dans les branches.</p>
<p>[[lieux/lac-dzialandze-et-ntingui.html|Randonner au cœur d'Anjouan →]]</p>
"""),
            dict(title="La route des parfums", media="ylang", html="""
<p>Anjouan reste l'un des grands producteurs mondiaux d'essence d'ylang-ylang. Visiter un
alambic traditionnel, sentir les fleurs fraîchement cueillies au petit matin et repartir avec
un flacon est une expérience à ne pas manquer.</p>
<p>[[experiences/route-des-parfums.html|Suivre la route des parfums →]]</p>
"""),
            dict(title="Moya et les plages du sud", media="mutsamudu_port", html="""
<p>Le sud de l'île cache quelques belles plages de sable, dont celle de <strong>Moya</strong>,
appréciée pour la baignade et le snorkeling. La route qui y mène traverse vallées et villages
accrochés aux pentes&nbsp;: comptez du temps, le trajet est un voyage en soi.</p>
"""),
        ],
        places=["mutsamudu", "domoni", "lac-dzialandze-et-ntingui"],
        gallery=["mutsamudu", "mutsamudu_vue", "mutsamudu_port", "mutsamudu_escalier",
                 "mutsamudu_rue", "domoni", "ylang", "ylang_plantation", "lemur_mongoz", "roussette_2"],
        tips=[
            "Les routes de montagne sont étroites et sinueuses : préférez un chauffeur local.",
            "Pour visiter une distillerie d'ylang-ylang, demandez à votre hébergeur.",
            "La randonnée vers le lac Dzialandzé se fait idéalement avec un guide.",
        ],
    ),
    dict(
        slug="mayotte",
        name="Mayotte",
        local="Maore",
        tagline="L'île au lagon",
        status="Département français",
        chef_lieu="Mamoudzou",
        area="≈ 374 km²",
        summit="Mont Bénara, 660 m",
        accent="#1b8fa3",
        hero="lagon_choungui",
        card="lagon_dembeni",
        map=(-12.83, 45.15, 10),
        lead=(
            "La plus ancienne île de l'archipel est entourée de l'un des plus vastes lagons "
            "fermés du monde. Tortues, baleines, dugongs et makis : Mayotte est un sanctuaire "
            "marin au cœur du canal du Mozambique."
        ),
        intro="""
<p>Géologiquement l'aînée de l'archipel, Mayotte a eu le temps de s'entourer d'une ceinture de
corail exceptionnelle. Son <strong>lagon</strong>, d'environ 1&nbsp;100&nbsp;km², est fermé par
une barrière récifale longue de plusieurs dizaines de kilomètres et présente par endroits une
rare <strong>double barrière</strong>. Il est protégé depuis 2010 par le
<strong>parc naturel marin de Mayotte</strong>.</p>
<p>L'île se compose de <strong>Grande-Terre</strong> et de <strong>Petite-Terre</strong>, reliées
par la barge, ainsi que d'une multitude d'îlots. Département français depuis 2011, Mayotte
partage avec ses voisines la langue, la religion et les traditions de l'archipel, tout en
utilisant l'euro et le droit français. L'Union des Comores en revendique la souveraineté.</p>
<div class="notice"><strong>Bon à savoir&nbsp;:</strong> en décembre&nbsp;2024, le cyclone Chido a
durement frappé Mayotte. La reconstruction se poursuit et certains sites, hébergements ou
services peuvent être affectés. Renseignez-vous avant votre départ.</div>
""",
        sections=[
            dict(title="Le lagon, un aquarium géant", media="lagon_dembeni", html="""
<p>Tortues vertes et imbriquées, raies manta, dauphins, plus de deux cents espèces de coraux
et des centaines d'espèces de poissons&nbsp;: le lagon se découvre en kayak, en snorkeling ou en
plongée, notamment dans la célèbre <strong>passe en S</strong>. De juillet à octobre, les
<strong>baleines à bosse</strong> viennent y mettre bas.</p>
<p>[[lieux/lagon-de-mayotte.html|Explorer le lagon de Mayotte →]]</p>
"""),
            dict(title="Petite-Terre et le lac Dziani", media="dziani", html="""
<p>Sur Petite-Terre, un ancien cratère abrite le <strong>lac Dziani</strong>, aux eaux d'un vert
surprenant. Le sentier qui fait le tour du cratère offre des vues à couper le souffle sur le
lagon et sur la plage de <strong>Moya</strong>, site de ponte des tortues. Dzaoudzi, ancien
chef-lieu, garde son rocher et ses bâtiments coloniaux.</p>
<p>[[lieux/petite-terre-et-lac-dziani.html|Découvrir Petite-Terre →]]</p>
"""),
            dict(title="N'Gouja, nager avec les tortues", media="tortue_ngouja", html="""
<p>Dans le sud de Grande-Terre, la plage de <strong>N'Gouja</strong> est célèbre pour ses
tortues vertes qui viennent brouter les herbiers à quelques mètres du bord. Masque et tuba
suffisent pour vivre une rencontre inoubliable, à condition de respecter les distances.</p>
<p>[[lieux/ngouja.html|La plage de N'Gouja →]]</p>
"""),
            dict(title="Mont Choungui et sommets", media="choungui", html="""
<p>Avec son pic en forme de pain de sucre, le <strong>mont Choungui</strong> (594&nbsp;m) est la
silhouette la plus reconnaissable de l'île. Son ascension, courte mais raide, se termine par un
panorama à 360° sur le lagon et sa barrière de corail.</p>
<p>[[lieux/mont-choungui.html|Gravir le mont Choungui →]]</p>
"""),
            dict(title="Mamoudzou et la mosquée de Tsingoni", media="mamoudzou", html="""
<p>Ville animée et principal pôle économique, <strong>Mamoudzou</strong> s'anime autour de son
marché et de son front de mer. À l'ouest, la <strong>mosquée de Tsingoni</strong>, dont le
mihrab date du XVIe siècle, est considérée comme la plus ancienne mosquée en activité du
territoire français.</p>
<p>[[lieux/mamoudzou-et-tsingoni.html|Mamoudzou et Tsingoni →]]</p>
"""),
        ],
        places=["lagon-de-mayotte", "petite-terre-et-lac-dziani", "ngouja", "mont-choungui",
                "mamoudzou-et-tsingoni"],
        gallery=["lagon_choungui", "lagon_dembeni", "lagon_mbouzi", "mbouzi", "dziani",
                 "dziani_aerien", "dzaoudzi", "barge", "ngouja", "ngouja_2", "tortue_ngouja",
                 "tortue_pilote", "dugong", "choungui", "barriere_choungui", "mamoudzou",
                 "mtsapere", "maki", "plage_prefet", "tahiti_plage", "hamouro", "soulou",
                 "coucher_mamoudzou"],
        tips=[
            "La monnaie est l'euro ; les cartes bancaires sont largement acceptées.",
            "La barge relie Mamoudzou à Dzaoudzi en une vingtaine de minutes.",
            "Mayotte ne fait pas partie de l'espace Schengen : vérifiez vos formalités.",
        ],
    ),
]

ISLANDS_BY_SLUG = {i["slug"]: i for i in ISLANDS}
