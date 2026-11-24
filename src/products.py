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

SHOPS = {
    "trekkinn": dict(name="Trekkinn", link=TRADEINN.format(si=20618, li=1874240), langs=["en"], strip="https://www.tradeinn.com/"),
    "techinn": dict(name="Techinn", link=TRADEINN.format(si=20616, li=1874238), langs=["en"], strip="https://www.tradeinn.com/"),
}

T = "https://www.tradeinn.com/trekkinn/en/"
E = "https://www.tradeinn.com/techinn/en/"
OGL = "https://www.outdoorgearlab.com/reviews/"

def P(shop, path, name, desc, say=None, src=None):
    """say: ("review", text) for what an independent reviewer found, ("note", text) for a fact worth knowing.
    src: (site name, url) for a review. Text is our own summary, never a quote."""
    return dict(shop=shop, url=(T if shop == "trekkinn" else E) + path + "/p", name=name, desc=desc, say=say, src=src)

PRODUCTS = {
    "powerbank-kulde": [
        P("techinn", "anker-a1388g11-power-bank-10000mah/141770458", "Anker Power Bank 10,000 mAh (22.5 W)",
          "USB-C and USB-A ports, 22.5 W output and about 250 g. Enough for roughly two phone charges.",
          ("note", "Like every lithium battery it loses capacity in the cold, so carry it inside your jacket on winter trips.")),
        P("techinn", "samsung-eb-p3401xue-10000mah-25w-power-bank/143661434", "Samsung 10,000 mAh 25 W",
          "Two USB-C ports with 25 W fast charging when one device is connected. A good match for phones that support Samsung Super Fast Charging.",
          ("note", "Fast charging only applies with a single device; charging two at once is slower.")),
    ],
    "skalljakke-eller-regnjakke": [
        P("trekkinn", "columbia-pouring-adventure--iii-jacket/140985428", "Columbia Pouring Adventure III",
          "Light, packable rain jacket with Columbia's Omni-Tech waterproof and breathable membrane.",
          ("note", "A rain jacket for summer hikes and everyday use rather than a full mountain shell.")),
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
          "The matching 260 bottom layer for winter trips and cold nights in the tent."),
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
          ("note", "Salewa says the Litetrek tents are wind-tunnel tested to 90 km/h. With only one door it can feel warm on summer nights.")),
        P("trekkinn", "salewa-denali-ii-tent/136362637", "Salewa Denali II",
          "Two-person, three-season dome with two entrances and two vestibules. About 2.4 kg.",
          ("review", "We Are Explorers found it robust and roomy, but at the heavier end for a two-person tent."),
          ("We Are Explorers", "https://weareexplorers.co/salewa-denali-ii-tent/")),
        P("trekkinn", "salewa-latitude-ii-tent/136473591", "Salewa Latitude II",
          "Light two-person dome that packs small, made for alpine trekking. Two entrances, about 2.7 kg, fly 3,000 mm."),
    ],
    "sovepose-temperatur": [
        P("trekkinn", "marmot-helium-m14404-sleeping-bag/139716678", "Marmot Helium",
          "Down bag with 800-fill goose down, a water-resistant shell and a lower limit around -9 °C.",
          ("review", "OutdoorGearLab praised the warmth and build quality but marked it down for an awkwardly placed second zip and a high price."),
          ("OutdoorGearLab", OGL + "camping-and-hiking/backpacking-sleeping-bag/marmot-helium-15")),
        P("trekkinn", "haglofs-tarius--18-c-sleeping-bag/137633887", "Haglöfs Tarius -18 °C",
          "Synthetic winter bag: comfort -11 °C, limit -18 °C. Weighs close to 3 kg.",
          ("note", "Synthetic fill keeps insulating when it gets damp, but the bag is heavy and bulky. Best when you pull a sled.")),
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
    ],
}


def img(url):
    """Tradeinn product image (same as in the product feed): /f/<first 5 digits of id>/<id>/<slug>.webp"""
    parts = url.rstrip("/").split("/")
    slug, pid = parts[-3], parts[-2]
    return f"https://www.tradeinn.com/f/{pid[:5]}/{pid}/{slug}.webp"


L = {
    "en": dict(h="Where to buy", btn="See price at {shop}", ad="Affiliate link", review="What reviewers say", notel="Good to know",
               note="We may earn a commission if you buy through these links. Prices include VAT for buyers in the EU. Buyers outside the EU, including Norway, may pay VAT, duty and fees on delivery."),
    "no": dict(h="Hvor kan du kjøpe", btn="Se pris hos {shop}", ad="Annonselenke", review="Dette sier testene", notel="Verdt å vite",
               note="Vi kan få provisjon hvis du kjøper via disse lenkene."),
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
        say = ""
        if p["say"]:
            kind, text = p["say"]
            srcl = f' <a href="{escape(p["src"][1])}" target="_blank" rel="noopener">{escape(p["src"][0])}</a>' if p["src"] else ""
            say = f'<p class="psay"><strong>{t["review"] if kind == "review" else t["notel"]}:</strong> {escape(text)}{srcl}</p>'
        out.append(f'<div class="pcard"><img class="pimg" src="{img(url)}" alt="{escape(p["name"])}" loading="lazy" width="400" height="400">'
                   f'<h3>{escape(p["name"])}</h3><p class="pdesc">{escape(p["desc"])}</p>{say}'
                   f'<a class="pbtn" href="{escape(href)}" rel="sponsored nofollow noopener" target="_blank">{t["btn"].format(shop=s["name"])}</a>'
                   f'<span class="adlabel">{t["ad"]}</span></div>')
    return f'<section class="products"><h2>{t["h"]}</h2><div class="pgrid">{"".join(out)}</div><p class="pnote">{t["note"]}</p></section>'
