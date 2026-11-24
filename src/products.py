"""Product cards with affiliate links, shown under a guide.
SHOPS: one entry per shop. "link" is the network's deeplink template with {url} (URL-encoded product address)
and {sub} (guide slug + language, so sales can be traced per guide). A shop with an empty "link" is skipped.
"langs" lists the site languages the shop may be shown on. Tradeinn is not VOEC-registered, so Norwegian
buyers pay VAT, possible duty and a clearance fee on arrival: Tradeinn shops are shown on /en/ only.
PRODUCTS: Norwegian guide slug -> list of (shop, product URL, name, one-line reason in English)."""
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
PRODUCTS = {
    "powerbank-kulde": [
        ("techinn", E + "anker-a1388g11-power-bank-10000mah/141770458/p", "Anker 10,000 mAh power bank", "Small and light: about two phone charges for a weekend."),
        ("techinn", E + "samsung-eb-p3401xue-10000mah-25w-power-bank/143661434/p", "Samsung 10,000 mAh 25 W power bank", "USB-C fast charging for phones that support it."),
        ("techinn", E + "ugreen-lipo-20000mah-power-bank/141721671/p", "Ugreen 20,000 mAh power bank", "Double the capacity for longer trips off the grid."),
    ],
    "skalljakke-eller-regnjakke": [
        ("trekkinn", T + "columbia-pouring-adventure--iii-jacket/140985428/p", "Columbia Pouring Adventure III", "Lightweight rain jacket for wet summer hikes."),
        ("trekkinn", T + "columbia-watertight--ii-jacket/140983790/p", "Columbia Watertight II", "Simple, packable rain shell at a low price."),
    ],
    "lag-pa-lag": [
        ("trekkinn", T + "icebreaker-260-tech-merino-long-sleeve-base-layer/136879912/p", "Icebreaker 260 Tech merino top", "Warm merino base layer for winter."),
        ("trekkinn", T + "icebreaker-200-oasis-merino-long-sleeve-base-layer/136879888/p", "Icebreaker 200 Oasis merino top", "Lighter merino for active days and shoulder seasons."),
        ("trekkinn", T + "icebreaker-260-tech-merino-base-layer-pants/136879924/p", "Icebreaker 260 Tech merino leggings", "The matching bottom layer for cold trips."),
    ],
    "tursko-eller-fjellstovler": [
        ("trekkinn", T + "salomon-quest-5-gore-tex--hiking-boots/142751824/p", "Salomon Quest 5 GTX", "Supportive boot for heavy packs and rough terrain."),
        ("trekkinn", T + "salomon-x-ultra-360-mid-gore-tex--hiking-boots/140536746/p", "Salomon X Ultra 360 Mid GTX", "Lighter mid boot for fast day hikes."),
        ("trekkinn", T + "merrell-moab-3-mid-gore-tex--hiking-boots/139599810/p", "Merrell Moab 3 Mid GTX", "Comfortable classic that needs little breaking in."),
    ],
    "velge-telt": [
        ("trekkinn", T + "salewa-litetrek-iii-tent/136362634/p", "Salewa Litetrek III", "Light three-person tent for summer trips."),
        ("trekkinn", T + "salewa-denali-ii-tent/136362637/p", "Salewa Denali II", "Sturdy two-person dome for windy campsites."),
        ("trekkinn", T + "salewa-latitude-ii-tent/136473591/p", "Salewa Latitude II", "Tunnel tent with room for gear in the vestibule."),
    ],
    "sovepose-temperatur": [
        ("trekkinn", T + "marmot-helium-m14404-sleeping-bag/139716678/p", "Marmot Helium", "Down bag for cold three-season nights."),
        ("trekkinn", T + "haglofs-tarius--18-c-sleeping-bag/137633887/p", "Haglöfs Tarius -18 °C", "Rated for winter camping in Nordic conditions."),
        ("trekkinn", T + "sea-to-summit-breeze-sleeping-bag/140608877/p", "Sea to Summit Breeze", "Light down bag for summer."),
    ],
    "liggeunderlag-r-verdi": [
        ("trekkinn", T + "sea-to-summit-ether-light-xt-inflatable-mat/137081634/p", "Sea to Summit Ether Light XT", "Thick, comfortable mat for three seasons."),
        ("trekkinn", T + "sea-to-summit-ultralight-inflatable-mat/135906860/p", "Sea to Summit Ultralight", "Packs small for summer trips; add a foam pad in winter."),
    ],
}

L = {
    "en": dict(h="Where to buy", btn="See price at {shop}", ad="Affiliate link",
               note="We may earn a commission if you buy through these links. Prices include VAT for buyers in the EU. Buyers outside the EU, including Norway, may pay VAT, duty and fees on delivery."),
    "no": dict(h="Hvor kan du kjøpe", btn="Se pris hos {shop}", ad="Annonselenke",
               note="Vi kan få provisjon hvis du kjøper via disse lenkene."),
}


def cards(lang, slug_no, prefix=""):
    items = [p for p in PRODUCTS.get(slug_no, []) if SHOPS[p[0]]["link"] and lang in SHOPS[p[0]]["langs"]]
    if not items:
        return ""
    t = L[lang]
    out = []
    for shop, url, name, why in items:
        s = SHOPS[shop]
        target = url[len(s["strip"]):] if s.get("strip") and url.startswith(s["strip"]) else url
        href = s["link"].format(url=quote(target, safe=""), sub=f"{slug_no}-{lang}")
        out.append(f'<div class="pcard"><h3>{escape(name)}</h3><p>{escape(why)}</p>'
                   f'<a class="btn-signal pbtn" href="{escape(href)}" rel="sponsored nofollow noopener" target="_blank">{t["btn"].format(shop=s["name"])}</a>'
                   f'<span class="adlabel">{t["ad"]}</span></div>')
    return f'<section class="products"><h2>{t["h"]}</h2><div class="pgrid">{"".join(out)}</div><p class="pnote">{t["note"]}</p></section>'
