"""Rubrique Histoire : périodes, frise chronologique, personnages."""

HISTOIRE = dict(
    slug="histoire",
    name="Histoire",
    icon="scroll",
    hero="moroni_ancienne_mosquee",
    card="sultan_said_ali",
    lead=(
        "Des premiers navigateurs bantous aux sultans swahilis, de la colonisation à l'indépendance : "
        "mille ans d'histoire au carrefour de l'Afrique, de l'Arabie, de la Perse et de Madagascar."
    ),
    intro="""
<p>Longtemps escale sur les routes maritimes de l'océan Indien, l'archipel a vu passer marins,
marchands, prédicateurs, pirates et colons. De ces rencontres est née une civilisation originale,
à la fois africaine, musulmane et maritime, dont les médinas, les mosquées et les traditions
orales gardent la trace. Cette rubrique retrace les grandes étapes de cette histoire, que les
quatre îles ont longtemps partagée avant que leurs destins politiques ne divergent en 1975.</p>
""",
    facts=[
        ("Premiers peuplements", "Ier millénaire"),
        ("Islamisation", "À partir du Xe siècle environ"),
        ("Mayotte française", "1841"),
        ("Protectorat sur les trois autres îles", "1886"),
        ("Indépendance des Comores", "6 juillet 1975"),
        ("Mayotte, département", "31 mars 2011"),
    ],
    pages=[
        dict(
            slug="premiers-peuplements",
            name="Premiers peuplements & monde swahili",
            period="VIIIe – XVe siècle",
            icon="boat",
            hero="moroni_port",
            lead="Navigateurs bantous, marchands arabes et persans, influences malgaches : la naissance d'une civilisation de l'océan Indien.",
            sections=[
                dict(title="Les premiers habitants", html="""
<p>Les fouilles archéologiques indiquent une occupation des îles au cours du <strong>premier
millénaire</strong> de notre ère. Les premiers habitants venaient vraisemblablement de la côte
orientale de l'Afrique et parlaient des langues bantoues, ancêtres du comorien actuel. Ils
cultivaient, pêchaient et commerçaient déjà avec les rivages voisins.</p>
"""),
                dict(title="Un carrefour commercial", html="""
<p>À partir du IXe siècle, l'archipel s'insère dans les grands réseaux du commerce de l'océan
Indien. À Mayotte, le site archéologique de <strong>Dembéni</strong> a livré des céramiques venues
du golfe Persique, de Chine et de l'Inde, témoignant d'échanges lointains. Les îles exportent
riz, bétail, ambre gris et cauris, et servent d'escale entre la côte africaine et Madagascar.</p>
"""),
                dict(title="L'arrivée de l'islam", media="moroni_ancienne_mosquee", html="""
<p>L'islam s'implante progressivement, sans doute dès le Xe siècle, porté par les marchands et
les lettrés de la côte swahilie. La tradition attribue à un certain <strong>Mtswa Mwindza</strong>,
originaire de Ntsaoueni en Grande Comore, l'introduction de la nouvelle religion après un voyage en
Arabie&nbsp;: un récit fondateur plus légendaire qu'historique, mais très vivant dans la mémoire
collective. Les plus anciennes mosquées de l'archipel, à Sima (Anjouan), Ntsaoueni ou Domoni,
remontent à cette époque ou aux siècles suivants.</p>
"""),
                dict(title="Les « Shirazi »", html="""
<p>Comme sur toute la côte swahilie, de nombreuses familles nobles des Comores se disent
descendantes de princes venus de <strong>Shiraz</strong>, en Perse. Les historiens y voient
surtout un mythe d'origine prestigieux, adopté par les élites marchandes, mais il témoigne des
liens réels entre l'archipel, le golfe Persique et l'Arabie du Sud. Ces élites fondent les
premières cités de pierre et les dynasties qui deviendront les sultanats.</p>
"""),
            ],
            didyouknow="Les céramiques chinoises retrouvées sur le site de Dembéni, à Mayotte, prouvent que l'archipel participait au commerce mondial de l'époque il y a plus de mille ans.",
            gallery=["moroni_port", "moroni_ancienne_mosquee", "domoni", "carte_1808"],
        ),
        dict(
            slug="le-temps-des-sultans",
            name="Le temps des sultans",
            period="XVe – XIXe siècle",
            icon="dome",
            hero="mutsamudu_escalier",
            lead="Cités de pierre, rivalités princières, escales européennes et razzias venues de Madagascar : l'âge d'or et les tourments des sultanats.",
            sections=[
                dict(title="Des îles morcelées en sultanats", html="""
<p>Du XVe au XIXe siècle, l'archipel est divisé en plusieurs <strong>sultanats</strong>. La
Grande Comore en compte jusqu'à une dizaine, comme le Bambao, l'Itsandra, le Mitsamiouli ou le
Badjini, dont les souverains se disputent le titre de <em>sultan tibe</em>, le suzerain de l'île.
Anjouan, Mohéli et Mayotte forment chacune un sultanat, Anjouan exerçant longtemps une influence
sur ses voisines.</p>
"""),
                dict(title="Médinas, mosquées et palais", media="mutsamudu_rue", html="""
<p>Les sultans et les familles marchandes bâtissent des villes de pierre à l'architecture
swahilie&nbsp;: maisons à cour intérieure, portes sculptées, ruelles étroites, mosquées du
vendredi. <strong>Domoni</strong> et <strong>Mutsamudu</strong> à Anjouan, <strong>Iconi</strong>,
<strong>Itsandra</strong> et <strong>Moroni</strong> en Grande Comore, <strong>Tsingoni</strong> à
Mayotte, dont la mosquée porte un mihrab daté de 1538, en sont les plus beaux exemples.</p>
"""),
                dict(title="Les Européens à l'escale", media="carte_amiraute", html="""
<p>Les navigateurs portugais signalent l'archipel dès le début du XVIe siècle. Aux XVIIe et
XVIIIe siècles, Anjouan, que les marins anglais appellent <em>Johanna</em>, devient une escale
appréciée des navires de la Compagnie anglaise des Indes orientales, qui y font provision d'eau
et de vivres. Des <strong>pirates</strong> célèbres croisent aussi dans ces eaux à la fin du
XVIIe siècle.</p>
"""),
                dict(title="Le temps des razzias", media="ntsaoueni_rempart", html="""
<p>À la fin du XVIIIe et au début du XIXe siècle, des flottes venues de Madagascar mènent des
<strong>razzias</strong> meurtrières sur les côtes comoriennes, capturant hommes et femmes pour
les réduire en esclavage. Les cités se protègent par des <strong>remparts</strong> et des
<strong>citadelles</strong>, comme à Mutsamudu ou à Ntsaoueni. À Iconi, la tradition rapporte que
des femmes préférèrent se jeter du haut de la falaise plutôt que d'être capturées.</p>
"""),
                dict(title="Princes malgaches et intrigues", media="djoumbe_fatima", html="""
<p>Au XIXe siècle, des princes malgaches chassés par l'expansion du royaume merina s'installent
dans l'archipel. <strong>Andriantsoly</strong>, ancien roi sakalava, prend le pouvoir à Mayotte.
<strong>Ramanetaka</strong>, prince merina, s'empare de Mohéli, où sa fille
<strong>Djoumbé Fatima</strong> régnera ensuite. Dans le même temps, la France, la
Grande-Bretagne et le sultanat de Zanzibar cherchent à étendre leur influence dans la région.</p>
"""),
            ],
            didyouknow="Les marins anglais du XVIIIe siècle appelaient Anjouan « Johanna » et la Grande Comore « Angazija », des noms que l'on retrouve sur les cartes anciennes.",
            gallery=["mutsamudu_escalier", "mutsamudu_rue", "ntsaoueni_rempart", "iconi", "carte_amiraute", "djoumbe_fatima"],
        ),
        dict(
            slug="periode-coloniale",
            name="La période coloniale",
            period="1841 – 1975",
            icon="flag",
            hero="residence_gouverneur",
            lead="De la cession de Mayotte en 1841 à l'autonomie interne : plus d'un siècle de présence française dans l'archipel.",
            sections=[
                dict(title="1841 : Mayotte devient française", media="andriantsoly", html="""
<p>Menacé par ses rivaux, le sultan <strong>Andriantsoly</strong> cède Mayotte à la France par un
traité signé en <strong>1841</strong>. La France cherche alors un point d'appui dans l'océan Indien
après la perte de l'île Maurice. Dzaoudzi, sur son rocher de Petite-Terre, devient le siège de
l'administration. L'esclavage y est aboli en <strong>1846</strong>, deux ans avant le reste des
colonies françaises, et des plantations de canne à sucre se développent.</p>
"""),
                dict(title="1886 : le protectorat", media="sultan_said_ali", html="""
<p>En <strong>1886</strong>, la France impose son protectorat aux sultanats de la Grande Comore,
d'Anjouan et de Mohéli. En Grande Comore, le sultan <strong>Saïd Ali</strong> du Bambao, qui a
unifié l'île avec l'appui français, signe le traité. Des sociétés coloniales obtiennent de vastes
concessions de terres, au détriment des paysans, ce qui provoque des révoltes, notamment en Grande
Comore en 1915.</p>
"""),
                dict(title="1912 : rattachement à Madagascar", html="""
<p>En <strong>1912</strong>, l'archipel devient une colonie rattachée administrativement à
Madagascar. Les Comores sont alors une périphérie lointaine de la Grande Île&nbsp;: peu
d'infrastructures, peu d'écoles, une économie tournée vers l'exportation de vanille, de girofle,
de coprah et d'essences à parfum comme l'ylang-ylang.</p>
"""),
                dict(title="1946 – 1975 : vers l'autonomie", media="hopital_dzaoudzi", html="""
<p>Après la Seconde Guerre mondiale, les Comores sont séparées de Madagascar et deviennent un
<strong>territoire d'outre-mer</strong> (1946). Elles obtiennent l'autonomie interne en
<strong>1961</strong>, avec à leur tête <strong>Saïd Mohamed Cheikh</strong>, président du
conseil de gouvernement. Le transfert de la capitale de Dzaoudzi à Moroni, décidé à la fin des
années 1950 et achevé dans les années 1960, nourrit à Mayotte un mouvement favorable au maintien
dans la France, porté notamment par des femmes surnommées les «&nbsp;chatouilleuses&nbsp;».</p>
"""),
            ],
            didyouknow="L'esclavage fut aboli à Mayotte dès 1846, deux ans avant l'abolition générale dans les colonies françaises. L'anniversaire est commémoré chaque 27 avril à Mayotte.",
            gallery=["residence_gouverneur", "hopital_dzaoudzi", "dzaoudzi", "andriantsoly", "sultan_said_ali", "said_ali"],
        ),
        dict(
            slug="independance-et-epoque-contemporaine",
            name="Indépendance & époque contemporaine",
            period="1975 – aujourd'hui",
            icon="star",
            hero="carte_1976",
            lead="L'indépendance proclamée en 1975, le choix de Mayotte, les crises politiques et la naissance de l'Union des Comores.",
            sections=[
                dict(title="Le référendum de 1974", html="""
<p>Le <strong>22 décembre 1974</strong>, les habitants de l'archipel votent sur l'indépendance.
Une très large majorité se prononce pour, mais à Mayotte, une majorité choisit le maintien dans
la France. Paris décide alors de prendre en compte les résultats île par île, ce que contestent
les autorités comoriennes.</p>
"""),
                dict(title="6 juillet 1975 : l'indépendance", html="""
<p>Le <strong>6 juillet 1975</strong>, <strong>Ahmed Abdallah</strong>, président du conseil de
gouvernement, proclame unilatéralement l'indépendance des Comores. Le nouvel État est admis à
l'ONU en novembre 1975 avec ses quatre îles. Mayotte, elle, reste française et confirme ce choix
lors d'une consultation en <strong>1976</strong>.</p>
"""),
                dict(title="Des années agitées", html="""
<p>Les premières décennies de l'indépendance sont marquées par une forte instabilité&nbsp;:
coups d'État, régime révolutionnaire d'<strong>Ali Soilih</strong> (1975-1978), retour au pouvoir
d'Ahmed Abdallah, interventions de mercenaires étrangers. En 1997, Anjouan et Mohéli font
sécession. La crise se dénoue avec l'accord de <strong>Fomboni</strong> en 2001 et une nouvelle
constitution qui crée l'<strong>Union des Comores</strong>, où chaque île dispose d'une large
autonomie et où la présidence tourne entre les îles.</p>
"""),
                dict(title="Mayotte, 101e département", media="mamoudzou", html="""
<p>Après un référendum en 2009, Mayotte devient le <strong>101e département français</strong> le
31 mars 2011, puis une <strong>région ultrapériphérique</strong> de l'Union européenne en 2014.
L'île connaît une croissance démographique rapide et des défis importants&nbsp;: logement, accès à
l'eau, immigration, inégalités. Depuis 2018, elle est aussi au cœur d'une crise sismique liée à la
naissance du volcan sous-marin Fani Maoré, et elle a été dévastée par le cyclone Chido en
décembre 2024.</p>
"""),
                dict(title="L'archipel aujourd'hui", html="""
<p>L'Union des Comores a adopté une nouvelle constitution en 2018 et poursuit ses efforts de
développement. Malgré la frontière politique, les liens familiaux, culturels et économiques entre
les quatre îles restent très étroits. La question du statut de Mayotte demeure un sujet de
désaccord entre la France et l'Union des Comores.</p>
"""),
            ],
            didyouknow="Les Comores ont été admises à l'ONU le 12 novembre 1975, quelques mois seulement après la proclamation de leur indépendance.",
            gallery=["carte_1976", "moroni_panorama", "mamoudzou", "fomboni"],
        ),
        dict(
            slug="personnages",
            name="Grandes figures",
            period="Portraits",
            icon="people",
            hero="djoumbe_fatima",
            lead="Reines et sultans, hommes politiques, militantes, écrivains et musiciens : quelques personnalités qui ont marqué l'histoire de l'archipel.",
            sections=[
                dict(title="Djoumbé Fatima (1836 – 1878)", media="djoumbe_fatima", html="""
<p>Reine de Mohéli, fille du prince merina Ramanetaka, elle accède au trône encore enfant. Son
règne est marqué par les rivalités entre puissances européennes et par sa volonté de préserver
l'indépendance de son île, qui la conduit jusqu'à Paris. Elle reste l'une des figures féminines
les plus célèbres de l'histoire comorienne.</p>
"""),
                dict(title="Andriantsoly (première moitié du XIXe siècle)", media="andriantsoly", html="""
<p>Ancien roi sakalava du Boina, à Madagascar, il se réfugie à Mayotte et en devient le
souverain. Menacé par ses voisins, il cède l'île à la France en 1841, ouvrant une nouvelle page de
l'histoire de l'archipel.</p>
"""),
                dict(title="Saïd Ali ben Saïd Omar (mort en 1916)", media="said_ali", html="""
<p>Sultan du Bambao, il parvient à dominer l'ensemble de la Grande Comore avec l'appui de la
France et signe le traité de protectorat de 1886. Il est souvent présenté comme le dernier grand
sultan de l'île.</p>
"""),
                dict(title="Hommes politiques de l'indépendance", html="""
<ul>
  <li><strong>Saïd Mohamed Cheikh</strong>, médecin, préside le conseil de gouvernement de l'autonomie interne dans les années 1960.</li>
  <li><strong>Prince Saïd Ibrahim</strong>, qui lui succède, a donné son nom à l'aéroport international de Moroni.</li>
  <li><strong>Ahmed Abdallah</strong> proclame l'indépendance le 6 juillet 1975.</li>
  <li><strong>Ali Soilih</strong> conduit de 1975 à 1978 un régime révolutionnaire qui bouscule les traditions.</li>
</ul>
"""),
                dict(title="Les chatouilleuses de Mayotte", html="""
<p>Dans les années 1960, des femmes mahoraises, parmi lesquelles <strong>Zéna M'Déré</strong>,
mènent une campagne active pour le maintien de Mayotte dans la France. Leur surnom vient de leur
méthode&nbsp;: «&nbsp;chatouiller&nbsp;» les responsables politiques venus défendre l'option
contraire jusqu'à les faire renoncer. Elles sont devenues des figures de l'histoire mahoraise.</p>
"""),
                dict(title="Écrivains et artistes", html="""
<ul>
  <li><strong>Mohamed Toihiri</strong>, auteur de <em>La République des Imberbes</em> (1985), souvent présenté comme le premier roman comorien en français.</li>
  <li><strong>Salim Hatubou</strong>, conteur et écrivain, a recueilli et transmis de nombreux contes de l'archipel.</li>
  <li><strong>Ali Zamir</strong>, romancier, auteur d'<em>Anguille sous roche</em> (2016), salué par la critique.</li>
  <li><strong>Nassur Attoumani</strong>, écrivain et dramaturge mahorais.</li>
  <li><strong>Maalesh</strong>, <strong>Nawal</strong> ou <strong>Salim Ali Amir</strong>, musiciens qui ont fait connaître les sonorités comoriennes au-delà de l'archipel.</li>
</ul>
<p>Voir aussi [[culture/litterature-et-arts.html|Littérature &amp; arts]].</p>
"""),
            ],
            didyouknow="L'aéroport international de Moroni porte le nom du prince Saïd Ibrahim, l'un des dirigeants de l'archipel pendant l'autonomie interne.",
            gallery=["djoumbe_fatima", "andriantsoly", "said_ali", "sultan_said_ali"],
        ),
    ],
)

# Frise chronologique (page d'accueil de la rubrique Histoire)
TIMELINE = [
    ("Ier millénaire", "Premiers habitants", "Des populations venues de la côte est-africaine s'installent dans les îles."),
    ("IXe – XIIe s.", "Dembéni, comptoir marchand", "Mayotte participe au commerce de l'océan Indien : céramiques persanes et chinoises."),
    ("Xe s. environ", "Arrivée de l'islam", "La nouvelle religion se diffuse depuis la côte swahilie ; premières mosquées."),
    ("XVe s.", "Naissance des sultanats", "Les cités de pierre et les dynasties se développent dans les quatre îles."),
    ("1538", "Mosquée de Tsingoni", "Date inscrite sur le mihrab de la mosquée de Tsingoni, à Mayotte."),
    ("XVIIe – XVIIIe s.", "Anjouan, escale des Indes", "Les navires anglais de la route des Indes font escale à « Johanna »."),
    ("v. 1780 – 1820", "Le temps des razzias", "Raids venus de Madagascar ; construction de citadelles et de remparts."),
    ("1841", "Mayotte française", "Le sultan Andriantsoly cède l'île à la France."),
    ("1846", "Abolition à Mayotte", "L'esclavage est aboli à Mayotte, deux ans avant les autres colonies."),
    ("1886", "Protectorat", "La France établit son protectorat sur la Grande Comore, Anjouan et Mohéli."),
    ("1912", "Colonie de Madagascar", "L'archipel est rattaché administrativement à Madagascar."),
    ("1946", "Territoire d'outre-mer", "Les Comores sont séparées de Madagascar."),
    ("1952", "Le cœlacanthe d'Anjouan", "Un cœlacanthe pêché à Anjouan confirme la survie de ce « fossile vivant »."),
    ("1961", "Autonomie interne", "Saïd Mohamed Cheikh préside le conseil de gouvernement."),
    ("1974", "Référendum", "Large majorité pour l'indépendance, sauf à Mayotte."),
    ("6 juillet 1975", "Indépendance", "Ahmed Abdallah proclame l'indépendance des Comores."),
    ("1976", "Mayotte reste française", "Les Mahorais confirment leur choix lors d'une consultation."),
    ("1997", "Crise séparatiste", "Anjouan et Mohéli font sécession."),
    ("2001", "Union des Comores", "Accord de Fomboni et nouvelle constitution fédérale."),
    ("2011", "101e département", "Mayotte devient un département français."),
    ("2018", "Fani Maoré", "Début de la crise sismique qui révèle un nouveau volcan sous-marin près de Mayotte."),
    ("2020", "Réserve de biosphère", "L'UNESCO reconnaît l'île de Mohéli réserve de biosphère."),
    ("2024", "Cyclone Chido", "Mayotte est dévastée par un cyclone d'une rare violence."),
]
