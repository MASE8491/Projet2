"""Pages transverses : découvrir l'archipel, agenda, vidéos, accueil."""

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
        ("1 000 ans", "d'histoire swahilie"),
        ("4", "variantes de la langue comorienne"),
    ],
    features=[
        dict(media="sultan_said_ali", kicker="Histoire", title="Au temps des sultans",
             text="Cités de pierre, rivalités princières, escales des navires des Indes et razzias venues de Madagascar : plongez dans l'histoire mouvementée des sultanats de l'archipel.",
             href="histoire/le-temps-des-sultans.html"),
        dict(media="dziani", kicker="Folklore", title="Djinns, lacs engloutis et contes du soir",
             text="Le folklore comorien se transmet à la veillée : légendes de lieux, esprits des arbres et des sources, lièvre rusé et sultans punis.",
             href="culture/contes-et-legendes.html"),
        dict(media="coelacanthe", kicker="Nature", title="Sur la trace du cœlacanthe",
             text="Longtemps cru disparu, ce poisson apparu il y a plus de 400 millions d'années vit dans les grottes sous-marines des Comores.",
             href="geographie/faune-et-flore.html"),
    ],
)
