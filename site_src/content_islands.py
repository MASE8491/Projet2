"""Les quatre îles de l'archipel des Comores, présentées par thème.

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
        language="Shingazidja",
        accent="#c65a3a",
        hero="moroni_panorama",
        card="moroni_centre",
        map=(-11.65, 43.33, 10),
        lead=(
            "La plus vaste et la plus jeune des quatre îles vit au rythme de son volcan, le Karthala. "
            "Coulées de lave, médinas de corail, anciens sultanats et grands mariages : Ngazidja est "
            "le cœur politique et culturel de l'Union des Comores."
        ),
        intro="""
<p>Vue du ciel, la Grande Comore ressemble à une vaste coulée figée dans l'océan. Née des
éruptions du <strong>Karthala</strong> au sud et du massif plus ancien de la <strong>Grille</strong>
au nord, c'est la plus jeune île de l'archipel, et la plus grande. Elle abrite
<strong>Moroni</strong>, capitale de l'Union des Comores, et près de la moitié de la population
du pays. C'est aussi l'île où les traditions coutumières, à commencer par le grand mariage, sont
les plus vivaces.</p>
""",
        themes=[
            dict(key="geo", title="Géographie", media="karthala", html="""
<p>L'île, longue d'environ 65&nbsp;km, est presque entièrement volcanique. Le
<strong>Karthala</strong> (2&nbsp;361&nbsp;m), l'un des volcans les plus actifs de l'océan
Indien, occupe toute sa moitié sud&nbsp;; son sommet est creusé d'une caldeira de plusieurs
kilomètres. La roche, très poreuse, absorbe l'eau de pluie&nbsp;: l'île ne compte presque aucune
rivière permanente. Le littoral alterne falaises de basalte noir et plages de sable blanc,
surtout au nord, autour de <strong>Mitsamiouli</strong>. Curiosités géologiques&nbsp;: le
<strong>lac Salé</strong>, cratère d'eau saumâtre, et le <strong>Trou du Prophète</strong>.</p>
<p>[[geographie/volcans-et-reliefs.html|En savoir plus sur les volcans de l'archipel →]]</p>
"""),
            dict(key="histoire", title="Histoire", media="sultan_said_ali", html="""
<p>Pendant des siècles, Ngazidja fut divisée en une dizaine de <strong>sultanats</strong> rivaux
(Bambao, Itsandra, Mitsamiouli, Badjini…), dont les souverains se disputaient le titre de
<em>sultan tibe</em>. <strong>Iconi</strong>, <strong>Itsandra</strong> et <strong>Ntsaoueni</strong>
comptent parmi les plus anciennes cités. À la fin du XIXe siècle, le sultan <strong>Saïd Ali</strong>
du Bambao unifie l'île avec l'appui de la France, qui y établit son protectorat en 1886. Moroni
devient capitale de l'archipel dans les années 1960, puis de l'État indépendant en 1975.</p>
<p>[[histoire/le-temps-des-sultans.html|Le temps des sultans →]]</p>
"""),
            dict(key="culture", title="Culture & traditions", media="bijoux_mariage", html="""
<p>La Grande Comore est le pays du <strong>anda</strong>, le grand mariage qui fait passer un homme
au rang de notable. La société y est organisée par la coutume (<em>mila na ntsi</em>) et par les
classes d'âge. On y parle le <strong>shingazidja</strong>. Les danses de prestige comme le
<em>chigoma</em>, les orchestres de twarab et les cortèges en <em>djoho</em> brodés animent les
étés, quand la diaspora revient au pays.</p>
<p>[[culture/coutumes-et-rites.html|Coutumes et grand mariage →]]</p>
"""),
            dict(key="nature", title="Nature", media="coelacanthe", html="""
<p>Les forêts d'altitude du Karthala abritent des oiseaux uniques au monde, comme le petit-duc du
Karthala. Au large de la côte sud-ouest, les grottes sous-marines des pentes volcaniques sont le
refuge du <strong>cœlacanthe</strong>, protégé par le parc national du Cœlacanthe. Les tortues
fréquentent les plages du nord.</p>
"""),
        ],
        places=["moroni", "karthala", "nord-grande-comore", "iconi", "ntsaoueni"],
        gallery=["moroni_panorama", "moroni_mosquee", "moroni_ancienne_mosquee", "moroni_port",
                 "itsandra", "karthala", "karthala_lave", "mitsamiouli", "moroni_medina",
                 "ntsaoueni_rempart", "iconi", "sultan_said_ali"],
        tips=[
            "L'aéroport international Prince Saïd Ibrahim se trouve à Hahaya, à une vingtaine de kilomètres au nord de Moroni.",
            "L'été (juillet-août) est la saison des grands mariages : ambiance festive, mais hébergements plus chers.",
            "Prévoyez de bonnes chaussures : les sentiers volcaniques sont abrasifs.",
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
        language="Shimwali",
        accent="#2f7d55",
        hero="nioumachoua_ilots",
        card="nioumachoua_ilots",
        map=(-12.32, 43.74, 11),
        lead=(
            "La plus petite et la plus sauvage des îles comoriennes. Forêts, mangroves, plages de "
            "ponte des tortues et souvenir de la reine Djoumbé Fatima : Mohéli est une réserve de "
            "biosphère à ciel ouvert."
        ),
        intro="""
<p>On arrive à Mohéli comme on entre dans un jardin. L'île, peu peuplée et peu urbanisée, a gardé
une grande partie de ses forêts et de ses mangroves. Son littoral sud est protégé au sein du
<strong>parc national de Mohéli</strong>, premier parc marin du pays, et l'île entière est
reconnue depuis 2020 comme <strong>réserve de biosphère</strong> par l'UNESCO. Son chef-lieu,
<strong>Fomboni</strong>, a gardé des allures de gros village.</p>
""",
        themes=[
            dict(key="geo", title="Géographie", media="nioumachoua_mangrove", html="""
<p>Allongée d'ouest en est sur une quarantaine de kilomètres, Mohéli est parcourue par une
dorsale boisée culminant au <strong>Mzé Koukoulé</strong> (790&nbsp;m). Plus ancienne que la Grande
Comore, elle est entaillée de vallées et bordée de plaines littorales. Au sud, un chapelet
d'<strong>îlots</strong> fait face au village de Nioumachoua, et des <strong>mangroves</strong>
s'étendent dans les baies. Au sud-est, le cratère du <strong>lac Dziani Boundouni</strong>
accueille de nombreux oiseaux d'eau.</p>
<p>[[geographie/ocean-et-lagons.html|Océan, récifs et lagons →]]</p>
"""),
            dict(key="histoire", title="Histoire", media="djoumbe_fatima", html="""
<p>Longtemps placée dans l'orbite d'Anjouan, Mohéli passe au XIXe siècle sous la domination d'un
prince venu de Madagascar, <strong>Ramanetaka</strong>. Sa fille, la reine
<strong>Djoumbé Fatima</strong>, règne au milieu des rivalités entre la France, la Grande-Bretagne
et Zanzibar, et se rend jusqu'à Paris pour défendre son île. Mohéli passe sous protectorat
français en 1886. En 2001, c'est à Fomboni qu'est signé l'accord qui donne naissance à l'Union
des Comores.</p>
<p>[[histoire/personnages.html|Les grandes figures de l'histoire →]]</p>
"""),
            dict(key="culture", title="Culture & traditions", media="fomboni", html="""
<p>On y parle le <strong>shimwali</strong>. La vie s'organise autour des villages de pêcheurs et
d'agriculteurs, où les traditions de l'archipel (mariages, Maoulid, danses) se vivent de façon
plus intime qu'à la Grande Comore. Les associations villageoises sont au cœur de la protection
de la nature&nbsp;: ce sont elles qui forment les écoguides d'Itsamia et gèrent les zones de pêche
du parc.</p>
"""),
            dict(key="nature", title="Nature", media="roussette", html="""
<p>Mohéli est l'un des derniers refuges de la <strong>roussette de Livingstone</strong>, une
chauve-souris géante, et abrite le <strong>lémur mongoz</strong>. Les plages d'<strong>Itsamia</strong>
comptent parmi les plus importants sites de ponte de <strong>tortues vertes</strong> de l'océan
Indien occidental, et les <strong>baleines à bosse</strong> fréquentent ses eaux de juillet à
octobre.</p>
<p>[[geographie/faune-et-flore.html|Faune et flore de l'archipel →]]</p>
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
        language="Shindzuani",
        accent="#b0861f",
        hero="mutsamudu",
        card="domoni",
        map=(-12.21, 44.43, 10),
        lead=(
            "Montagnes abruptes, cascades, champs d'ylang-ylang et cités de sultans : Anjouan est "
            "l'île la plus spectaculaire par son relief, et celle dont l'histoire maritime est la "
            "plus riche."
        ),
        intro="""
<p>Anjouan a la forme d'un triangle dont chaque pointe se prolonge par une presqu'île. Son centre
est un enchevêtrement de crêtes vertigineuses dominées par le <strong>mont Ntingui</strong>. Très
peuplée, cultivée jusque sur les pentes les plus raides, elle a valu aux Comores le surnom
d'«&nbsp;îles aux parfums&nbsp;» grâce à ses plantations d'ylang-ylang. Ses médinas de
<strong>Mutsamudu</strong> et de <strong>Domoni</strong> comptent parmi les plus belles de l'océan
Indien.</p>
""",
        themes=[
            dict(key="geo", title="Géographie", media="mutsamudu_vue", html="""
<p>Le relief d'Anjouan est le plus tourmenté de l'archipel&nbsp;: l'érosion a sculpté des cirques,
des vallées profondes et des dizaines de rivières et de <strong>cascades</strong>. Au centre, le
<strong>lac Dzialandzé</strong> occupe un cratère forestier vers 900&nbsp;m d'altitude, sur les
flancs du <strong>mont Ntingui</strong> (1&nbsp;595&nbsp;m). Trois presqu'îles, dont celle de
<strong>Bimbini</strong> à l'ouest, prolongent l'île. La forte densité de population exerce une
pression importante sur les forêts et les sources.</p>
"""),
            dict(key="histoire", title="Histoire", media="carte_amiraute", html="""
<p>Siège d'un sultanat puissant, Anjouan a longtemps exercé une influence sur Mohéli et Mayotte.
<strong>Domoni</strong>, puis <strong>Mutsamudu</strong>, en furent les capitales. Aux XVIIe et
XVIIIe siècles, les navires anglais de la route des Indes faisaient escale dans cette île qu'ils
appelaient <em>Johanna</em>. Face aux razzias venues de Madagascar, Mutsamudu se dota d'une
<strong>citadelle</strong> à la fin du XVIIIe siècle. C'est aussi au large d'Anjouan qu'a été pêché
en 1952 un cœlacanthe qui a fait le tour du monde.</p>
<p>[[histoire/le-temps-des-sultans.html|Le temps des sultans →]]</p>
"""),
            dict(key="culture", title="Culture & traditions", media="mutsamudu_rue", html="""
<p>On y parle le <strong>shindzuani</strong>. Les femmes portent le <strong>chiromani</strong>,
tissu drapé souvent rouge et blanc, devenu un symbole de l'île. Les médinas conservent un riche
artisanat de portes sculptées et de broderies. La culture de l'<strong>ylang-ylang</strong>, de la
<strong>vanille</strong> et du <strong>girofle</strong> rythme la vie des villages, entre cueillette
à l'aube et distillation dans les alambics.</p>
<p>[[culture/artisanat-et-costumes.html|Artisanat et costumes →]]</p>
"""),
            dict(key="nature", title="Nature", media="lemur_mongoz", html="""
<p>Les forêts de nuages du centre de l'île abritent la <strong>roussette de Livingstone</strong>,
le <strong>lémur mongoz</strong> et le <strong>petit-duc d'Anjouan</strong>, un hibou longtemps cru
disparu. Les parcs nationaux du mont Ntingui et de Shisiwani cherchent à préserver ces milieux
fragiles.</p>
"""),
        ],
        places=["mutsamudu", "domoni", "lac-dzialandze-et-ntingui"],
        gallery=["mutsamudu", "mutsamudu_vue", "mutsamudu_port", "mutsamudu_escalier",
                 "mutsamudu_rue", "domoni", "ylang", "ylang_plantation", "lemur_mongoz",
                 "roussette_2", "carte_amiraute"],
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
        language="Shimaore et kibushi",
        accent="#1b8fa3",
        hero="lagon_choungui",
        card="lagon_dembeni",
        map=(-12.83, 45.15, 10),
        lead=(
            "La plus ancienne île de l'archipel est entourée de l'un des plus vastes lagons fermés "
            "du monde. Tortues, baleines et makis, mosquée de Tsingoni et rocher de Dzaoudzi : "
            "Mayotte allie richesse naturelle et histoire singulière."
        ),
        intro="""
<p>Géologiquement l'aînée de l'archipel, Mayotte a eu le temps de s'entourer d'une ceinture de
corail exceptionnelle. Elle se compose de <strong>Grande-Terre</strong>, de
<strong>Petite-Terre</strong> et d'une trentaine d'îlots. Française depuis 1841, devenue
département en 2011, elle partage avec ses voisines la langue, la religion et les traditions de
l'archipel, tout en utilisant l'euro et le droit français. L'Union des Comores en revendique la
souveraineté.</p>
<div class="notice"><strong>Bon à savoir&nbsp;:</strong> en décembre&nbsp;2024, le cyclone Chido a
durement frappé Mayotte. La reconstruction se poursuit et certains sites ou services peuvent être
affectés.</div>
""",
        themes=[
            dict(key="geo", title="Géographie", media="barriere_choungui", html="""
<p>Érodée et lentement affaissée, Mayotte présente des reliefs adoucis, culminant au
<strong>mont Bénara</strong> (660&nbsp;m), et des pitons comme le <strong>mont Choungui</strong>.
Son <strong>lagon</strong>, d'environ 1&nbsp;100&nbsp;km², est fermé par une barrière de corail longue
de plus de 150&nbsp;km, doublée au sud-ouest d'une rare <strong>double barrière</strong>. Sur
Petite-Terre, le <strong>lac Dziani</strong> occupe un ancien cratère. Depuis 2018, un nouveau
volcan sous-marin, <strong>Fani Maoré</strong>, s'est formé à une cinquantaine de kilomètres à
l'est.</p>
<p>[[geographie/ocean-et-lagons.html|Océan, récifs et lagons →]]</p>
"""),
            dict(key="histoire", title="Histoire", media="residence_gouverneur", html="""
<p>Le site de <strong>Dembéni</strong> témoigne d'un commerce actif avec le golfe Persique et la
Chine dès le IXe siècle. Au XVIe siècle, <strong>Tsingoni</strong> est la capitale du sultanat&nbsp;;
sa mosquée porte un mihrab daté de 1538. En 1841, le sultan <strong>Andriantsoly</strong> cède l'île
à la France, qui installe son administration sur le rocher de <strong>Dzaoudzi</strong>.
L'esclavage y est aboli en 1846. Lors des consultations de 1974 et 1976, les Mahorais choisissent
de rester français&nbsp;; l'île devient le 101e département en 2011.</p>
<p>[[histoire/periode-coloniale.html|La période coloniale →]]</p>
"""),
            dict(key="culture", title="Culture & traditions", media="manzaraka", html="""
<p>On y parle le <strong>shimaore</strong> et, dans plusieurs villages, le <strong>kibushi</strong>,
d'origine malgache. Les femmes portent le <strong>saluva</strong> et le <strong>msindzano</strong>.
Le <strong>manzaraka</strong>, grand mariage mahorais, le <strong>debaa</strong> chanté par les
femmes et le <strong>m'biwi</strong> rythmé par les bambous sont au cœur des fêtes. Le musée de
Mayotte, à Dzaoudzi, présente ce patrimoine.</p>
<p>[[culture/musique-et-danses.html|Musique et danses →]]</p>
"""),
            dict(key="nature", title="Nature", media="tortue_ngouja", html="""
<p>Le lagon, protégé par le <strong>parc naturel marin de Mayotte</strong>, abrite tortues vertes,
dauphins, raies, plus de deux cents espèces de coraux et quelques derniers
<strong>dugongs</strong>. Les <strong>baleines à bosse</strong> viennent y mettre bas de juillet à
octobre. À terre, les <strong>makis</strong> se laissent facilement observer, et les forêts des
crêtes sont protégées par une réserve naturelle nationale.</p>
"""),
        ],
        places=["lagon-de-mayotte", "petite-terre-et-lac-dziani", "ngouja", "mont-choungui",
                "mamoudzou-et-tsingoni"],
        gallery=["lagon_choungui", "lagon_dembeni", "lagon_mbouzi", "mbouzi", "dziani",
                 "dziani_aerien", "dzaoudzi", "residence_gouverneur", "hopital_dzaoudzi", "barge",
                 "ngouja", "tortue_ngouja", "tortue_pilote", "dugong", "choungui",
                 "barriere_choungui", "mamoudzou", "mtsapere", "maki", "manzaraka",
                 "tahiti_plage", "soulou", "coucher_mamoudzou"],
        tips=[
            "La monnaie est l'euro ; les cartes bancaires sont largement acceptées.",
            "La barge relie Mamoudzou à Dzaoudzi en une vingtaine de minutes.",
            "Mayotte ne fait pas partie de l'espace Schengen : vérifiez vos formalités.",
        ],
    ),
]

ISLANDS_BY_SLUG = {i["slug"]: i for i in ISLANDS}
