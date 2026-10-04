"""Pages transverses : découvrir l'archipel, agenda, vidéos, accueil."""

ARCHIPEL = dict(
    hero="lagon_choungui",
    lead=(
        "Quatre îles volcaniques posées à l'entrée nord du canal du Mozambique, entre l'Afrique "
        "et Madagascar. Leur nom viendrait de l'arabe « Djazaïr al-Qamar » : les îles de la Lune."
    ),
    facts=[
        ("Localisation", "Canal du Mozambique, océan Indien"),
        ("Îles", "Grande Comore, Mohéli, Anjouan, Mayotte"),
        ("Point culminant", "Karthala, 2 361 m"),
        ("Langues", "Shikomori, français, arabe"),
        ("Monnaies", "Franc comorien (KMF), euro à Mayotte"),
        ("Fuseau", "UTC+3"),
    ],
    sections=[
        dict(title="Une géographie de feu et de corail", media="karthala_lave", html="""
<p>L'archipel des Comores est né de l'activité volcanique qui a fait surgir les îles du fond de
l'océan. Les îles sont d'autant plus anciennes qu'elles sont situées à l'est&nbsp;: <strong>Mayotte</strong>,
la plus vieille, est érodée et entourée d'un immense lagon&nbsp;; <strong>Anjouan</strong> et
<strong>Mohéli</strong> présentent des reliefs découpés et des forêts profondes&nbsp;; la
<strong>Grande Comore</strong>, la plus jeune, est encore dominée par le Karthala, l'un des volcans
les plus actifs de la région. Quelque 300&nbsp;km séparent l'archipel des côtes du Mozambique comme
de celles de Madagascar.</p>
"""),
        dict(title="Mille ans d'histoire swahilie", media="moroni_ancienne_mosquee", html="""
<p>Les premiers habitants, d'origine bantoue, s'installent sur les îles au cours du premier
millénaire. Au fil des siècles, des navigateurs et commerçants venus de la côte africaine, du
golfe Persique, d'Arabie, d'Inde et de Madagascar y font escale. L'islam s'implante tôt, et
des <strong>sultanats</strong> rivaux se partagent les îles, enrichis par le commerce maritime de
l'océan Indien. À la fin du XVIIIe siècle, des raids venus de Madagascar poussent les cités à se
fortifier&nbsp;: c'est l'époque des citadelles et des remparts.</p>
"""),
        dict(title="De la colonisation à l'indépendance", media="djoumbe_fatima", html="""
<p>La France acquiert Mayotte en 1841, puis établit son protectorat sur les autres îles à la fin
du XIXe siècle. L'archipel devient colonie, rattachée un temps à Madagascar, puis territoire
d'outre-mer après 1946. Le <strong>6 juillet 1975</strong>, les Comores proclament leur
indépendance. Mayotte, où la population s'était majoritairement prononcée pour le maintien
dans la France, reste sous administration française&nbsp;; l'Union des Comores continue de
revendiquer l'île.</p>
"""),
        dict(title="L'archipel aujourd'hui", media="mamoudzou", html="""
<p>L'<strong>Union des Comores</strong>, dont la capitale est Moroni, rassemble la Grande
Comore, Mohéli et Anjouan, chacune disposant d'une large autonomie. <strong>Mayotte</strong>
est devenue le 101e département français en 2011 et une région ultrapériphérique de l'Union
européenne en 2014. Au-delà des frontières politiques, les quatre îles partagent une même
langue, une même religion et des liens familiaux étroits.</p>
"""),
        dict(title="Peuples, langues et religion", media="moroni_medina", html="""
<p>La société comorienne est le fruit d'un métissage africain, arabe, persan et malgache. La
grande majorité des habitants sont musulmans sunnites. On parle partout le
<strong>shikomori</strong> sous ses différentes formes, le français et, dans l'Union, l'arabe. La
<strong>diaspora</strong>, importante en France (notamment à Marseille), à La Réunion et à Mayotte,
joue un rôle essentiel dans la vie économique et culturelle de l'archipel.</p>
"""),
    ],
)

EVENTS = [
    dict(when="Janvier – mars", title="Cœur de la saison chaude", text="Pluies tropicales, végétation luxuriante et mer chaude. Période de vigilance cyclonique.", tag="Climat"),
    dict(when="27 avril", title="Commémoration de l'abolition de l'esclavage (Mayotte)", text="Jour férié à Mayotte, marqué par des cérémonies et manifestations culturelles.", tag="Mayotte"),
    dict(when="Mai – octobre", title="Saison sèche, saison des randonnées", text="Le meilleur moment pour gravir le Karthala, le Ntingui ou le Choungui.", tag="Nature"),
    dict(when="6 juillet", title="Fête de l'indépendance", text="Fête nationale de l'Union des Comores : défilés, discours et festivités dans les trois îles.", tag="Union des Comores"),
    dict(when="Juillet – août", title="Saison des grands mariages", text="Retour de la diaspora, cortèges et danses traditionnelles, surtout en Grande Comore.", tag="Culture"),
    dict(when="14 juillet", title="Fête nationale française (Mayotte)", text="Défilés et animations à Mamoudzou et dans les communes de l'île.", tag="Mayotte"),
    dict(when="Juillet – octobre", title="Saison des baleines à bosse", text="Les baleines viennent mettre bas dans les eaux chaudes de l'archipel. Pic en août-septembre.", tag="Nature"),
    dict(when="Toute l'année", title="Ponte des tortues vertes", text="À Itsamia (Mohéli), Moya et Saziley (Mayotte), avec des pics variables selon les plages.", tag="Nature"),
    dict(when="Novembre – janvier", title="Saison des litchis et des mangues", text="Les marchés débordent de fruits : un régal de fin d'année.", tag="Gastronomie"),
    dict(when="Dates lunaires", title="Ramadan, Aïd el-Fitr, Aïd el-Kébir, Maoulid", text="Les grandes fêtes religieuses suivent le calendrier lunaire et avancent d'une dizaine de jours chaque année. Le Maoulid donne lieu à des chants et processions remarquables.", tag="Religion"),
]

VIDEOS = ["v_baleine", "v_tortues", "v_bebe_tortue", "v_recif", "v_vagues"]

HOME = dict(
    hero="lagon_choungui",
    stats=[
        ("4", "îles, un même archipel"),
        ("2 361 m", "au sommet du Karthala"),
        ("≈ 1 100 km²", "de lagon à Mayotte"),
        ("400 Ma", "l'âge de la lignée du cœlacanthe"),
    ],
    features=[
        dict(media="coelacanthe", kicker="Fossile vivant", title="Sur la trace du cœlacanthe",
             text="Longtemps cru disparu, ce poisson préhistorique vit dans les grottes sous-marines des Comores. Il est devenu le symbole d'un archipel hors du temps.",
             href="experiences/nature-et-faune.html"),
        dict(media="baleine", kicker="Juillet – octobre", title="La saison des baleines",
             text="Chaque hiver austral, les baleines à bosse viennent mettre bas dans les eaux chaudes de l'archipel. Un spectacle inoubliable depuis un bateau.",
             href="experiences/plongee-et-ocean.html"),
    ],
)
