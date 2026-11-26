"""Product cards with affiliate links, shown under a guide.
SHOPS: one entry per shop. "link" is the network's deeplink template with {url} (URL-encoded product address)
and {sub} (guide slug + language, so sales can be traced per guide). A shop with an empty "link" is skipped.
"langs" lists the site languages the shop may be shown on. Tradeinn is not VOEC-registered, so Norwegian
buyers pay VAT, possible duty and a clearance fee on arrival: Tradeinn shops are shown on /en/ only.
PRODUCTS: Norwegian guide slug -> list of P(...) entries: shop, path, name, description, optional review/note and source.
Texts summarise reviews in our own words; we compare, we do not test ourselves."""
from urllib.parse import quote
from html import escape

# Daisycon deeplinks (Material -> Deeplinks, media 450174). Tradeinn's "dl" is the path after www.tradeinn.com/,
# so {url} is the URL-encoded path. Each Tradeinn shop is its own Daisycon campaign (si) with its own link id (li).
TRADEINN = "https://partners.tradeinn.com/c/?si={si}&li={li}&wi=450174&ws={{sub}}&dl={{url}}"

# Awin deeplinks (publisher 3160360): clickref = guide slug + language, so sales show per guide in Awin.
AWIN = "https://www.awin1.com/cread.php?awinmid={mid}&awinaffid=3160360&clickref={{sub}}&ued={{url}}"

SHOPS = {
    "trekkinn": dict(name="Trekkinn", link=TRADEINN.format(si=20618, li=1874240), langs=["en"], strip="https://www.tradeinn.com/"),
    "techinn": dict(name="Techinn", link=TRADEINN.format(si=20616, li=1874238), langs=["en"], strip="https://www.tradeinn.com/"),
    # Awin shops: {url} = the full product URL, URL-encoded. Add a shop here only when it shows as "Joined" in Awin.
    "outnorth": dict(name="Outnorth", link=AWIN.format(mid=18620), langs=["no"]),
    "db": dict(name="Db", link=AWIN.format(mid=109844), langs=["no"]),
}

# Products shown only in the shop (not under a guide): key -> heading per language. Their clickref is "<key>-<lang>".
SHOP_ONLY = {"sekker": {"no": "Sekker og bagger", "en": "Backpacks and bags"}}

T = "https://www.tradeinn.com/trekkinn/en/"
E = "https://www.tradeinn.com/techinn/en/"
OGL = "https://www.outdoorgearlab.com/reviews/"

def P(shop, path, name, desc, say=None, src=None, img=None, price=None, checked=None, pick=None, spec=None):
    """say: ("review", text) for what an independent reviewer found, ("buyers", text) for what customer reviews say,
    ("note", text) for a fact worth knowing.
    src: (site name, url) for a review. Text is our own summary, never a quote."""
    """Tradeinn shops: path = slug/id (url and image built automatically). Other shops: path = the full product URL,
    img = the product image URL from the shop's product feed (only if the programme allows feed images), price = a
    display string such as "1 299 kr", checked = the date the price was checked ("2026-11-24"). Prices older than
    14 days are hidden automatically, so a stale price never shows."""
    """Buying guides: pick = a short label per language, e.g. {"no": "Best i kulda", "en": "Best in the cold"}, and
    spec = the key figure per language, e.g. {"no": "350 lumen, 94 g", "en": "350 lumens, 94 g"}. Products with a pick
    are listed in a comparison table near the top of the guide ("Våre valg"), in the order they appear here."""
    url = path if path.startswith("http") else (T if shop == "trekkinn" else E) + path + "/p"
    return dict(shop=shop, url=url, name=name, desc=desc, say=say, src=src, img=img, price=price, checked=checked, pick=pick, spec=spec)

DBJ = "https://dbjourney.com/en-no/products/"
DBI = "https://dbjourney.com/cdn/shop/files/"

PRODUCTS = {
    "sekker": [
        P("db", DBJ + "backcountry-backpack-25l-white-noise", "Db Backcountry Backpack 25L",
          "Toppturssekk på 25 liter og 1,35 kg, med feste for ski eller brett, isøks og hjelm, og eget rom for skredutstyr.",
          ("note", "Laget av resirkulert nylon. Produsenten oppgir ikke at sekken er vanntett, så ha viktige ting i en tørrsekk."),
          img=DBI + "Backcountry_Backpack_25L_White_Noise_1000181014401_1.png?width=600", price="1 999 kr", checked="2026-11-26"),
        P("db", DBJ + "hugger-backpack-30l-black-out", "Db Hugger Backpack 30L",
          "Sekk på 30 liter og 1,23 kg til reise og hverdag, med polstret rom for PC opptil 16 tommer. Passer som håndbagasje.",
          ("note", "Tåler lett regn ifølge produsenten, men er ikke helt vanntett. Mer reisesekk enn tursekk."),
          img=DBI + "Hugger_30L_Black_Out_New_Image_11.png?width=600", price="2 299 kr", checked="2026-11-26"),
        P("db", DBJ + "ramverk-backpack-21l-black-out", "Db Ramverk Backpack 21L",
          "Kompakt sekk på 21 liter og 1,08 kg med polstret PC-rom som åpnes fra ryggsiden.",
          ("note", "Til pendling og dagsturer i byen heller enn i fjellet."),
          img=DBI + "Ramverk_Backpack_21L_Black_Out_1.png?width=600", price="2 199 kr", checked="2026-11-26"),
    ],
    "powerbank-kulde": [
        P("techinn", "anker-a1388g11-power-bank-10000mah/141770458", "Anker Power Bank 10,000 mAh (22.5 W)",
          "USB-C and USB-A ports, 22.5 W output and about 250 g. Enough for roughly two phone charges.",
          ("buyers", "Rated 4.7 of 5 by more than 300 buyers at Best Buy, mostly for its size and reliability. A few found it charges a little slower than a 20 W wall charger. Keep it inside your jacket in the cold."),
          ("Best Buy", "https://www.bestbuy.com/site/reviews/anker-power-bank-10000mah-22-5w-black/6587879")),
        P("techinn", "samsung-eb-p3401xue-10000mah-25w-power-bank/143661434", "Samsung 10,000 mAh 25 W",
          "Two USB-C ports with 25 W fast charging when one device is connected. A good match for phones that support Samsung Super Fast Charging.",
          ("review", "Australian consumer group CHOICE recommended the previous version (P3400) with a 75% score, citing very good capacity and a recharge time of about two hours. Fast charging only applies with one device connected."),
          ("CHOICE", "https://www.choice.com.au/products/electronics-and-technology/phones/mobile-phones/samsung-10000mah-battery-pack-p3400")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/biolite/biolite-charge-80-pd-grey-orange", "BioLite Charge 80 PD",
          "Powerbank på 20 000 mAh med USB-C PD og to USB-A-utganger, rundt 450 g. Nok til flere mobilladinger på en lang tur.",
          ("review", "T3 ga den sin anbefaling for robust bygg, stor kapasitet og at alle tre utgangene kan brukes samtidig. Minus for høy pris og at lampene bare viser fire nivåer, ikke prosent."),
          ("T3", "https://www.t3.com/reviews/biolite-charge-pd-80-portable-power-bank-review"),
          img="https://www.outnorth.com/assets/blobs/biolite-charge-80-pd-grey-orange-89ec71131d.jpeg", price="999 kr", checked="2026-11-24"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/gp-batterier/gp-batterier-powerbank-m2-20000-mah-grey-FS647916", "GP Powerbank M2+ 20 000 mAh",
          "Rimelig powerbank på 20 000 mAh med hurtiglading, godt egnet som reserve på hytta eller i pulken.",
          ("note", "Litiumbatterier gir mindre strøm når de er kalde. Ha powerbanken i en innerlomme eller i soveposen om natten."),
          img="https://www.outnorth.com/assets/blobs/405205-3fc337a1-08e1e753e9.png"),
    ],
    "skalljakke-eller-regnjakke": [
        P("trekkinn", "columbia-pouring-adventure--iii-jacket/140985428", "Columbia Pouring Adventure III",
          "Light, packable rain jacket with Columbia's Omni-Tech waterproof and breathable membrane.",
          ("buyers", "Trekkinn buyers say it keeps the rain out, but one reports heavy condensation inside on active walks. Best for summer hikes and everyday use rather than as a full mountain shell."),
          ("Trekkinn reviews", "https://www.tradeinn.com/trekkinn/en/columbia-pouring-adventure--iii-jacket/140985425/p")),
        P("trekkinn", "columbia-watertight--ii-jacket/140983790", "Columbia Watertight II",
          "Simple, packable rain jacket at a low price, with a hood and zipped hand pockets.",
          ("review", "OutdoorGearLab found it one of the cheapest jackets in its test, with fair rain protection for the money and good use as a windbreaker."),
          ("OutdoorGearLab", OGL + "clothing-mens/rain-jacket/columbia-watertight-ii")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/bergans/bergans-essentials-2-5l-shell-jacket-men-black-FS662890", "Bergans Essentials 2.5L Shell Jacket",
          "Lett og pakkbar 2,5-lags skalljakke med Bergans' egen membran og PFAS-fri impregnering. God til fotturer og hverdag.",
          ("note", "2,5-lags jakker er lettere og billigere enn 3-lags, men tåler mindre slitasje fra tung sekk og klatring over tid."),
          img="https://www.outnorth.com/assets/blobs/images2-shell2-5-0912226ade.png"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/urberg/urberg-3l-shell-jacket-men-mediterranea-FS552541", "Urberg 3L Shell Jacket",
          "Tre-lags skalljakke med stretch, vanntette glidelåser og ventilasjon under armene. Til fjellturer i vind og regn.",
          ("note", "Urberg er Outnorth og Fjellsports eget merke. En 3-lags jakke er mer slitesterk enn en 2,5-lags, men gjerne litt stivere og mer støyende."),
          img="https://www.outnorth.com/assets/blobs/pl11958-pc559-urberg-3l-shell-jacket-men-mediterranea-main-6c9128a967.jpeg"),
    ],
    "lag-pa-lag": [
        P("trekkinn", "icebreaker-260-tech-merino-long-sleeve-base-layer/136879912", "Icebreaker 260 Tech merino top",
          "Midweight base layer in 100% merino wool for cold days. Icebreaker now sells the same top as 260 Oasis.",
          ("review", "OutdoorGearLab rated the 260 Tech as very warm, with merino's typical ability to regulate temperature."),
          ("OutdoorGearLab", OGL + "clothing-womens/base-layer-womens/icebreaker-tech-260-womens")),
        P("trekkinn", "icebreaker-200-oasis-merino-long-sleeve-base-layer/136879888", "Icebreaker 200 Oasis merino top",
          "Lighter 100% merino layer for active days, from spring to autumn and under a fleece in winter.",
          ("review", "Advnture called it a high-performing top for all seasons and activities, though not a cheap one."),
          ("Advnture", "https://www.advnture.com/reviews/icebreaker-200-oasis-long-sleeve-crewe-thermal-top")),
        P("trekkinn", "icebreaker-260-tech-merino-base-layer-pants/136879924", "Icebreaker 260 Tech merino leggings",
          "The matching 260 bottom layer for winter trips and cold nights in the tent.",
          ("review", "Packstack's review rates them as genuinely warm, soft rather than itchy and good at resisting odour on multi-day trips. Some owners report snags and wear after a few months."),
          ("Packstack", "https://www.packstack.io/reviews/clothing/icebreaker-merino-260-tech-thermal-leggings")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/icebreaker/icebreaker-mens-200-oasis-ls-crewe-black", "Icebreaker 200 Oasis LS Crewe",
          "Ullundertrøye i 100 % merino på 200 g/m², med flate sømmer. Et lett innerste lag til aktive turer hele året.",
          ("review", "Advnture kalte den en svært god trøye til alle årstider og aktiviteter, men påpekte at den ikke er billig."),
          ("Advnture", "https://www.advnture.com/reviews/icebreaker-200-oasis-long-sleeve-crewe-thermal-top"),
          img="https://www.outnorth.com/assets/blobs/icebreaker-men-s-200-oasis-longsleeve-crewe-black-22f235935b.jpeg"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/icebreaker/icebreaker-mens-260-tech-leggings-black-monsoon", "Icebreaker 260 Tech Leggings",
          "Tykkere ullongs i 100 % merino, varm nok som innerste lag på vinterturer og kalde netter i teltet.",
          ("review", "Packstack fant dem varme, myke og flinke til å holde lukt borte på flerdagsturer. Noen eiere melder om lo og slitasje etter noen måneder."),
          ("Packstack", "https://www.packstack.io/reviews/clothing/icebreaker-merino-260-tech-thermal-leggings"),
          img="https://www.outnorth.com/assets/blobs/icebreaker-men-s-merino-260-tech-thermal-leggings-black-00e888327c.jpeg"),
    ],
    "tursko-eller-fjellstovler": [
        P("trekkinn", "salomon-quest-5-gore-tex--hiking-boots/142751824", "Salomon Quest 5 GTX",
          "High, supportive Gore-Tex boot for heavy packs, scree and rough terrain.",
          ("review", "OutdoorGearLab ranked it third of 18 hiking boots for its ankle support. RunRepeat's lab test found it heavier than average and not very breathable."),
          ("OutdoorGearLab", OGL + "shoes-and-boots/hiking-boots-men/salomon-quest-5-gore-tex")),
        P("trekkinn", "salomon-x-ultra-360-mid-gore-tex--hiking-boots/140536746", "Salomon X Ultra 360 Mid GTX",
          "Lighter mid-height Gore-Tex boot for day hikes and mixed terrain.",
          ("review", "Men's Fitness tested it on mud, rock and wet trails and was impressed by how light it feels."),
          ("Men's Fitness", "https://mensfitness.co.uk/review/salomon-x-ultra-360-mid-gore-tex/")),
        P("trekkinn", "merrell-moab-3-mid-gore-tex--hiking-boots/139599810", "Merrell Moab 3 Mid GTX",
          "Popular all-round boot with a Vibram sole and Gore-Tex membrane.",
          ("review", "Advnture praised its comfort straight out of the box and roomy toe box. RunRepeat rated the toe-box durability as only average."),
          ("Advnture", "https://www.advnture.com/reviews/merrell-moab-3-mid-gtx")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/salomon/salomon-quest-5-gore-tex-black-deep-lichen-green-black-FS661076", "Salomon Quest 5 GTX",
          "Høy fjellstøvel med Gore-Tex og stivt chassis som gir sidestøtte med tung sekk og i ulendt terreng.",
          ("review", "OutdoorGearLab rangerte den som nummer tre av 18 turstøvler, særlig for ankelstøtten. RunRepeat målte den som tyngre enn snittet og lite pustende."),
          ("OutdoorGearLab", OGL + "shoes-and-boots/hiking-boots-men/salomon-quest-5-gore-tex"),
          img="https://www.outnorth.com/assets/blobs/png-2000px-max-72dpi-94817e6990.jpeg"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/merrell/merrell-moab-3-mid-gtx-m-black-grey", "Merrell Moab 3 Mid GTX",
          "Middels høy tursko med Gore-Tex, Vibram-såle og 5 mm dype knaster. Mykere og lettere enn en fjellstøvel.",
          ("review", "Advnture likte at den er komfortabel rett ut av esken og har god plass til tærne. RunRepeat vurderte slitestyrken i tåpartiet som middels."),
          ("Advnture", "https://www.advnture.com/reviews/merrell-moab-3-mid-gtx"),
          img="https://www.outnorth.com/assets/blobs/merrell-men-s-moab-3-mid-gore-tex-black-grey-7ae1920fea.jpeg"),
    ],
    "velge-telt": [
        P("trekkinn", "salewa-litetrek-iii-tent/136362634", "Salewa Litetrek III",
          "Freestanding three-person tent with one entrance and a vestibule for gear or cooking. Fly 3,000 mm, floor 5,000 mm, around 2.6–3 kg.",
          ("buyers", "A UKClimbing forum user who spent a month in Patagonia with it found it quick to pitch and dry in strong storms, but colder and more wind-buffeted than four-season tents in the mountains."),
          ("UKClimbing forum", "https://www.ukclimbing.com/forums/gear/salewa_litetrek_tent_advice-701779")),
        P("trekkinn", "salewa-denali-ii-tent/136362637", "Salewa Denali II",
          "Two-person, three-season dome with two entrances and two vestibules. About 2.4 kg.",
          ("review", "We Are Explorers found it robust and roomy, but at the heavier end for a two-person tent."),
          ("We Are Explorers", "https://weareexplorers.co/salewa-denali-ii-tent/")),
        P("trekkinn", "salewa-latitude-ii-tent/136473591", "Salewa Latitude II",
          "Light two-person dome that packs small, made for alpine trekking. Two entrances, about 2.7 kg, fly 3,000 mm.",
          ("review", "Swiss consumer programme Kassensturz rated it good in a test of two-person tents: waterproof, robust and with reasonable room for two."),
          ("SRF Kassensturz", "https://www.srf.ch/sendungen/kassensturz-espresso/tests/sport-freizeit-outdoor/camping-zelte-zweierzelte-im-test-undicht-und-kein-platz-fuers-gepaeck")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/sydvang/sydvang-skaring-4-season-tent-haute-red", "Sydvang Skaring 4 Season",
          "Tunneltelt for tre personer, laget for bruk hele året, med stormmatter og to romslige absider.",
          ("note", "Sydvang er Outnorth og Fjellsports eget merke, og prisen er ofte lavere enn for tilsvarende telt fra kjente produsenter."),
          ("Jeger.no", "https://www.jeger.no/jaktutstyr/telt/test-av-sydvang-skaring-ultralight"),
          img="https://www.outnorth.com/assets/blobs/sydvang-skaring-4-season-tent-haute-red-3b87ad4d4c.jpeg"),
    ],
    "sovepose-temperatur": [
        P("trekkinn", "marmot-helium-m14404-sleeping-bag/139716678", "Marmot Helium",
          "Down bag with 800-fill goose down, a water-resistant shell and a lower limit around -9 °C.",
          ("review", "OutdoorGearLab praised the warmth and build quality but marked it down for an awkwardly placed second zip and a high price."),
          ("OutdoorGearLab", OGL + "camping-and-hiking/backpacking-sleeping-bag/marmot-helium-15")),
        P("trekkinn", "haglofs-tarius--18-c-sleeping-bag/137633887", "Haglöfs Tarius -18 °C",
          "Synthetic winter bag: comfort -11 °C, limit -18 °C. Weighs close to 3 kg.",
          ("review", "Villmarksbutikken tested it at a winter camp in Femundsmarka and named it the best budget pick: even warmth all night despite condensation. It is heavy and bulky, so best when you pull a sled."),
          ("Villmarksbutikken", "https://www.villmarksbutikken.net/turutstyr/vintersovepose/")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/haglofs/haglofs-tarius-18-midnight-blue-tangerine", "Haglöfs Tarius -18",
          "Syntetisk vinterpose: komfort -11 °C, grense -18 °C. Veier nær 3 kg.",
          ("review", "Villmarksbutikken testet den på vinterleir i Femundsmarka og kåret den til beste budsjettvalg: jevn varme hele natten, selv med kondens i teltet."),
          ("Villmarksbutikken", "https://www.villmarksbutikken.net/turutstyr/vintersovepose/"),
          img="https://www.outnorth.com/assets/blobs/haglofs-tarius-18-midnight-blue-tangerine-0be25e8952.jpeg", price="1 659 kr", checked="2026-11-24"),
    ],
    "liggeunderlag-r-verdi": [
        P("trekkinn", "sea-to-summit-ether-light-xt-extreme-inflatable-mat/138043159", "Sea to Summit Ether Light XT Extreme",
          "10 cm thick insulated air mat with an R-value of 6.2, made for winter camping.",
          ("review", "BBC Countryfile gave it top marks for comfort and quick inflation, but noted the weight and larger pack size."),
          ("BBC Countryfile", "https://www.countryfile.com/reviews/sea-to-summit-ether-light-xt-extreme-sleeping-mat/")),
        P("trekkinn", "sea-to-summit-ultralight-inflatable-mat/137098785", "Sea to Summit Ultralight Insulated",
          "Insulated air mat with an R-value of about 3 that packs small. For spring to autumn.",
          ("review", "OutdoorsMagic liked the warmth for its weight and how quickly it inflates and deflates."),
          ("OutdoorsMagic", "https://outdoorsmagic.com/article/sea-to-summit-ul-insulated-sleeping-mat-review/")),
        P("outnorth", "https://www.outnorth.com/no/varemerker/therm-a-rest/therm-a-rest-z-lite-sol-regular", "Therm-a-Rest Z Lite SOL",
          "Sammenleggbart skumunderlag med R-verdi 2,0. Kan ikke punktere, og veier rundt 410 g.",
          ("note", "Therm-a-Rest anbefaler det alene om sommeren og under et luftunderlag om vinteren, for ekstra varme og vern mot punktering."),
          ("Therm-a-Rest", "https://www.thermarest.com/mattresses/fast-light/z-lite"),
          img="https://www.outnorth.com/assets/blobs/thermarest-z-lite-sol-regular-limon-silver-27e19bec82.jpeg", price="829 kr", checked="2026-11-24"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/exped/exped-ultra-8r-m-greygoose-P490-8889", "Exped Ultra 8R",
          "Isolert luftunderlag med R-verdi 8,8, laget for vinterturer og kalde netter på snø.",
          ("note", "Med så høy R-verdi trenger du normalt ikke et ekstra skumunderlag under, selv i kulde."),
          ("Exped", "https://www.expedusa.com/products/ultra-8r"),
          img="https://www.outnorth.com/assets/blobs/7640423641416-ultra-8r-m-top-ss26-613e8fc373.png"),
    ],
    "gps-klokke-tur": [
        P("outnorth", "https://www.outnorth.com/no/varemerker/garmin/garmin-instinct-2x-solar-graphite-449948", "Garmin Instinct 2X Solar",
          "Robust turklokke med solcellelading, innebygd lommelykt og opptil 60 timer GPS (lengre med sol). Veier rundt 67 g.",
          ("review", "Advnture likte den lange batteritiden, den sterke lommelykten og at den større kassen ikke ble særlig tyngre. Minus for litt treg respons og at den mangler fullverdige topografiske kart."),
          ("Advnture", "https://www.advnture.com/reviews/garmin-instinct-2x-solar"),
          img="https://www.outnorth.com/assets/blobs/garmin-instinct-2x-solar-graphite-999dd5539c.png", price="4 949 kr", checked="2026-11-24"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/suunto/suunto-race-s-black-P438-7402", "Suunto Race S",
          "Sportsklokke med AMOLED-skjerm, stålramme og opptil 30 timer GPS med alle satellittsystemer. Veier rundt 60 g.",
          ("review", "TechRadar ga 4 av 5 på alle punkter og trakk fram presis GPS, god byggekvalitet og lang batteritid. Klokken er stor og tykk for små håndledd, og kronen er litt klønete i bruk."),
          ("TechRadar", "https://www.techradar.com/health-fitness/fitness-trackers/suunto-race-s-review"),
          img="https://www.outnorth.com/assets/blobs/suunto-race-s-all-black-ss051013000-perspective-quarter-c36-new-year-fireworks-defc3a7c86.jpeg", price="2 690 kr", checked="2026-11-24"),
    ],
    "kikkert-tallene-forklart": [
        P("outnorth", "https://www.outnorth.com/no/varemerker/focus-optics/outdoor-ii-8x42-171280-P403-5437", "Focus Outdoor II 8x42",
          "Vanntett takprismekikkert med 8x forstørrelse og 42 mm objektiv, rundt 500 g. Synsfelt 113 m på 1000 m og skumringsfaktor 18.",
          ("note", "8x42 er et godt allroundvalg på tur: rolig bilde uten stativ og nok lys i skumring. Focus er et svensk merke."),
          img="https://www.outnorth.com/assets/blobs/focus-optics-outdoor-ii-8x42-green-77922a5f79.png", price="1 195 kr", checked="2026-11-24"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/focus-optics/focus-optics-focus-observer-8x42-hd-nocolour-P109-9042", "Focus Observer 8x42 HD",
          "Kraftigere modell i samme 8x42-format, med HD-glass for skarpere bilde og bedre farger enn instegsmodellene.",
          ("note", "HD- eller ED-glass reduserer fargekanter rundt motiver i motlys, noe du merker mest når du ser på fugler mot himmelen."),
          img="https://www.outnorth.com/assets/blobs/800q-01-107925-4c405cd340.png"),
    ],
    "julegaver-til-turfolk": [
        P("outnorth", "https://www.outnorth.com/no/varemerker/woolpower/woolpower-socks-400-black", "Woolpower Socks 400",
          "Ullsokker med frotté i foten, 50 % merinoull. Middels skaft, laget i Sverige.",
          ("note", "Merinoull holder på varmen selv når sokken blir litt fuktig. Ta en størrelse som passer tursko eller skistøvler."),
          img="https://www.fjellsport.no/assets/blobs/woolpower-socks-400-black-749b863b38.jpeg", price="259 kr", checked="2026-11-25",
          pick={"no": "Under 300 kr"}, spec={"no": "50 % merinoull, frotté"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/petzl/tikka-230017-214864-P481-3893", "Petzl Tikka",
          "Hodelykt på 350 lumen og 94 gram, med opptil 110 timers brenntid på tre AAA-batterier eller Petzls oppladbare CORE-batteri.",
          ("note", "Litiumbatterier i AAA-størrelse tåler kulde bedre enn alkaliske og er en fin ekstra liten gave."),
          img="https://www.fjellsport.no/assets/blobs/e061ab02-tikka-highres-822649dc59.jpeg", price="425 kr", checked="2026-11-25",
          pick={"no": "300–700 kr"}, spec={"no": "350 lumen, 94 g"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/stanley/stanley-the-legendary-classic-food-jar-spork-0-4l-black-2-0-P532-4956", "Stanley Legendary Classic Food Jar 0,4 L",
          "Mattermos på 0,4 liter med spork, 340 gram. Holder maten varm i opptil sju timer.",
          ("note", "Forvarm mattermosen med kokende vann i noen minutter før du fyller den, så holder den varmen lenger."),
          img="https://www.fjellsport.no/assets/blobs/st10113530105-1-222428d4f5.png",
          pick={"no": "300–700 kr"}, spec={"no": "0,4 L, 7 t varm"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/woolpower/woolpower-mittens-400-black", "Woolpower Mittens 400",
          "Ullvotter i 70 % merinoull med frotté. Kan brukes alene eller som innervott under en vindtett skallvott.",
          ("note", "Votter er varmere enn fingerhansker fordi fingrene deler på varmen."),
          img="https://www.fjellsport.no/assets/blobs/mittens400-390822ddca.jpeg", price="499 kr", checked="2026-11-25",
          pick={"no": "300–700 kr"}, spec={"no": "70 % merinoull"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/stanley/stanley-the-legendary-classic-bottle-0-94-l-hammertone-green-P481-7601", "Stanley Legendary Classic Bottle 0,94 L",
          "Klassisk ståltermos på 940 ml og 639 gram. Holder drikken varm i opptil et døgn.",
          ("note", "En termos på rundt en liter passer for to personer på dagstur."),
          img="https://www.fjellsport.no/assets/blobs/web-png-square-theclassiclegendaryvacuumbottle1qt-hammertonegreen-front-65f04414aa.png", price="599 kr", checked="2026-11-25",
          pick={"no": "300–700 kr"}, spec={"no": "0,94 L, 24 t varm"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/primus/primus-essential-trail-kit", "Primus Essential Trail Kit",
          "Gassbrenner og 1-liters aluminiumskjele med lokk som også er stekepanne, 382 gram til sammen. Kjelen rommer en liten gasspatron når den pakkes.",
          ("note", "Gass er ikke inkludert. Til vinterbruk bør du velge en gassblanding beregnet for kulde."),
          img="https://www.fjellsport.no/assets/blobs/primus-essential-trail-kit-nocolour-009f32d2f0.jpeg",
          pick={"no": "700–1500 kr"}, spec={"no": "382 g, 1 L kjele"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/biolite/biolite-charge-80-pd-grey-orange", "BioLite Charge 80 PD",
          "Powerbank på 20 000 mAh med USB-C PD og to USB-A-utganger, rundt 450 gram.",
          ("review", "T3 ga den sin anbefaling for robust bygg, stor kapasitet og at alle tre utgangene kan brukes samtidig. Minus for høy pris og at lampene bare viser fire nivåer."),
          ("T3", "https://www.t3.com/reviews/biolite-charge-pd-80-portable-power-bank-review"),
          img="https://www.outnorth.com/assets/blobs/biolite-charge-80-pd-grey-orange-89ec71131d.jpeg", price="999 kr", checked="2026-11-25",
          pick={"no": "700–1500 kr"}, spec={"no": "20 000 mAh, ca. 450 g"}),
        P("outnorth", "https://www.outnorth.com/no/varemerker/woolpower/woolpower-full-zip-jacket-400-forest-green", "Woolpower Full Zip Jacket 400",
          "Ullgenser med hel glidelås i 400 g/m² ullfrotté, tommelhull og elastisk passform. Laget i Sverige.",
          ("note", "Den er ikke vindtett, så den fungerer best som mellomlag under en skalljakke."),
          img="https://www.fjellsport.no/assets/blobs/woolpower-full-zip-jacket-400-forest-green-1-eac35eaa00.jpeg", price="2 199 kr", checked="2026-11-25",
          pick={"no": "Over 1500 kr"}, spec={"no": "400 g/m² ullfrotté"}),
    ],
}


def img(p):
    """The card image: the entry's own img, else the Tradeinn image built from the URL, else none."""
    if p.get("img"):
        return p["img"]
    url = p["url"]
    if "tradeinn.com/" not in url:
        return None
    parts = url.rstrip("/").split("/")
    slug, pid = parts[-3], parts[-2]
    return f"https://www.tradeinn.com/f/{pid[:5]}/{pid}/{slug}.webp"


L = {
    "en": dict(pk_h="Our picks", pk_cols=("Pick", "Product", "Key figures", "Price", ""), pk_btn="See price", pk_more="More about each product further down.",
               h="Where to buy", btn="See price at {shop}", ad="Affiliate link", review="What reviewers say", notel="Good to know", buyers="What buyers say", price="About {price} (checked {date})",
               note="Affiliate links: we may earn a commission. Prices include VAT for buyers in the EU. Buyers outside the EU, including Norway, may pay VAT, duty and fees on delivery."),
    "no": dict(pk_h="Våre valg", pk_cols=("Valg", "Produkt", "Nøkkeltall", "Pris", ""), pk_btn="Se pris", pk_more="Mer om hvert produkt lenger ned.",
               h="Hvor kan du kjøpe", btn="Se pris hos {shop}", ad="Annonselenke", review="Dette sier testene", notel="Verdt å vite", buyers="Dette sier kjøperne",
               note="Annonselenker: vi kan få provisjon. Du betaler det samme.", price="Ca. {price} (sjekket {date})"),
}


def _items(lang, slug_no):
    return [p for p in PRODUCTS.get(slug_no, []) if SHOPS[p["shop"]]["link"] and lang in SHOPS[p["shop"]]["langs"]]


def _href(p, slug_no, lang):
    s = SHOPS[p["shop"]]
    url = p["url"]
    target = url[len(s["strip"]):] if s.get("strip") and url.startswith(s["strip"]) else url
    return s["link"].format(url=quote(target, safe=""), sub=f"{slug_no}-{lang}")


def _fresh_price(p):
    """(price, date) when the price was checked within 14 days, else None."""
    if p.get("price") and p.get("checked"):
        import datetime as _d
        d = _d.date.fromisoformat(p["checked"])
        if (_d.date.today() - d).days <= 14:
            return p["price"], d
    return None


def picks(lang, slug_no, prefix=""):
    """Comparison table of the products that have a pick label, shown near the top of a buying guide."""
    items = [p for p in _items(lang, slug_no) if p.get("pick") and lang in p["pick"]]
    if not items:
        return ""
    t = L[lang]
    rows = []
    for p in items:
        fp = _fresh_price(p)
        price = escape(fp[0]) if fp else "–"
        spec = escape((p.get("spec") or {}).get(lang, ""))
        rows.append(f'<tr><td class="pk-pick">{escape(p["pick"][lang])}</td><td class="pk-name">{escape(p["name"])}</td>'
                    f'<td>{spec}</td><td class="pk-price">{price}</td>'
                    f'<td><a class="pk-btn" href="{escape(_href(p, slug_no, lang))}" rel="sponsored nofollow noopener" target="_blank">{t["pk_btn"]}</a>'
                    f'<span class="adlabel">{t["ad"]}</span></td></tr>')
    head = "".join(f"<th>{c}</th>" for c in t["pk_cols"])
    return (f'<section class="picks"><h2>{t["pk_h"]}</h2><div class="pk-wrap"><table><thead><tr>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div><p class="pnote">{t["pk_more"]}</p></section>')


def _card(p, slug_no, lang):
    t, s = L[lang], SHOPS[p["shop"]]
    href = _href(p, slug_no, lang)
    im = img(p)
    pic = f'<img class="pimg" src="{escape(im)}" alt="{escape(p["name"])}" loading="lazy" width="400" height="400">' if im else ""
    pr = ""
    fp = _fresh_price(p)
    if fp:
        pr = f'<p class="pprice">{escape(t["price"].format(price=fp[0], date=f"{fp[1].day}.{fp[1].month}."))}</p>'
    say = ""
    if p["say"]:
        kind, text = p["say"]
        srcl = f' <a href="{escape(p["src"][1])}" target="_blank" rel="noopener">{escape(p["src"][0])}</a>' if p["src"] else ""
        say = f'<p class="psay"><strong>{t[{"review": "review", "buyers": "buyers"}.get(kind, "notel")]}:</strong> {escape(text)}{srcl}</p>'
    return (f'<div class="pcard">{pic}'
            f'<h3>{escape(p["name"])}</h3><p class="pdesc">{escape(p["desc"])}</p>{pr}{say}'
            f'<a class="pbtn" href="{escape(href)}" rel="sponsored nofollow noopener" target="_blank">{t["btn"].format(shop=s["name"])}</a>'
            f'<span class="adlabel">{t["ad"]}</span></div>')


def cards(lang, slug_no, prefix=""):
    items = _items(lang, slug_no)
    if not items:
        return ""
    t = L[lang]
    out = [_card(p, slug_no, lang) for p in items]
    return f'<section class="products"><h2>{t["h"]}</h2><div class="pgrid">{"".join(out)}</div><p class="pnote">{t["note"]}</p></section>'

SHOP_L = {
    "no": dict(lead="Utvalgte produkter fra guidene våre, samlet på ett sted. Du handler direkte hos nettbutikken.",
               resp_h="Hvem du handler hos",
               resp="Nordic Trail Gear selger ikke varer selv. Når du klikker «Se pris», kommer du til nettbutikken, og det er nettbutikken som er selger. "
                    "Bestilling, betaling, levering, angrerett, retur og reklamasjon avtaler du med butikken, og spørsmål om et kjøp sendes dit.",
               shops="Butikker", count="{n} produkter"),
    "en": dict(lead="Selected products from our guides, gathered in one place. You buy directly from the store.",
               resp_h="Who you buy from",
               resp="Nordic Trail Gear does not sell anything itself. When you click “See price”, you go to the store, and the store is the seller. "
                    "Ordering, payment, delivery, cancellation, returns and complaints are between you and the store, so send any questions about a purchase there.",
               shops="Stores", count="{n} products"),
}


def shop(lang, groups):
    """The shop page: every product from the guides, grouped. groups = [(heading, [guide slugs])]. Each product appears once."""
    t, s = L[lang], SHOP_L[lang]
    seen, secs, names = set(), [], set()
    for heading, slugs in groups:
        out = []
        for slug in slugs:
            for p in _items(lang, slug):
                if p["url"] in seen:
                    continue
                seen.add(p["url"]); names.add(SHOPS[p["shop"]]["name"])
                out.append(_card(p, slug, lang))
        if out:
            secs.append(f'<section class="products shopgrp"><h2>{escape(heading)}</h2><div class="pgrid">{"".join(out)}</div></section>')
    intro = (f'<p class="lede">{s["lead"]}</p><div class="shopinfo"><h2>{s["resp_h"]}</h2><p>{s["resp"]}</p>'
             f'<p><strong>{s["shops"]}:</strong> {escape(", ".join(sorted(names)))} · {s["count"].format(n=len(seen))}</p>'
             f'<p class="pnote">{t["note"]}</p></div>')
    return intro + "".join(secs)
