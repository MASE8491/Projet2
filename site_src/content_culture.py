"""Rubrique Culture & folklore : langues, musique, contes, coutumes, artisanat, cuisine, fêtes, arts."""

CULTURE = dict(
    slug="culture",
    name="Culture & folklore",
    icon="drum",
    hero="manzaraka",
    card="kofia_couture",
    lead=(
        "Langue partagée, grands mariages, danses de femmes et d'hommes, contes de djinns, "
        "msindzano et kofia brodées : la culture comorienne se vit au quotidien dans les quatre îles."
    ),
    intro="""
<p>La culture comorienne est le fruit de mille ans de brassages entre l'Afrique bantoue, le monde
arabo-musulman, la Perse et Madagascar. Elle se transmet surtout <strong>oralement</strong>, par
les contes, les chants, les proverbes et les cérémonies. L'islam, la vie de village, le respect des
aînés et la coutume structurent la société. Chaque île a ses nuances, mais toutes partagent un
même fonds de traditions.</p>
""",
    facts=[
        ("Langue commune", "Shikomori (comorien)"),
        ("Religion", "Islam sunnite"),
        ("Grand rite social", "Le grand mariage (anda, manzaraka)"),
        ("Musique emblématique", "Twarab"),
        ("Beauté traditionnelle", "Msindzano"),
        ("Coiffe masculine", "Kofia brodée"),
    ],
    pages=[
        dict(
            slug="langues",
            name="Langues",
            icon="chat",
            hero="moroni_medina",
            lead="Le shikomori, langue bantoue cousine du swahili, se décline en quatre variantes, une par île. À ses côtés : le français, l'arabe et, à Mayotte, le kibushi.",
            sections=[
                dict(title="Le shikomori", html="""
<p>Le <strong>shikomori</strong> (ou comorien) appartient à la grande famille des langues
<strong>bantoues</strong>. Il est proche du swahili, avec lequel il partage une grande partie de
son vocabulaire, et a emprunté de nombreux mots à l'arabe, au français et au malgache. Longtemps
écrit en caractères arabes (on parle d'écriture <em>ajami</em>), il s'écrit aujourd'hui surtout en
alphabet latin.</p>
"""),
                dict(title="Une langue, quatre parlers", html="""
<table class="table">
  <thead><tr><th>Île</th><th>Variante</th></tr></thead>
  <tbody>
    <tr><td>Grande Comore (Ngazidja)</td><td>Shingazidja</td></tr>
    <tr><td>Mohéli (Mwali)</td><td>Shimwali</td></tr>
    <tr><td>Anjouan (Ndzuwani)</td><td>Shindzuani</td></tr>
    <tr><td>Mayotte (Maore)</td><td>Shimaore</td></tr>
  </tbody>
</table>
<p>Les linguistes distinguent deux groupes&nbsp;: le shingazidja et le shimwali à l'ouest, le
shindzuani et le shimaore à l'est. Les habitants se comprennent d'une île à l'autre, avec un peu
d'effort entre les variantes les plus éloignées.</p>
"""),
                dict(title="Les autres langues", html="""
<ul>
  <li><strong>Le français</strong>, langue de l'administration et de l'enseignement, est compris par une grande partie de la population et officiel à Mayotte.</li>
  <li><strong>L'arabe</strong>, langue du Coran, est appris dans les écoles coraniques et officiel dans l'Union des Comores.</li>
  <li><strong>Le kibushi</strong>, une langue d'origine malgache, est parlé dans plusieurs villages de Mayotte.</li>
</ul>
"""),
                dict(title="Petit lexique", html="""
<table class="table">
  <thead><tr><th>Français</th><th>Comorien</th></tr></thead>
  <tbody>
    <tr><td>Merci</td><td>Marahaba</td></tr>
    <tr><td>Bienvenue</td><td>Karibu</td></tr>
    <tr><td>Au revoir</td><td>Kwaheri</td></tr>
    <tr><td>La mer</td><td>Bahari</td></tr>
  </tbody>
</table>
<p>Les formules de salutation et la prononciation varient selon les îles. Retrouvez d'autres mots
dans notre [[glossaire.html|glossaire]].</p>
"""),
            ],
            didyouknow="Le nom même des îles diffère selon la langue : Ngazidja, Mwali, Ndzuwani et Maore en comorien deviennent Grande Comore, Mohéli, Anjouan et Mayotte en français.",
            gallery=["moroni_medina", "mutsamudu_rue", "marche_tissus"],
        ),
        dict(
            slug="musique-et-danses",
            name="Musique & danses",
            icon="drum",
            hero="comorienne",
            lead="Twarab, chigoma, wadaha, debaa, m'biwi : tambours, violons et chants accompagnent toutes les étapes de la vie.",
            sections=[
                dict(title="Le twarab", html="""
<p>Venu de Zanzibar au début du XXe siècle, le <strong>twarab</strong> (cousin du
<em>taarab</em> swahili) mêle mélodies arabes, rythmes africains et instruments variés&nbsp;: oud,
violon, qanoun, percussions, puis claviers électroniques. Il anime les soirées de mariage, où
chanteurs et orchestres se succèdent jusque tard dans la nuit, et ses chansons d'amour sont
connues de tous.</p>
"""),
                dict(title="Les danses des hommes", html="""
<ul>
  <li><strong>Le chigoma</strong>&nbsp;: danse de prestige exécutée lors du grand mariage en Grande Comore, au son des tambours et des cuivres.</li>
  <li><strong>Le sambé</strong>&nbsp;: danse collective très rythmée, souvent accompagnée de cannes ou de sabres.</li>
  <li><strong>Les chants religieux</strong> (<em>maoulida</em>, <em>daïra</em>)&nbsp;: récités ou chantés en groupe lors des fêtes religieuses, parfois avec des mouvements coordonnés.</li>
</ul>
"""),
                dict(title="Les danses des femmes", media="comorienne", html="""
<ul>
  <li><strong>Le wadaha</strong>&nbsp;: danse du pilon, où les femmes rythment leurs gestes en pilant le riz dans un mortier, entre jeu et démonstration d'adresse.</li>
  <li><strong>Le debaa</strong>&nbsp;: chant religieux dansé par les femmes à Mayotte, vêtues de couleurs vives et de bijoux, en l'honneur du Prophète.</li>
  <li><strong>Le m'biwi</strong>&nbsp;: danse mahoraise au son de baguettes de bambou frappées l'une contre l'autre.</li>
  <li><strong>Le mgodro</strong>&nbsp;: rythme populaire de Mayotte, que l'on danse lors des fêtes de village.</li>
</ul>
"""),
                dict(title="Les instruments", html="""
<p>Tambours de toutes tailles (<em>ngoma</em>), tambourins sur cadre, gongs, flûtes, cithares en
bambou et <strong>gabusi</strong>, un luth à cordes pincées d'origine arabe, composent
l'instrumentarium traditionnel. Les musiques actuelles, du reggae au rap en comorien, continuent de
puiser dans ces rythmes.</p>
"""),
            ],
            didyouknow="Lors des grandes fêtes, les danses peuvent durer toute la nuit : les orchestres se relaient et les invités récompensent les meilleurs danseurs en leur glissant des billets.",
            gallery=["comorienne", "manzaraka", "marche_tissus"],
        ),
        dict(
            slug="contes-et-legendes",
            name="Contes & légendes",
            icon="moon",
            hero="dziani",
            lead="Djinns, lacs engloutis, prophètes et rusés animaux : le folklore comorien se transmet le soir, à la lueur des lampes, de génération en génération.",
            sections=[
                dict(title="La tradition orale", html="""
<p>Aux Comores, les contes se disent le soir, quand le travail est fini. Une conteuse ou un
conteur commence par une formule rituelle à laquelle l'auditoire répond, et le récit peut
commencer. Ces histoires amusent, mais elles enseignent aussi&nbsp;: respect des aînés, hospitalité,
méfiance envers les orgueilleux, ruse des faibles face aux puissants. Plusieurs auteurs, comme
Salim Hatubou, ont recueilli ces contes pour les transmettre par écrit.</p>
"""),
                dict(title="Les djinns et les esprits", html="""
<p>Les <strong>djinns</strong>, êtres invisibles mentionnés dans le Coran, peuplent les récits et
les croyances populaires. On dit qu'ils habitent certains arbres, rochers, grottes ou sources, et
qu'il faut savoir s'en protéger ou se concilier leurs faveurs. À Mayotte et dans certaines
régions de l'archipel, des cultes de possession d'origine malgache (<em>trumba</em>) ou locale
(<em>patros</em>) font encore appel aux esprits lors de cérémonies accompagnées de chants et de
tambours.</p>
"""),
                dict(title="Légendes de lieux", media="dziani", html="""
<ul>
  <li><strong>Le lac Salé</strong> (Grande Comore)&nbsp;: on raconte qu'un village aurait été englouti à cet endroit pour avoir refusé l'hospitalité à un étranger de passage.</li>
  <li><strong>Le Trou du Prophète</strong>&nbsp;: cette anse du nord de la Grande Comore devrait son nom au souvenir d'un saint homme qui y aurait accosté.</li>
  <li><strong>La falaise d'Iconi</strong>&nbsp;: la tradition rapporte que des femmes s'en seraient jetées pour échapper aux razzias venues de Madagascar.</li>
  <li><strong>Mtswa Mwindza</strong>&nbsp;: le récit de cet habitant de Ntsaoueni, parti en Arabie et revenu porteur de l'islam, est l'une des légendes fondatrices de l'archipel.</li>
</ul>
<p>Ces récits, transmis de bouche à oreille, existent en plusieurs versions selon les villages et
les conteurs.</p>
"""),
                dict(title="Personnages de contes", html="""
<p>On retrouve dans les contes comoriens des figures communes à toute la côte swahilie&nbsp;: le
lièvre rusé qui triomphe des plus forts, l'ogre ou le monstre dévoreur, l'enfant orphelin
maltraité qui finit récompensé, le sultan injuste puni par plus malin que lui. Les animaux parlent,
les esprits se mêlent aux humains et la morale tombe toujours à la fin.</p>
"""),
                dict(title="Proverbes et devinettes", html="""
<p>Les <strong>proverbes</strong> ponctuent les conversations et les discours des notables&nbsp;:
savoir les placer au bon moment est un signe de sagesse. Les <strong>devinettes</strong>,
échangées en jeu entre enfants ou en ouverture des veillées de contes, aiguisent l'esprit et
l'art de la parole.</p>
"""),
            ],
            didyouknow="Dans de nombreuses familles, on ne raconte traditionnellement pas les contes en plein jour : c'est une activité réservée à la soirée.",
            gallery=["dziani", "iconi", "ntsaoueni_rempart", "karthala"],
        ),
        dict(
            slug="coutumes-et-rites",
            name="Coutumes & grand mariage",
            icon="rings",
            hero="manzaraka",
            lead="Grand mariage, classes d'âge, coutume et rites de passage : les règles sociales qui organisent la vie dans les villages.",
            sections=[
                dict(title="Le grand mariage", media="manzaraka", html="""
<p>À la Grande Comore, le <strong>anda</strong> ou <em>ndola nkuu</em> (grand mariage) est bien plus
qu'une noce&nbsp;: c'est le rite qui fait passer un homme au rang de notable (<em>mdru mdzima</em>,
«&nbsp;homme accompli&nbsp;») et lui donne la parole sur la place publique. Il peut coûter des années
d'économies&nbsp;: bijoux en or pour la mariée, repas pour tout le village, cortèges, danses et
cadeaux. À Mayotte, son équivalent est le <strong>manzaraka</strong>, et Anjouan et Mohéli
connaissent leurs propres formes de mariage coutumier.</p>
"""),
                dict(title="Une semaine de fêtes", media="bijoux_mariage", html="""
<p>Les cérémonies s'étalent sur plusieurs jours&nbsp;: procession du marié, présentation des
bijoux, soirées de twarab, danses des hommes et des femmes, grand repas collectif. Les invités
revêtent leurs plus beaux habits&nbsp;: <em>djoho</em> brodé et <em>kofia</em> pour les hommes,
<em>chiromani</em> ou <em>saluva</em> et bijoux pour les femmes. La saison des grands mariages
culmine en juillet et août, lorsque la diaspora revient au pays.</p>
"""),
                dict(title="Mila na ntsi : la coutume", html="""
<p>En Grande Comore, le système coutumier, appelé <strong>mila na ntsi</strong> («&nbsp;les us et
le pays&nbsp;»), règle la vie sociale à côté du droit civil et du droit musulman. Les hommes sont
répartis en <strong>classes d'âge</strong> (<em>hirimu</em>), qui leur attribuent des droits et
des devoirs au sein du village. La société est également marquée par une tradition
<strong>matrilinéaire</strong>&nbsp;: la maison familiale revient souvent aux filles.</p>
"""),
                dict(title="Rites de passage", html="""
<ul>
  <li><strong>La naissance</strong>&nbsp;: le nouveau-né reçoit son nom quelques jours après sa naissance, lors d'une petite cérémonie familiale.</li>
  <li><strong>L'école coranique</strong>&nbsp;: dès l'enfance, garçons et filles apprennent à lire le Coran ; la fin de l'apprentissage est célébrée.</li>
  <li><strong>Le mariage</strong>&nbsp;: petit mariage (religieux) puis, pour certains, grand mariage.</li>
  <li><strong>Le deuil</strong>&nbsp;: les funérailles ont lieu rapidement, suivies de prières et de visites de condoléances.</li>
</ul>
"""),
                dict(title="Hospitalité et solidarité", html="""
<p>Recevoir un hôte est un honneur. On offre volontiers un thé, des fruits ou un repas, et la
solidarité familiale et villageoise reste très forte&nbsp;: chacun contribue aux fêtes, aux
constructions de mosquées ou aux funérailles de ses proches.</p>
"""),
            ],
            didyouknow="Un homme qui a accompli son grand mariage peut porter un châle et un djoho particuliers et prendre la parole lors des réunions de notables de son village.",
            gallery=["manzaraka", "bijoux_mariage", "comorienne", "kofia_couture"],
        ),
        dict(
            slug="artisanat-et-costumes",
            name="Artisanat & costumes",
            icon="needle",
            hero="kofia_couture",
            lead="Kofia brodées, portes sculptées, bijoux en or, chiromani et saluva colorés, masque de msindzano : l'élégance comorienne.",
            sections=[
                dict(title="La kofia, couronne brodée", media="kofia_couture", html="""
<p>La <strong>kofia</strong> est la calotte portée par les hommes. Les plus belles, entièrement
brodées à la main de motifs géométriques et floraux, demandent des semaines de travail. Leur
qualité et leurs motifs indiquent parfois l'âge ou le statut de celui qui la porte. Avec le
<strong>kandou</strong> (longue tunique blanche) et le <strong>djoho</strong> (manteau brodé
d'apparat), elle compose la tenue des grandes occasions.</p>
"""),
                dict(title="Chiromani et saluva", media="marche_tissus", html="""
<p>Les femmes portent des pièces de tissu drapées aux couleurs vives. Le <strong>chiromani</strong>,
souvent rouge et blanc, est typique d'Anjouan&nbsp;; le <strong>saluva</strong> (ou salouva) est
le vêtement emblématique des Mahoraises, porté avec un châle sur la tête ou les épaules. Les
marchés regorgent de tissus imprimés venus d'Afrique de l'Est et d'Asie.</p>
"""),
                dict(title="Le msindzano", html="""
<p>Le <strong>msindzano</strong> est un masque de beauté obtenu en frottant un morceau de bois de
santal sur une pierre de corail humidifiée. La pâte jaune pâle, appliquée sur le visage,
adoucit et protège la peau du soleil. Les jours de fête, elle est dessinée en motifs délicats de
points et de fleurs. C'est l'un des symboles les plus visibles de la féminité comorienne.</p>
"""),
                dict(title="Bois, pierre et métal", media="mutsamudu_rue", html="""
<ul>
  <li><strong>Portes sculptées</strong>&nbsp;: les encadrements en bois des maisons anciennes de Mutsamudu, Domoni ou Moroni sont ornés de motifs floraux et de versets.</li>
  <li><strong>Coffres et lits</strong>&nbsp;: le mobilier traditionnel, comme le lit nuptial, est souvent finement travaillé.</li>
  <li><strong>Bijouterie</strong>&nbsp;: colliers, bracelets et pendentifs en or ou en argent, transmis de mère en fille, sont au cœur du grand mariage.</li>
  <li><strong>Vannerie</strong>&nbsp;: nattes, paniers et éventails tressés en feuilles de cocotier ou de pandanus.</li>
</ul>
"""),
            ],
            didyouknow="Une belle kofia brodée à la main peut demander plusieurs semaines, voire plusieurs mois de travail.",
            gallery=["kofia_couture", "marche_tissus", "bijoux_mariage", "comorienne", "mutsamudu_rue"],
        ),
        dict(
            slug="cuisine",
            name="Cuisine",
            icon="bowl",
            hero="moroni_port_2",
            lead="Lait de coco, épices de l'océan Indien, poissons, manioc et fruit à pain : une cuisine généreuse, parfumée et faite pour être partagée.",
            sections=[
                dict(title="Les grands classiques", html="""
<ul>
  <li><strong>Langouste à la vanille</strong>&nbsp;: le plat de fête, où la vanille locale parfume le crustacé.</li>
  <li><strong>Mataba</strong>&nbsp;: feuilles de manioc pilées, mijotées au lait de coco, souvent avec du poisson.</li>
  <li><strong>Pilao</strong>&nbsp;: riz parfumé à la cannelle, à la cardamome et au clou de girofle, cuit avec de la viande.</li>
  <li><strong>M'tsolola</strong>&nbsp;: poisson ou viande avec bananes vertes et manioc dans une sauce au coco.</li>
  <li><strong>Mkatra foutra</strong>&nbsp;: pain plat au lait de coco, au petit-déjeuner.</li>
  <li><strong>Mabawa</strong>&nbsp;: ailes de poulet grillées, star de la cuisine de rue à Mayotte.</li>
</ul>
"""),
                dict(title="Les épices", media="ylang_plantation", html="""
<p>L'archipel produit certaines des épices les plus recherchées&nbsp;: <strong>vanille</strong>,
<strong>clou de girofle</strong>, <strong>cannelle</strong>, poivre. Elles parfument plats salés et
sucrés, ainsi que le thé, souvent préparé avec de la citronnelle, du gingembre ou du lait.</p>
"""),
                dict(title="Douceurs et fruits", html="""
<p>Les <em>ladu</em> (boulettes sucrées de farine de riz), les beignets de banane, les gâteaux de
riz au coco et les pâtisseries de fête accompagnent le thé. Mangues, papayes, ananas, corossols,
jacques, fruits à pain et, en fin d'année, <strong>litchis</strong> remplissent les étals.</p>
"""),
                dict(title="À table", html="""
<p>Le repas se partage souvent sur une natte, autour d'un plat commun, et l'on mange de la main
droite. Pendant le <strong>ramadan</strong>, la rupture du jeûne réunit les familles autour de
soupes, de beignets, de dattes et de plats mijotés. Retrouvez aussi nos conseils dans
[[voyager/index.html|Voyager]].</p>
"""),
            ],
            didyouknow="La vanille est une orchidée : aux Comores, chaque fleur est pollinisée à la main, une par une, car l'insecte qui le fait naturellement au Mexique est absent de l'océan Indien.",
            gallery=["ylang", "ylang_plantation", "moroni_port_2", "mitsamiouli", "marche_tissus"],
        ),
        dict(
            slug="fetes-et-religion",
            name="Fêtes & religion",
            icon="moon",
            hero="moroni_mosquee",
            lead="Ramadan, Maoulid, Aïd, fêtes nationales : l'islam et le calendrier lunaire rythment l'année dans tout l'archipel.",
            sections=[
                dict(title="Un islam ancien et tolérant", media="moroni_mosquee", html="""
<p>La quasi-totalité des Comoriens sont musulmans sunnites, de rite <strong>chaféite</strong>,
comme sur toute la côte swahilie. Les confréries soufies, comme la Chadhiliyya ou la Qadiriyya,
ont joué un rôle important dans la diffusion de l'islam et la vie religieuse. Chaque village
possède sa mosquée du vendredi et ses écoles coraniques.</p>
"""),
                dict(title="Le Maoulid", html="""
<p>La fête de la naissance du Prophète (<strong>Maoulid</strong>) est l'un des moments forts de
l'année. Pendant plusieurs semaines, les villages organisent à tour de rôle des récitations de
poèmes et des chants religieux collectifs, parfois accompagnés de mouvements rythmés, et des
repas partagés.</p>
"""),
                dict(title="Ramadan et Aïd", html="""
<p>Pendant le mois de <strong>ramadan</strong>, les journées sont calmes et les soirées animées
autour de la rupture du jeûne. L'<strong>Aïd el-Fitr</strong> marque la fin du jeûne&nbsp;:
nouveaux vêtements, visites familiales, cadeaux aux enfants. L'<strong>Aïd el-Kébir</strong>
commémore le sacrifice d'Abraham. Ces fêtes suivent le calendrier lunaire et avancent d'une
dizaine de jours chaque année.</p>
"""),
                dict(title="Fêtes civiles", html="""
<ul>
  <li><strong>6 juillet</strong>&nbsp;: fête de l'indépendance de l'Union des Comores.</li>
  <li><strong>27 avril</strong>&nbsp;: commémoration de l'abolition de l'esclavage à Mayotte.</li>
  <li><strong>14 juillet</strong>&nbsp;: fête nationale française, célébrée à Mayotte.</li>
</ul>
<p>Voir le [[agenda.html|calendrier complet]].</p>
"""),
            ],
            didyouknow="Pendant la saison du Maoulid, les villages se rendent visite pour assister aux chants religieux les uns des autres : une occasion de resserrer les liens entre communautés.",
            gallery=["moroni_mosquee", "moroni_ancienne_mosquee", "mtsapere", "moroni_mosquee_2"],
        ),
        dict(
            slug="litterature-et-arts",
            name="Littérature & arts",
            icon="book",
            hero="moroni_centre",
            lead="De la poésie orale aux romans contemporains, de la peinture au cinéma : une création vivante, entre archipel et diaspora.",
            sections=[
                dict(title="De l'oral à l'écrit", html="""
<p>La littérature comorienne est d'abord orale&nbsp;: contes, poèmes chantés, épopées
villageoises et proverbes. Des manuscrits en comorien et en arabe, écrits en caractères arabes,
conservent aussi poèmes religieux et chroniques. La littérature écrite en français se développe à
partir des années 1980.</p>
"""),
                dict(title="Quelques écrivains", html="""
<ul>
  <li><strong>Mohamed Toihiri</strong>&nbsp;: <em>La République des Imberbes</em> (1985), satire politique considérée comme le premier roman comorien en français.</li>
  <li><strong>Salim Hatubou</strong>&nbsp;: conteur et auteur prolifique, passeur du patrimoine oral de l'archipel.</li>
  <li><strong>Ali Zamir</strong>&nbsp;: <em>Anguille sous roche</em> (2016), roman d'une seule phrase salué par la critique.</li>
  <li><strong>Nassur Attoumani</strong>&nbsp;: romancier et dramaturge mahorais.</li>
  <li><strong>Soeuf Elbadawi</strong>&nbsp;: poète, dramaturge et artiste.</li>
</ul>
"""),
                dict(title="Musique d'aujourd'hui", html="""
<p>Des artistes comme <strong>Maalesh</strong>, <strong>Nawal</strong> ou
<strong>Salim Ali Amir</strong> ont fait connaître la musique comorienne au-delà de l'archipel, en
mêlant twarab, rythmes traditionnels, folk et musiques du monde. Le rap, le reggae et les musiques
électroniques en comorien sont aujourd'hui très populaires auprès des jeunes, dans l'archipel comme
dans la diaspora.</p>
"""),
                dict(title="Arts visuels, cinéma et patrimoine", media="manzaraka", html="""
<p>Peintres, photographes et cinéastes explorent les thèmes de l'insularité, de l'exil et de la
mémoire. Des institutions comme le <strong>Centre national de documentation et de recherche
scientifique</strong> (CNDRS) à Moroni ou le <strong>musée de Mayotte</strong> à Dzaoudzi
conservent et présentent le patrimoine de l'archipel.</p>
"""),
            ],
            didyouknow="Le roman Anguille sous roche d'Ali Zamir est composé d'une seule et unique phrase de plus de 300 pages.",
            gallery=["manzaraka", "moroni_centre", "comorienne"],
        ),
    ],
)
