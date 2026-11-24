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
}

T = "https://www.tradeinn.com/trekkinn/en/"
E = "https://www.tradeinn.com/techinn/en/"
OGL = "https://www.outdoorgearlab.com/reviews/"

def P(shop, path, name, desc, say=None, src=None, img=None, price=None, checked=None):
    """say: ("review", text) for what an independent reviewer found, ("buyers", text) for what customer reviews say,
    ("note", text) for a fact worth knowing.
    src: (site name, url) for a review. Text is our own summary, never a quote."""
    """Tradeinn shops: path = slug/id (url and image built automatically). Other shops: path = the full product URL,
    img = the product image URL from the shop's product feed (only if the programme allows feed images), price = a
    display string such as "1 299 kr", checked = the date the price was checked ("2026-11-24"). Prices older than
    14 days are hidden automatically, so a stale price never shows."""
    url = path if path.startswith("http") else (T if shop == "trekkinn" else E) + path + "/p"
    return dict(shop=shop, url=url, name=name, desc=desc, say=say, src=src, img=img, price=price, checked=checked)

PRODUCTS = {
    "powerbank-kulde": [
        P("techinn", "anker-a1388g11-power-bank-10000mah/141770458", "Anker Power Bank 10,000 mAh (22.5 W)",
          "USB-C and USB-A ports, 22.5 W output and about 250 g. Enough for roughly two phone charges.",
          ("buyers", "Rated 4.7 of 5 by more than 300 buyers at Best Buy, mostly for its size and reliability. A few found it charges a little slower than a 20 W wall charger. Keep it inside your jacket in the cold."),
          ("Best Buy", "https://www.bestbuy.com/site/reviews/anker-power-bank-10000mah-22-5w-black/6587879")),
        P("techinn", "samsung-eb-p3401xue-10000mah-25w-power-bank/143661434", "Samsung 10,000 mAh 25 W",
          "Two USB-C ports with 25 W fast charging when one device is connected. A good match for phones that support Samsung Super Fast Charging.",
          ("review", "Australian consumer group CHOICE recommended the previous version (P3400) with a 75% score, citing very good capacity and a recharge time of about two hours. Fast charging only applies with one device connected."),
          ("CHOICE", "https://www.choice.com.au/products/electronics-and-technology/phones/mobile-phones/samsung-10000mah-battery-pack-p3400")),
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
          ("Jeger.no", "https://www.jeger.no/jaktutstyr/telt/test-av-sydvang-skaring-ultralight")),
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
          ("Villmarksbutikken", "https://www.villmarksbutikken.net/turutstyr/vintersovepose/"), price="1 659 kr", checked="2026-11-24"),
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
          ("Therm-a-Rest", "https://www.thermarest.com/mattresses/fast-light/z-lite"), price="829 kr", checked="2026-11-24"),
        P("outnorth", "https://www.outnorth.com/no/varemerker/exped/exped-ultra-8r-m-greygoose-P490-8889", "Exped Ultra 8R",
          "Isolert luftunderlag med R-verdi 8,8, laget for vinterturer og kalde netter på snø.",
          ("note", "Med så høy R-verdi trenger du normalt ikke et ekstra skumunderlag under, selv i kulde."),
          ("Exped", "https://www.expedusa.com/products/ultra-8r"), price="2 271 kr", checked="2026-11-24"),
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
    "en": dict(h="Where to buy", btn="See price at {shop}", ad="Affiliate link", review="What reviewers say", notel="Good to know", buyers="What buyers say", price="About {price} (checked {date})",
               note="We may earn a commission if you buy through these links. Prices include VAT for buyers in the EU. Buyers outside the EU, including Norway, may pay VAT, duty and fees on delivery."),
    "no": dict(h="Hvor kan du kjøpe", btn="Se pris hos {shop}", ad="Annonselenke", review="Dette sier testene", notel="Verdt å vite", buyers="Dette sier kjøperne",
               note="Vi kan få provisjon hvis du kjøper via disse lenkene. Prisene kan ha endret seg siden vi sjekket dem.", price="Ca. {price} (sjekket {date})"),
}


def cards(lang, slug_no, prefix=""):
    items = [p for p in PRODUCTS.get(slug_no, []) if SHOPS[p["shop"]]["link"] and lang in SHOPS[p["shop"]]["langs"]]
    if not items:
        return ""
    t = L[lang]
    out = []
    for p in items:
        s = SHOPS[p["shop"]]
        url = p["url"]
        target = url[len(s["strip"]):] if s.get("strip") and url.startswith(s["strip"]) else url
        href = s["link"].format(url=quote(target, safe=""), sub=f"{slug_no}-{lang}")
        im = img(p)
        pic = f'<img class="pimg" src="{escape(im)}" alt="{escape(p["name"])}" loading="lazy" width="400" height="400">' if im else ""
        pr = ""
        if p.get("price") and p.get("checked"):
            import datetime as _d
            age = (_d.date.today() - _d.date.fromisoformat(p["checked"])).days
            if age <= 14:
                d = _d.date.fromisoformat(p["checked"])
                pr = f'<p class="pprice">{escape(t["price"].format(price=p["price"], date=f"{d.day}.{d.month}."))}</p>'
        say = ""
        if p["say"]:
            kind, text = p["say"]
            srcl = f' <a href="{escape(p["src"][1])}" target="_blank" rel="noopener">{escape(p["src"][0])}</a>' if p["src"] else ""
            say = f'<p class="psay"><strong>{t[{"review": "review", "buyers": "buyers"}.get(kind, "notel")]}:</strong> {escape(text)}{srcl}</p>'
        out.append(f'<div class="pcard">{pic}'
                   f'<h3>{escape(p["name"])}</h3><p class="pdesc">{escape(p["desc"])}</p>{pr}{say}'
                   f'<a class="pbtn" href="{escape(href)}" rel="sponsored nofollow noopener" target="_blank">{t["btn"].format(shop=s["name"])}</a>'
                   f'<span class="adlabel">{t["ad"]}</span></div>')
    return f'<section class="products"><h2>{t["h"]}</h2><div class="pgrid">{"".join(out)}</div><p class="pnote">{t["note"]}</p></section>'
