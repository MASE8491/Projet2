"""Médiathèque du site Komori.

Toutes les photos et vidéos proviennent de Wikimedia Commons, qui n'héberge que
des fichiers sous licence libre (Creative Commons, GFDL…) ou dans le domaine
public. Elles sont chargées directement depuis Commons via Special:FilePath.

Chaque entrée :
    file     nom exact du fichier sur Commons (sans le préfixe « File: »)
    caption  légende en français
    island   gc | moheli | anjouan | mayotte | archipel (sert aux filtres de la galerie)
    author   auteur quand il est connu (sinon voir la page source)
    license  licence quand elle est connue (sinon voir la page source)
    kind     image (défaut) | video
    gallery  False pour exclure de la galerie
"""

COMMONS_FILEPATH = "https://commons.wikimedia.org/wiki/Special:FilePath/"
COMMONS_PAGE = "https://commons.wikimedia.org/wiki/File:"

MEDIA = {
    # ------------------------------------------------------------------ Grande Comore
    "moroni_panorama": dict(
        file="Moroni_Capital_of_the_Comores_Photo_by_Sascha_Grabow.jpg",
        caption="Moroni, capitale de l'Union des Comores, entre océan Indien et pentes du Karthala",
        island="gc", author="Sascha Grabow"),
    "moroni_centre": dict(
        file="Moroni_Capital_of_Comores_Photo_by_Sascha_Grabow.jpg",
        caption="Le cœur de Moroni : la mosquée du Vendredi et la baie du vieux port",
        island="gc", author="Sascha Grabow"),
    "moroni_mosquee": dict(
        file="Moroni_Friday_Mosque_Comoros.jpg",
        caption="La mosquée du Vendredi, silhouette blanche du front de mer de Moroni",
        island="gc", license="CC BY 3.0 PL"),
    "moroni_ancienne_mosquee": dict(
        file="Ancienne_Mosquee_du_Vendredi_(10886895544).jpg",
        caption="L'ancienne mosquée du Vendredi de Moroni, fondée au XVe siècle",
        island="gc"),
    "moroni_mosquee_2": dict(
        file="Mosque_in_Moroni,_Comoros_(3923026238).jpg",
        caption="Minaret dans la vieille ville de Moroni",
        island="gc"),
    "moroni_medina": dict(
        file="Moroni_Medina_Comoros_2.jpg",
        caption="Ruelles ombragées de la médina de Moroni",
        island="gc"),
    "moroni_port": dict(
        file="Moroni-Harbour.jpg",
        caption="Le vieux port de Moroni, où accostaient autrefois les boutres",
        island="gc"),
    "moroni_port_2": dict(
        file="Moroni_harbour_(2).jpg",
        caption="Barques et pirogues dans le port de Moroni",
        island="gc"),
    "moroni_bord_de_mer": dict(
        file="Moroni_beach.jpg",
        caption="Bord de mer aux abords de Moroni",
        island="gc"),
    "moroni_banner": dict(
        file="Moroni_banner.jpg",
        caption="Panorama de Moroni",
        island="gc", gallery=False),
    "itsandra": dict(
        file="Moroni,_Comoros.jpg",
        caption="La plage d'Itsandra, à quelques minutes au nord de Moroni",
        island="gc", author="TheLizardQueen", license="CC BY 2.0"),
    "karthala": dict(
        file="Karthala_volcano-Comoros.jpg",
        caption="La caldeira du Karthala, l'un des plus vastes cratères actifs du monde",
        island="gc", author="alKomor.com", license="CC BY-SA 2.0"),
    "karthala_lave": dict(
        file="Lava_Flows_of_Mount_Karthala_volcano_in_Grande_Comore.jpg",
        caption="Anciennes coulées de lave du Karthala descendant vers la mer",
        island="gc"),
    "mitsamiouli": dict(
        file="Mitsamiouli_beach_pirogues_Comoros.jpg",
        caption="Pirogues à balancier sur le sable blanc de Mitsamiouli",
        island="gc", license="CC BY 3.0 PL"),

    # ------------------------------------------------------------------ Mohéli
    "moheli_banner": dict(
        file="Mohéli_banner.jpg",
        caption="Côte sauvage de Mohéli",
        island="moheli"),
    "fomboni": dict(
        file="Fomboni-Ship.jpg",
        caption="Navire au mouillage devant Fomboni, chef-lieu de Mohéli",
        island="moheli"),
    "nioumachoua_ilots": dict(
        file="Îlot_de_Nioumachoua.jpg",
        caption="Les îlots de Nioumachoua, joyaux du parc national de Mohéli",
        island="moheli"),
    "nioumachoua_mangrove": dict(
        file="Panorama_mangrove_de_nioumachoua.jpg",
        caption="La mangrove de Nioumachoua, nurserie de la vie marine",
        island="moheli"),
    "djoumbe_fatima": dict(
        file="Queen_of_Mohéli.jpg",
        caption="Djoumbé Fatima, reine de Mohéli au XIXe siècle",
        island="moheli"),

    # ------------------------------------------------------------------ Anjouan
    "domoni": dict(
        file="Anjouan_-_Islands_of_Comoros.jpg",
        caption="Domoni, ancienne cité des sultans sur la côte est d'Anjouan",
        island="anjouan", author="Haryamouji"),
    "mutsamudu": dict(
        file="Mutsamudu_(9983246206).jpg",
        caption="Mutsamudu, serrée entre l'océan et les pentes vertes d'Anjouan",
        island="anjouan"),
    "mutsamudu_vue": dict(
        file="Mutsamudu.jpg",
        caption="Vue d'ensemble de Mutsamudu, chef-lieu d'Anjouan",
        island="anjouan"),
    "mutsamudu_port": dict(
        file="Mutsamudu_port1.jpg",
        caption="Le port de Mutsamudu, porte d'entrée maritime d'Anjouan",
        island="anjouan"),
    "mutsamudu_escalier": dict(
        file="Mutsamudu_Stone_Stairway_(9983185465).jpg",
        caption="Escaliers de pierre dans la médina de Mutsamudu",
        island="anjouan"),
    "mutsamudu_rue": dict(
        file="Mutsamudu_Street_(9983198004).jpg",
        caption="Une ruelle étroite de la vieille ville de Mutsamudu",
        island="anjouan"),

    # ------------------------------------------------------------------ Mayotte
    "mayotte_banner": dict(
        file="Mayotte_banner.jpg",
        caption="Le lagon de Mayotte",
        island="mayotte", gallery=False),
    "lagon_choungui": dict(
        file="LAGON_MAYOTTE.jpg",
        caption="Le lagon de Mayotte vu depuis le sommet du mont Choungui",
        island="mayotte", license="CC BY-SA 4.0"),
    "lagon_dembeni": dict(
        file="Le_lagon_à_Dembéni_(Mayotte)_(34073252283).jpg",
        caption="Le lagon à Dembéni, avec Petite-Terre à l'horizon",
        island="mayotte"),
    "lagon_mbouzi": dict(
        file="Mayotte_lagon_avec_ilôt_M'Bouzi_à_droite.jpg",
        caption="Le lagon et l'îlot M'Bouzi",
        island="mayotte"),
    "mbouzi": dict(
        file="Îlot_M'Bouzi.jpg",
        caption="L'îlot M'Bouzi, réserve naturelle nationale au large de Mamoudzou",
        island="mayotte"),
    "plage_prefet": dict(
        file="Plage_du_Préfet_(Mayotte).jpg",
        caption="La plage du Préfet, à Mayotte",
        island="mayotte"),
    "tahiti_plage": dict(
        file="Tahiti_plage_Mayotte_2.JPG",
        caption="Tahiti Plage, l'une des anses les plus fréquentées de Mayotte",
        island="mayotte"),
    "tahiti_plage_2": dict(
        file="Tahiti_plage_Mayotte_1.jpg",
        caption="Sable clair et eaux calmes à Tahiti Plage",
        island="mayotte"),
    "hamouro": dict(
        file="Plage_de_Hamouro-Mayotte.jpg",
        caption="La plage de Hamouro, sur la côte est de Grande-Terre",
        island="mayotte"),
    "soulou": dict(
        file="Plage_de_Soulou_2.JPG",
        caption="La plage de Soulou, dans le nord-ouest de Mayotte",
        island="mayotte"),
    "ngouja": dict(
        file="N'Gouja_2.jpg",
        caption="La plage de N'Gouja, dans le sud de Mayotte",
        island="mayotte"),
    "ngouja_2": dict(
        file="Nguja_(3063720186).jpg",
        caption="Les eaux turquoise de N'Gouja, royaume des tortues",
        island="mayotte"),
    "tortue_ngouja": dict(
        file="Tortue_N'Gouja.jpg",
        caption="Tortue verte broutant les herbiers de N'Gouja",
        island="mayotte", author="Frédéric Ducarme"),
    "tortue_pilote": dict(
        file="Tortue_verte_et_poisson-pilote.jpg",
        caption="Tortue verte escortée d'un poisson-pilote dans le lagon",
        island="mayotte", author="Frédéric Ducarme"),
    "dugong": dict(
        file="Dugong_du_parc_marin_de_Mayotte.jpg",
        caption="Un dugong, hôte rare et protégé du parc naturel marin de Mayotte",
        island="mayotte"),
    "dziani": dict(
        file="Mayotte-indian-ocean-dziani-lake-landscape-496a6b54ac95062ba05d28389a3cadac.jpg",
        caption="Le lac Dziani, lac de cratère aux eaux vert émeraude sur Petite-Terre",
        island="mayotte"),
    "dziani_aerien": dict(
        file="Dziani_Dzaha_in_Volcanic_Crater_in_Mayotte.jpg",
        caption="Vue aérienne du cratère du Dziani Dzaha",
        island="mayotte"),
    "dziani_2": dict(
        file="Lac_Dziani_Dzaha.jpg",
        caption="Les rives du Dziani Dzaha",
        island="mayotte"),
    "dzaoudzi": dict(
        file="Dzaoudzi.jpg",
        caption="Dzaoudzi, ancien chef-lieu installé sur son rocher de Petite-Terre",
        island="mayotte"),
    "barge": dict(
        file="La_barge_à_Dzaoudzi_(Mayotte)_(34019109614).jpg",
        caption="La barge, trait d'union entre Grande-Terre et Petite-Terre",
        island="mayotte"),
    "choungui": dict(
        file="Choungui_nord.jpg",
        caption="Le pic du mont Choungui vu du nord",
        island="mayotte", author="Frédéric Ducarme"),
    "choungui_2": dict(
        file="Mont_Choungui.jpg",
        caption="Le mont Choungui, sentinelle du sud de Mayotte",
        island="mayotte", author="Frédéric Ducarme"),
    "barriere_choungui": dict(
        file="Barrière_de_corail_et_lagon_vus_du_Mont_Choungui.jpg",
        caption="La double barrière de corail vue du mont Choungui",
        island="mayotte"),
    "mamoudzou": dict(
        file="Mayotte-mamoudzou-1800x1000-d259bf1d.jpg",
        caption="Mamoudzou, principale ville de Mayotte, face au lagon",
        island="mayotte", license="CC BY-SA 4.0"),
    "mamoudzou_2": dict(
        file="Mamoudzou_(10029936275).jpg",
        caption="Le front de mer de Mamoudzou",
        island="mayotte", author="David Stanley"),
    "mtsapere": dict(
        file="La_mosquée_de_Mtsapéré_(Mayotte)_(34746792691).jpg",
        caption="La mosquée de Mtsapéré, à Mamoudzou",
        island="mayotte"),
    "coucher_mamoudzou": dict(
        file="2004_12_12_18-24-04_rose_sea_in_mamoudzou_mayotte_island.jpg",
        caption="Coucher de soleil rose sur le lagon à Mamoudzou",
        island="mayotte"),
    "maki": dict(
        file="Maki_de_mayotte.jpg",
        caption="Le maki de Mayotte, lémurien emblématique de l'île",
        island="mayotte", author="Jérôme G"),

    # ------------------------------------------------------------------ Faune, flore, archipel
    "coelacanthe": dict(
        file="Latimeria_Chalumnae_-_Coelacanth_-_NHMW.jpg",
        caption="Cœlacanthe pêché en 1974 au large de la Grande Comore (Muséum d'histoire naturelle de Vienne)",
        island="archipel", author="Alberto Fernandez Fernandez"),
    "roussette": dict(
        file="Bristol.zoo.livfruitbat.arp.jpg",
        caption="La roussette de Livingstone, chauve-souris géante endémique d'Anjouan et de Mohéli",
        island="archipel"),
    "roussette_2": dict(
        file="Livingstone's_Fruit_Bat.jpg",
        caption="Roussette de Livingstone, l'un des mammifères les plus rares de l'océan Indien",
        island="archipel"),
    "lemur_mongoz": dict(
        file="Eulemur-mongoz_59489762.jpg",
        caption="Le lémur mongoz, présent à Anjouan et à Mohéli",
        island="archipel"),
    "ylang": dict(
        file="Cananga_odorata_flowers.jpg",
        caption="Fleurs d'ylang-ylang, l'or parfumé des Comores",
        island="archipel"),
    "ylang_plantation": dict(
        file="A_ylang-ylang_plantation,_near_a_factory_producing_essential_oil_from_the_flowers_(4).jpg",
        caption="Plantation d'ylang-ylang à proximité d'une distillerie",
        island="archipel"),
    "baleine": dict(
        file="026e_Humpback_whale_jump_and_splash_Photo_by_Giles_Laurent.jpg",
        caption="Saut de baleine à bosse (photo d'illustration)",
        island="archipel", author="Giles Laurent", license="CC BY-SA 4.0"),
    "tortue_verte": dict(
        file="Green_sea_turtle_(Chelonia_mydas)_Moorea.jpg",
        caption="Tortue verte en pleine eau (photo d'illustration)",
        island="archipel"),

    # ------------------------------------------------------------------ Histoire & cartes
    "carte_1976": dict(
        file="Comoros_country_map_1976,_CIA.jpg",
        caption="Carte de l'archipel des Comores publiée en 1976, un an après l'indépendance",
        island="histoire", license="Domaine public"),
    "carte_1808": dict(
        file="Map_of_Africa_(1808)_-_CAMORA_excerpt.jpg",
        caption="Extrait d'une carte de l'Afrique de 1808 où l'archipel apparaît sous le nom de « Camora »",
        island="histoire", license="Domaine public"),
    "carte_amiraute": dict(
        file="Admiralty_Chart_No_2762_Comoro_Islands,_Published_1879.jpg",
        caption="Carte marine britannique des îles Comores, publiée en 1879",
        island="histoire", license="Domaine public"),
    "sultan_said_ali": dict(
        file="Sultan_Said_Ali_ben_Said_Omar_of_Bambao_with_other_important_people_in_Ngazidja_(grand_comore).jpg",
        caption="Le sultan Saïd Ali ben Saïd Omar de Bambao entouré de notables de Ngazidja, avant 1916",
        island="histoire", license="Domaine public"),
    "said_ali": dict(
        file="Said_Ali.jpg",
        caption="Saïd Ali, dernier sultan de la Grande Comore",
        island="histoire", license="Domaine public"),
    "andriantsoly": dict(
        file="Andriantsoly.jpg",
        caption="Andriantsoly, souverain de Mayotte qui céda l'île à la France en 1841",
        island="histoire", license="Domaine public"),
    "ntsaoueni_rempart": dict(
        file="Ntsaoueni_Wall_(10927095456).jpg",
        caption="Le rempart de Ntsaoueni, bâti contre les razzias et qui protège aujourd'hui la ville des tempêtes",
        island="gc"),
    "iconi": dict(
        file="Grande_Comore-Iconi-Ancienne_capitale.jpg",
        caption="Iconi, ancienne capitale de sultanat au sud de Moroni",
        island="gc"),
    "residence_gouverneur": dict(
        file="La_Résidence_du_gouverneur_(Dzaoudzi,_Mayotte)_(34824394185).jpg",
        caption="La résidence du gouverneur à Dzaoudzi, bâtie à l'emplacement du palais du sultan Andriantsoly",
        island="mayotte", author="Jean-Pierre Dalbéra", license="CC BY 2.0"),
    "hopital_dzaoudzi": dict(
        file="L'hôpital_historique_(Dzaoudzi,_Mayotte)_(34787688536).jpg",
        caption="L'ancien hôpital colonial du rocher de Dzaoudzi",
        island="mayotte", author="Jean-Pierre Dalbéra", license="CC BY 2.0"),

    # ------------------------------------------------------------------ Culture & traditions
    "manzaraka": dict(
        file="Le_manzaraka,_le_grand_mariage_(musée_de_Mayotte)_(34751468196).jpg",
        caption="La chambre nuptiale du manzaraka, le grand mariage mahorais (musée de Mayotte)",
        island="culture", author="Jean-Pierre Dalbéra", license="CC BY 2.0"),
    "bijoux_mariage": dict(
        file="Bijoux_d'un_grand_mariage_Comorien.jpg",
        caption="Parure de bijoux en or offerte lors d'un grand mariage comorien",
        island="culture"),
    "kofia_couture": dict(
        file="Woman_sewing_Kofia.jpg",
        caption="Brodeuse confectionnant une kofia, la calotte traditionnelle des hommes",
        island="culture"),
    "marche_tissus": dict(
        file="Women_selling_colourful_dress_in_Comoros.jpg",
        caption="Étal de tissus colorés sur un marché comorien",
        island="culture"),
    "comorienne": dict(
        file="Comorian_Woman.jpg",
        caption="Femme comorienne en tenue traditionnelle",
        island="culture"),

    # ------------------------------------------------------------------ Vidéos
    "v_baleine": dict(
        file="032_Humpback_whale_lobtailing_in_slow_motion_Video_by_Giles_Laurent.webm",
        caption="Baleine à bosse frappant la surface de sa nageoire caudale, au ralenti",
        island="archipel", author="Giles Laurent", license="CC BY-SA 4.0",
        kind="video", poster="baleine"),
    "v_tortues": dict(
        file="Green_sea_turtles_(Chelonia_mydas)_mating.webm",
        caption="Tortues vertes dans leur milieu naturel",
        island="archipel", kind="video", poster="tortue_pilote"),
    "v_bebe_tortue": dict(
        file="Baby_turtle.webm",
        caption="Une jeune tortue rejoint l'océan après l'éclosion",
        island="archipel", kind="video", poster="tortue_ngouja"),
    "v_recif": dict(
        file="Tropical_Fish_Banner_Fish_on_Coral_Reef.webm",
        caption="Poissons-bannières sur un récif corallien de l'océan Indien",
        island="archipel", kind="video", poster="lagon_dembeni"),
    "v_vagues": dict(
        file="Waves_of_the_sea_(Video).webm",
        caption="Le ressac de l'océan Indien sur le rivage",
        island="archipel", kind="video", poster="itsandra"),
}

# Ordre des îles pour les filtres de la galerie
ISLAND_LABELS = {
    "gc": "Grande Comore",
    "moheli": "Mohéli",
    "anjouan": "Anjouan",
    "mayotte": "Mayotte",
    "archipel": "Faune & flore",
    "histoire": "Histoire",
    "culture": "Culture",
}

for _key, _m in MEDIA.items():
    _m.setdefault("kind", "image")
    _m.setdefault("gallery", _m["kind"] == "image")
    _m.setdefault("author", None)
    _m.setdefault("license", None)
    _m["key"] = _key
