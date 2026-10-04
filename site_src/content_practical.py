"""Préparer son voyage : informations pratiques.

Ces informations sont générales. Les règles (visas, santé, transports) évoluent :
chaque page invite le lecteur à vérifier auprès des sources officielles.
"""

PRACTICAL = [
    dict(
        slug="comment-venir",
        name="Comment venir",
        icon="plane",
        hero="barge",
        summary="Aéroports, compagnies et routes aériennes vers la Grande Comore et Mayotte.",
        sections=[
            dict(title="Les aéroports internationaux", html="""
<ul>
  <li><strong>Grande Comore — aéroport Prince Saïd Ibrahim (HAH)</strong>, à Hahaya, à une
  vingtaine de kilomètres au nord de Moroni. C'est la principale porte d'entrée de l'Union des
  Comores.</li>
  <li><strong>Mayotte — aéroport de Dzaoudzi-Pamandzi (DZA)</strong>, sur Petite-Terre.
  Comptez ensuite la barge pour rejoindre Mamoudzou.</li>
  <li>Anjouan (Ouani) et Mohéli (Bandar Es Salam) disposent d'aérodromes desservis par des vols
  régionaux.</li>
</ul>
"""),
            dict(title="Depuis l'Europe", html="""
<p>Mayotte est reliée à la métropole par des vols directs ou avec escale (souvent via
La Réunion ou une ville d'Afrique de l'Est). Pour la Grande Comore, les itinéraires les plus
courants passent par Nairobi, Addis-Abeba, Dar es Salaam, le Golfe, La Réunion ou Mayotte, selon
les compagnies. Comptez entre 11 et 16&nbsp;heures de trajet selon les correspondances.</p>
"""),
            dict(title="Depuis l'océan Indien et l'Afrique", html="""
<p>Des vols réguliers relient l'archipel à La Réunion, à Madagascar et à l'Afrique de l'Est.
Ces lignes évoluent fréquemment&nbsp;: comparez les offres et vérifiez les horaires peu avant le
départ.</p>
"""),
            dict(title="Par la mer", html="""
<p>Il n'existe pas de ligne régulière de croisière vers l'archipel, mais des bateaux relient
les îles entre elles (voir [[preparer-son-voyage/se-deplacer.html|Se déplacer]]). Les
plaisanciers trouveront des mouillages abrités, notamment dans le lagon de Mayotte.</p>
"""),
        ],
    ),
    dict(
        slug="formalites",
        name="Visas & formalités",
        icon="passport",
        hero="moroni_port",
        summary="Passeport, visa à l'arrivée pour l'Union des Comores, règles spécifiques pour Mayotte.",
        sections=[
            dict(title="Union des Comores", html="""
<ul>
  <li>Un <strong>passeport</strong> valide au moins six mois après la date de retour est exigé.</li>
  <li>Un <strong>visa</strong> est délivré à l'arrivée à l'aéroport pour la plupart des
  nationalités. Son prix et sa durée sont fixés par les autorités comoriennes&nbsp;: renseignez-vous
  auprès de l'ambassade des Comores avant de partir.</li>
  <li>Un billet de retour ou de continuation et une adresse d'hébergement peuvent être demandés.</li>
</ul>
"""),
            dict(title="Mayotte", html="""
<ul>
  <li>Mayotte est un département français, mais <strong>ne fait pas partie de l'espace
  Schengen</strong>.</li>
  <li>Les citoyens de l'Union européenne y entrent avec une carte d'identité ou un passeport
  en cours de validité.</li>
  <li>Les ressortissants soumis à visa doivent obtenir un visa spécifiquement valable pour
  Mayotte&nbsp;: un visa Schengen ordinaire ne suffit pas.</li>
</ul>
"""),
            dict(title="Voyager entre l'Union des Comores et Mayotte", html="""
<p>Le passage entre Mayotte et les îles de l'Union est un passage de frontière&nbsp;: emportez
toujours votre passeport et vérifiez les conditions d'entrée de chaque côté avant de réserver
un vol ou un bateau entre Anjouan, la Grande Comore et Mayotte.</p>
<div class="notice">Les règles d'entrée peuvent changer à tout moment. Consultez les sites
officiels (ambassades, ministères des Affaires étrangères) avant chaque voyage.</div>
"""),
        ],
    ),
    dict(
        slug="quand-partir",
        name="Quand partir ?",
        icon="calendar",
        hero="itsandra",
        summary="Climat tropical, saison sèche de mai à octobre, baleines de juillet à octobre.",
        sections=[
            dict(title="Deux grandes saisons", html="""
<ul>
  <li><strong>Saison sèche et fraîche (kusi), de mai à octobre&nbsp;:</strong> températures
  agréables (23 à 28&nbsp;°C), peu de pluie, alizés. C'est la meilleure période pour la randonnée et
  la plongée.</li>
  <li><strong>Saison chaude et humide (kashkazi), de novembre à avril&nbsp;:</strong> chaleur
  (28 à 32&nbsp;°C), averses parfois violentes et risque de cyclones, surtout de janvier à mars.
  La végétation est luxuriante et les fruits abondent.</li>
</ul>
"""),
            dict(title="Le calendrier de la nature", html="""
<table class="table">
  <thead><tr><th>Période</th><th>À ne pas manquer</th></tr></thead>
  <tbody>
    <tr><td>Juillet à octobre</td><td>Baleines à bosse dans tout l'archipel</td></tr>
    <tr><td>Toute l'année</td><td>Ponte des tortues vertes, avec des pics variables selon les plages</td></tr>
    <tr><td>Mai à octobre</td><td>Randonnées (Karthala, Ntingui, Choungui)</td></tr>
    <tr><td>Novembre à janvier</td><td>Saison des litchis et des mangues</td></tr>
  </tbody>
</table>
"""),
            dict(title="Le calendrier culturel", html="""
<p>Juillet et août sont la saison des <strong>grands mariages</strong>, quand la diaspora revient
au pays&nbsp;: ambiance festive garantie, mais vols et hébergements plus chers. Pendant le
<strong>ramadan</strong>, dont les dates varient chaque année, le rythme de vie change&nbsp;: les
journées sont calmes, les soirées très animées. Consultez notre [[agenda.html|agenda]].</p>
"""),
        ],
    ),
    dict(
        slug="se-deplacer",
        name="Se déplacer",
        icon="boat",
        hero="barge",
        summary="Vols et bateaux entre les îles, taxis collectifs, location de voiture, barge de Mayotte.",
        sections=[
            dict(title="Entre les îles", html="""
<p>Des <strong>vols régionaux</strong> relient la Grande Comore, Mohéli, Anjouan et Mayotte en
30 à 45&nbsp;minutes. Des <strong>bateaux</strong> (vedettes et ferries) assurent aussi des
traversées, plus économiques mais dépendantes de la météo. Les horaires sont souvent modifiés&nbsp;:
reconfirmez la veille et prévoyez une marge dans votre itinéraire.</p>
<div class="notice"><strong>Sécurité en mer&nbsp;:</strong> n'embarquez que sur des navires
officiels, munis de gilets de sauvetage, et renoncez si la mer est forte. N'empruntez jamais
d'embarcations de fortune.</div>
"""),
            dict(title="Sur chaque île", html="""
<ul>
  <li><strong>Taxis collectifs&nbsp;:</strong> le moyen le plus courant et le plus économique. Le
  prix se fixe par trajet&nbsp;; demandez-le avant de monter.</li>
  <li><strong>Voiture avec chauffeur&nbsp;:</strong> recommandée à Anjouan et à Mohéli, où les
  routes sont étroites et sinueuses.</li>
  <li><strong>Location de voiture&nbsp;:</strong> possible en Grande Comore et à Mayotte. On roule
  à droite. Permis international conseillé dans l'Union des Comores.</li>
</ul>
"""),
            dict(title="À Mayotte", media="barge", html="""
<p>La <strong>barge</strong> relie Mamoudzou (Grande-Terre) à Dzaoudzi (Petite-Terre) à
intervalles réguliers. La circulation est dense aux heures de pointe autour de Mamoudzou&nbsp;:
anticipez vos trajets, notamment pour rejoindre l'aéroport.</p>
"""),
        ],
    ),
    dict(
        slug="sante-securite",
        name="Santé & sécurité",
        icon="health",
        hero="moroni_medina",
        summary="Vaccins, paludisme, eau, soleil, assurance et conseils de prudence.",
        sections=[
            dict(title="Avant le départ", html="""
<ul>
  <li>Consultez un médecin ou un centre de vaccinations internationales 4 à 6&nbsp;semaines avant
  le départ.</li>
  <li>Mettez à jour vos vaccins habituels. Selon votre parcours, d'autres vaccins peuvent être
  recommandés (hépatites, typhoïde…). Un certificat contre la fièvre jaune peut être exigé si vous
  arrivez d'un pays où elle est présente.</li>
  <li>Le <strong>paludisme</strong> est présent dans l'Union des Comores&nbsp;: demandez conseil sur
  un traitement préventif.</li>
  <li>Souscrivez une <strong>assurance voyage</strong> couvrant le rapatriement sanitaire&nbsp;: les
  structures médicales sont limitées, surtout à Mohéli et Anjouan.</li>
</ul>
"""),
            dict(title="Sur place", html="""
<ul>
  <li>Buvez de l'eau en bouteille ou filtrée et lavez-vous souvent les mains.</li>
  <li>Protégez-vous des moustiques (dengue, chikungunya, paludisme)&nbsp;: répulsif, vêtements
  longs le soir, moustiquaire.</li>
  <li>Le soleil est très intense&nbsp;: chapeau, crème, hydratation.</li>
  <li>En mer, méfiez-vous des courants et des poissons venimeux&nbsp;: portez des chaussons.</li>
</ul>
"""),
            dict(title="Sécurité", html="""
<p>L'archipel est globalement accueillant et la petite délinquance y reste limitée, même si
des précautions s'imposent à Mayotte, notamment la nuit dans certains quartiers et sur
certaines routes. Ne laissez rien de visible dans les véhicules, évitez de marcher seul après la
tombée de la nuit et suivez les conseils de vos hôtes.</p>
<div class="notice">Avant de partir, consultez les conseils aux voyageurs de votre ministère des
Affaires étrangères, régulièrement mis à jour.</div>
"""),
            dict(title="Numéros utiles", html="""
<ul>
  <li><strong>Mayotte&nbsp;:</strong> 112 (urgences européennes), 15 (SAMU), 17 (police), 18 (pompiers).</li>
  <li><strong>Union des Comores&nbsp;:</strong> notez les numéros fournis par votre hébergeur et
  votre ambassade dès votre arrivée.</li>
</ul>
"""),
        ],
    ),
    dict(
        slug="argent-et-budget",
        name="Argent & budget",
        icon="coin",
        hero="moroni_port_2",
        summary="Franc comorien et euro, distributeurs, cartes bancaires et ordre de prix.",
        sections=[
            dict(title="Les monnaies", html="""
<ul>
  <li><strong>Union des Comores&nbsp;:</strong> le <strong>franc comorien (KMF)</strong>, à
  parité fixe avec l'euro (environ 492&nbsp;KMF pour 1&nbsp;€). L'euro s'échange facilement dans
  les banques et bureaux de change.</li>
  <li><strong>Mayotte&nbsp;:</strong> l'<strong>euro</strong>.</li>
</ul>
"""),
            dict(title="Cartes et distributeurs", html="""
<p>À Mayotte, cartes bancaires et distributeurs sont courants. Dans l'Union des Comores, les
distributeurs se trouvent surtout à Moroni et à Mutsamudu, et sont très rares à Mohéli&nbsp;; les
cartes ne sont acceptées que dans quelques hôtels. Prévoyez donc des espèces en euros, à changer
sur place.</p>
"""),
            dict(title="Ordre de prix", html="""
<table class="table">
  <thead><tr><th>Poste</th><th>Union des Comores</th><th>Mayotte</th></tr></thead>
  <tbody>
    <tr><td>Repas simple</td><td>Bon marché</td><td>Modéré</td></tr>
    <tr><td>Chambre d'hôtes</td><td>Modéré</td><td>Modéré à élevé</td></tr>
    <tr><td>Sortie en mer / plongée</td><td>Modéré</td><td>Modéré à élevé</td></tr>
    <tr><td>Vols inter-îles</td><td colspan="2">Élevés au regard des distances</td></tr>
  </tbody>
</table>
<p>Les pourboires ne sont pas obligatoires mais toujours appréciés pour les guides et
chauffeurs.</p>
"""),
        ],
    ),
    dict(
        slug="hebergement",
        name="Où dormir",
        icon="bed",
        hero="nioumachoua_ilots",
        summary="Hôtels, écolodges, chambres d'hôtes et gîtes chez l'habitant sur les quatre îles.",
        sections=[
            dict(title="Les types d'hébergement", html="""
<ul>
  <li><strong>Hôtels&nbsp;:</strong> surtout à Moroni, sur la côte nord de la Grande Comore, à
  Mutsamudu et à Mayotte.</li>
  <li><strong>Écolodges et bungalows&nbsp;:</strong> la formule idéale à Mohéli, près des îlots et
  des plages de ponte.</li>
  <li><strong>Chambres d'hôtes et gîtes&nbsp;:</strong> nombreux à Mayotte, ils permettent de
  rencontrer les habitants.</li>
  <li><strong>Chez l'habitant&nbsp;:</strong> dans les villages, des familles accueillent les
  voyageurs, une immersion précieuse.</li>
</ul>
"""),
            dict(title="Où séjourner sur chaque île ?", html="""
<ul>
  <li><strong>[[iles/grande-comore.html|Grande Comore]]&nbsp;:</strong> Moroni pour la
  culture, le nord (Mitsamiouli) pour les plages.</li>
  <li><strong>[[iles/moheli.html|Mohéli]]&nbsp;:</strong> le sud de l'île, autour de
  Nioumachoua et d'Itsamia.</li>
  <li><strong>[[iles/anjouan.html|Anjouan]]&nbsp;:</strong> Mutsamudu, puis une nuit dans
  les hauts ou sur la côte sud.</li>
  <li><strong>[[iles/mayotte.html|Mayotte]]&nbsp;:</strong> Petite-Terre pour l'arrivée, le
  sud ou l'ouest de Grande-Terre pour les plages et la tranquillité.</li>
</ul>
"""),
            dict(title="Conseils", html="""
<p>L'offre est limitée et se remplit vite en juillet-août. Réservez tôt, confirmez votre arrivée
la veille et vérifiez l'accès à l'eau et à l'électricité, parfois intermittent. À Mayotte,
demandez si l'établissement a rouvert après le cyclone de décembre&nbsp;2024.</p>
"""),
        ],
    ),
    dict(
        slug="langues-et-coutumes",
        name="Langues & savoir-vivre",
        icon="chat",
        hero="moroni_ancienne_mosquee",
        summary="Shikomori, français et arabe, tenue vestimentaire, photos, ramadan : les clés d'un voyage respectueux.",
        sections=[
            dict(title="Les langues", html="""
<p>La langue commune est le <strong>shikomori</strong> (comorien), langue bantoue proche du
swahili, qui se décline en <em>shingazidja</em>, <em>shimwali</em>, <em>shindzuani</em> et
<em>shimaore</em>. Le <strong>français</strong> est largement compris et l'<strong>arabe</strong>
est langue officielle dans l'Union des Comores. À Mayotte, on parle aussi le
<strong>kibushi</strong>, une langue d'origine malgache.</p>
"""),
            dict(title="Quelques mots", html="""
<table class="table">
  <thead><tr><th>Français</th><th>Comorien</th></tr></thead>
  <tbody>
    <tr><td>Merci</td><td>Marahaba</td></tr>
    <tr><td>Bienvenue</td><td>Karibu</td></tr>
    <tr><td>Au revoir</td><td>Kwaheri</td></tr>
  </tbody>
</table>
<p>Les formules de salutation varient d'une île à l'autre&nbsp;: un effort pour les apprendre est
toujours accueilli avec le sourire.</p>
"""),
            dict(title="Bonnes pratiques", html="""
<ul>
  <li><strong>Tenue&nbsp;:</strong> en dehors des plages, couvrez épaules et genoux, en particulier
  dans les villages et les lieux de culte.</li>
  <li><strong>Photos&nbsp;:</strong> demandez toujours l'autorisation avant de photographier
  quelqu'un, surtout les femmes et les enfants.</li>
  <li><strong>Religion&nbsp;:</strong> l'islam rythme la vie quotidienne. Le vendredi midi est
  consacré à la prière.</li>
  <li><strong>Ramadan&nbsp;:</strong> évitez de manger, boire ou fumer en public pendant la
  journée.</li>
  <li><strong>Hospitalité&nbsp;:</strong> si l'on vous invite, accepter un thé ou un repas est une
  marque de respect.</li>
</ul>
"""),
            dict(title="Infos express", html="""
<table class="table">
  <tbody>
    <tr><th>Fuseau horaire</th><td>UTC+3 toute l'année</td></tr>
    <tr><th>Électricité</th><td>220-230 V, prises européennes (types C et E)</td></tr>
    <tr><th>Indicatifs</th><td>+269 (Union des Comores), +262 (Mayotte)</td></tr>
    <tr><th>Conduite</th><td>À droite</td></tr>
  </tbody>
</table>
"""),
        ],
    ),
]

PRACTICAL_BY_SLUG = {p["slug"]: p for p in PRACTICAL}
