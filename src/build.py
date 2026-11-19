import json, os, datetime
from string import Template

OUT = "/tmp/ntg-design"
os.makedirs(OUT, exist_ok=True)

INK, MUTED, GROUND, LINE = "#12211C", "#4A5A54", "#F4F6F5", "#D5DDD9"

L = {
 "no": dict(lang="nb", nav=["Tur og camping", "Klær og sko", "Elektronikk", "Jakt og fiske", "Guider"],
  tag="Guider til nordisk friluftsliv",
  h1="Utstyr som tåler nordisk vær",
  sub="Guider til turutstyr, klær og elektronikk for friluftsliv. Vi sammenligner spesifikasjoner, priser og omtaler, så velger du.",
  cta="Se guidene", cta2="Slik jobber vi", cats_h="Kategorier", guides_h="Nyeste guider", read="Les guiden",
  cats=[("Tur og camping", "Telt, soveposer og kokeutstyr"), ("Klær og sko", "Skallbekledning, ull og tursko"),
        ("Elektronikk", "Hodelykter, GPS-klokker og powerbanker"), ("Jakt og fiske", "Kikkerter, kniver og fiskeutstyr")],
  guides=[("Elektronikk", "Hodelykt til vinterturen: dette bør du se etter"),
          ("Elektronikk", "Powerbank i kulda: slik velger du riktig"),
          ("Klær og sko", "Skalljakke eller regnjakke? Forskjellen forklart")],
  how_h="Slik jobber vi",
  how=[("Vi samler det viktigste", "Spesifikasjoner, priser og hva utstyret er laget for, forklart på vanlig norsk."),
       ("Vi leser anmeldelsene", "Vi går gjennom tester og omtaler fra dem som har brukt utstyret, og oppsummerer hva de sier."),
       ("Tydelig merket", "Alle annonselenker er merket, i teksten og ved hver knapp.")],
  disc="Annonselenker: Vi kan få provisjon når du kjøper via lenker hos oss. Det koster deg ikke noe ekstra.",
  foot=["Om oss", "Annonsemerking", "Personvern", "Kontakt"], img="Bilde", ad="Annonselenke",
  home="Forside", cat_h1="Elektronikk for friluftsliv",
  cat_sub="Lys, strøm og navigasjon som fungerer når det er kaldt, vått og langt til nærmeste stikkontakt.",
  chips=["Hodelykter", "GPS og klokker", "Powerbanker", "Solcellepanel", "Satellittkommunikasjon"],
  picks_h="Utvalgte produkter", pname="[PRODUKTNAVN]", pnote="[KORT VURDERING I ÉN SETNING]", price="[PRIS]",
  buy="Se pris hos [BUTIKK]", more_h="Guider i denne kategorien",
  art_h1="Hodelykt til vinterturen: dette bør du se etter", updated="Oppdatert [DATO]",
  lead="Mørketid og kulde stiller andre krav til en hodelykt enn en sommerkveld. Her er det som faktisk betyr noe når du skal velge.",
  short_h="Kort fortalt",
  short=["Batteriet er viktigere enn maks lysstyrke når det er kaldt.", "Velg en lykt du kan betjene med votter.", "Sjekk vanntetthet (IP-klasse) før du ser på pris."],
  our_h="Våre valg", ranks=["Best totalt", "Best på budsjett", "Best til lange turer"],
  look_h="Dette bør du se etter",
  look=[("Batteri i kulde", "Batterier leverer mindre strøm når det er kaldt. En lykt med batteripakke du kan ha innenfor jakka, holder lenger på vinterturer."),
        ("Lysstyrke og lyskjegle", "Lumen forteller hvor mye lys lykta gir totalt. Til skigåing og orientering trenger du lang rekkevidde, i leir er bredt og jevnt lys viktigere."),
        ("Betjening", "Store knapper eller ratt lar seg bruke med votter. Låsefunksjon hindrer at lykta slår seg på i sekken."),
        ("Vekt og passform", "En tung lykt bør ha rem over hodet. Prøv om den sitter stødig utenpå lue eller hjelm.")]),
 "en": dict(lang="en", nav=["Hiking & camping", "Clothing & footwear", "Electronics", "Hunting & fishing", "Guides"],
  tag="Guides to Nordic outdoor life",
  h1="Gear built for Nordic weather",
  sub="Guides to hiking gear, clothing and outdoor electronics. We compare specs, prices and reviews, then you choose.",
  cta="See the guides", cta2="How we work", cats_h="Categories", guides_h="Latest guides", read="Read the guide",
  cats=[("Hiking & camping", "Tents, sleeping bags and stoves"), ("Clothing & footwear", "Shells, wool and hiking boots"),
        ("Electronics", "Headlamps, GPS watches and power banks"), ("Hunting & fishing", "Binoculars, knives and tackle")],
  guides=[("Electronics", "Headlamps for winter trips: what to look for"),
          ("Electronics", "Power banks in the cold: how to choose"),
          ("Clothing & footwear", "Shell jacket or rain jacket? The difference explained")],
  how_h="How we work",
  how=[("We gather what matters", "Specs, prices and what the gear is made for, explained in plain language."),
       ("We read the reviews", "We go through tests and reviews from people who have used the gear, and sum up what they say."),
       ("Clearly labelled", "Every affiliate link is labelled, in the text and next to each button.")],
  disc="Affiliate links: We may earn a commission when you buy through links on this site, at no extra cost to you.",
  foot=["About", "Affiliate disclosure", "Privacy", "Contact"], img="Image", ad="Affiliate link",
  home="Home", cat_h1="Electronics for the outdoors",
  cat_sub="Light, power and navigation that keep working when it is cold, wet and far from the nearest socket.",
  chips=["Headlamps", "GPS & watches", "Power banks", "Solar panels", "Satellite messengers"],
  picks_h="Selected products", pname="[PRODUCT NAME]", pnote="[ONE-SENTENCE VERDICT]", price="[PRICE]",
  buy="See price at [STORE]", more_h="Guides in this category",
  art_h1="Headlamps for winter trips: what to look for", updated="Updated [DATE]",
  lead="Dark months and cold put different demands on a headlamp than a summer evening. Here is what actually matters when you choose.",
  short_h="In short",
  short=["Battery matters more than peak brightness in the cold.", "Pick a lamp you can operate with mittens on.", "Check water resistance (IP rating) before you look at price."],
  our_h="Our picks", ranks=["Best overall", "Best on a budget", "Best for long trips"],
  look_h="What to look for",
  look=[("Battery in the cold", "Batteries deliver less power when it is cold. A lamp with a battery pack you can keep inside your jacket lasts longer on winter trips."),
        ("Brightness and beam", "Lumens tell you how much light the lamp gives in total. Skiing and navigation need long reach, while camp chores need a wide, even beam."),
        ("Controls", "Large buttons or dials work with mittens. A lock stops the lamp switching on inside your pack."),
        ("Weight and fit", "A heavy lamp should have a top strap. Check that it sits firmly over a hat or helmet.")]),
}

PAGE = Template('''<!doctype html>
<html lang="$lang">
<head>
<meta charset="utf-8">
<title>$title</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap">
<style>
body{margin:0}
a{color:#12211C}a:hover{color:#1F5C4A}
</style>
</helmet>
<div style="background: #F4F6F5; color: #12211C; font-family: Inter, system-ui, sans-serif; font-size: 16px; line-height: 1.55">
$header
$body
$footer
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"accent":{"editor":"color","default":"#1F5C4A"},"$$preview":{"width":1280,"height":$h}}'>
class Component extends DCLogic {
renderVals() {
return { accent: this.props.accent ?? '#1F5C4A' };
}
}
</script>
</body>
</html>
''')

WRAP = "max-width: 1120px; margin: 0 auto; padding: 0 24px; box-sizing: border-box"
HEAD = "font-family: 'Space Grotesk', Inter, sans-serif; font-weight: 700; margin: 0"
BTN = "display: inline-flex; align-items: center; min-height: 48px; padding: 0 22px; border-radius: 6px; font-weight: 600; text-decoration: none; box-sizing: border-box"

def header(t, other_label, cur):
    nav = "".join(f'<a href="#" style="text-decoration: none; font-weight: 500; padding: 12px 0">{n}</a>' for n in t["nav"])
    no_s = "font-weight: 600; text-decoration: underline" if cur == "no" else "text-decoration: none"
    en_s = "font-weight: 600; text-decoration: underline" if cur == "en" else "text-decoration: none"
    return f'''<header style="background: #FFFFFF; border-bottom: 1px solid {LINE}">
<div style="{WRAP}; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px 32px; padding-top: 12px; padding-bottom: 12px">
<a href="#" style="display: flex; align-items: center; gap: 10px; text-decoration: none; {HEAD}; font-size: 20px">
<svg aria-hidden="true" width="32" height="32" viewBox="0 0 32 32" fill="none" stroke="{{{{accent}}}}" stroke-width="2.5" stroke-linejoin="round"><path d="M3 26 L12 9 L17 18 L21 12 L29 26 Z"/></svg>
Nordic Trail Gear</a>
<nav aria-label="Main" style="display: flex; flex-wrap: wrap; gap: 0 24px">{nav}</nav>
<div style="display: flex; gap: 12px; font-size: 14px"><a href="#" lang="nb" style="padding: 12px 4px; {no_s}">Norsk</a><a href="#" lang="en" style="padding: 12px 4px; {en_s}">English</a></div>
</div>
</header>'''

def footer(t):
    links = "".join(f'<a href="#" style="color: #FFFFFF; padding: 12px 0">{x}</a>' for x in t["foot"])
    return f'''<footer style="background: {INK}; color: #FFFFFF; margin-top: 72px">
<div style="{WRAP}; padding-top: 40px; padding-bottom: 40px; display: flex; flex-direction: column; gap: 16px">
<div style="{HEAD}; font-size: 18px">Nordic Trail Gear</div>
<p style="margin: 0; max-width: 640px; color: #D5DDD9">{t["disc"]}</p>
<nav aria-label="Footer" style="display: flex; flex-wrap: wrap; gap: 0 24px; font-size: 14px">{links}</nav>
</div>
</footer>'''

def ph(t, h):
    return f'<div role="img" aria-label="{t["img"]}" style="height: {h}px; background: #DDE5E1; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: {MUTED}; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase">[{t["img"]}]</div>'

def guide_cards(t):
    return "".join(f'''<article style="background: #FFFFFF; border: 1px solid {LINE}; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; gap: 12px">
{ph(t, 160)}
<div style="font-size: 13px; font-weight: 600; color: {{{{accent}}}}; text-transform: uppercase; letter-spacing: 0.06em">{c}</div>
<h3 style="{HEAD}; font-size: 20px; line-height: 1.25">{h}</h3>
<a href="#" style="font-weight: 600; padding: 10px 0">{t["read"]} →</a>
</article>''' for c, h in t["guides"])

GRID3 = "display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px"

def home(t):
    cats = "".join(f'''<a href="#" style="background: #FFFFFF; border: 1px solid {LINE}; border-radius: 8px; padding: 24px; text-decoration: none; display: flex; flex-direction: column; gap: 6px; min-height: 96px">
<span style="{HEAD}; font-size: 20px">{a}</span><span style="color: {MUTED}">{b}</span></a>''' for a, b in t["cats"])
    how = "".join(f'<div style="display: flex; flex-direction: column; gap: 6px"><h3 style="{HEAD}; font-size: 18px">{a}</h3><p style="margin: 0; color: {MUTED}">{b}</p></div>' for a, b in t["how"])
    return f'''<main>
<section style="background: #FFFFFF; border-bottom: 1px solid {LINE}">
<div style="{WRAP}; padding-top: 72px; padding-bottom: 72px; display: flex; flex-direction: column; gap: 20px">
<div style="font-size: 14px; font-weight: 600; color: {{{{accent}}}}; text-transform: uppercase; letter-spacing: 0.08em">{t["tag"]}</div>
<h1 style="{HEAD}; font-size: clamp(36px, 6vw, 64px); line-height: 1.05; max-width: 780px">{t["h1"]}</h1>
<p style="margin: 0; font-size: 20px; color: {MUTED}; max-width: 620px">{t["sub"]}</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 8px">
<a href="#" style="{BTN}; background: {{{{accent}}}}; color: #FFFFFF">{t["cta"]}</a>
<a href="#" style="{BTN}; border: 1px solid {INK}">{t["cta2"]}</a>
</div>
</div>
</section>
<section style="{WRAP}; padding-top: 56px; display: flex; flex-direction: column; gap: 24px">
<h2 style="{HEAD}; font-size: 28px">{t["cats_h"]}</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px">{cats}</div>
</section>
<section style="{WRAP}; padding-top: 56px; display: flex; flex-direction: column; gap: 24px">
<h2 style="{HEAD}; font-size: 28px">{t["guides_h"]}</h2>
<div style="{GRID3}">{guide_cards(t)}</div>
</section>
<section style="{WRAP}; padding-top: 56px; display: flex; flex-direction: column; gap: 24px">
<h2 style="{HEAD}; font-size: 28px">{t["how_h"]}</h2>
<div style="{GRID3}; border-top: 2px solid {INK}; padding-top: 24px">{how}</div>
</section>
</main>'''

def crumbs(t, trail):
    parts = [f'<a href="#" style="padding: 10px 0">{t["home"]}</a>'] + [f'<span aria-hidden="true">/</span><a href="#" style="padding: 10px 0">{x}</a>' for x in trail]
    return f'<nav aria-label="Breadcrumb" style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px; font-size: 14px">{"".join(parts)}</nav>'

def buy(t):
    return f'''<div style="display: flex; flex-direction: column; gap: 4px; align-items: flex-start">
<a href="#" rel="sponsored nofollow" style="{BTN}; background: {{{{accent}}}}; color: #FFFFFF">{t["buy"]}</a>
<span style="font-size: 12px; color: {MUTED}">{t["ad"]}</span></div>'''

def category(t):
    chips = "".join(f'<a href="#" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 16px; border: 1px solid {INK}; border-radius: 999px; text-decoration: none; font-weight: 500; background: #FFFFFF">{c}</a>' for c in t["chips"])
    cards = "".join(f'''<article style="background: #FFFFFF; border: 1px solid {LINE}; border-radius: 8px; padding: 16px; display: flex; flex-direction: column; gap: 12px">
{ph(t, 180)}
<h3 style="{HEAD}; font-size: 18px">{t["pname"]}</h3>
<p style="margin: 0; color: {MUTED}">{t["pnote"]}</p>
<div style="font-weight: 600; font-size: 18px">{t["price"]}</div>
{buy(t)}
</article>''' for _ in range(6))
    return f'''<main style="{WRAP}; padding-top: 24px; display: flex; flex-direction: column; gap: 24px">
{crumbs(t, [t["nav"][2]])}
<h1 style="{HEAD}; font-size: clamp(32px, 5vw, 48px); line-height: 1.1">{t["cat_h1"]}</h1>
<p style="margin: 0; font-size: 18px; color: {MUTED}; max-width: 640px">{t["cat_sub"]}</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px">{chips}</div>
<p style="margin: 0; padding: 12px 16px; background: #E6EEEA; border-radius: 6px; font-size: 14px">{t["disc"]}</p>
<h2 style="{HEAD}; font-size: 28px; margin-top: 16px">{t["picks_h"]}</h2>
<div style="{GRID3}">{cards}</div>
<h2 style="{HEAD}; font-size: 28px; margin-top: 32px">{t["more_h"]}</h2>
<div style="{GRID3}">{guide_cards(t)}</div>
</main>'''

def article(t):
    short = "".join(f"<li>{s}</li>" for s in t["short"])
    picks = "".join(f'''<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 16px; padding: 16px; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 8px">
<div style="flex: 0 0 120px">{ph(t, 96)}</div>
<div style="flex: 1 1 240px; display: flex; flex-direction: column; gap: 4px">
<span style="font-size: 13px; font-weight: 600; color: {{{{accent}}}}; text-transform: uppercase; letter-spacing: 0.06em">{r}</span>
<span style="{HEAD}; font-size: 18px">{t["pname"]}</span>
<span style="color: {MUTED}">{t["pnote"]} · {t["price"]}</span></div>
{buy(t)}
</div>''' for r in t["ranks"])
    look = "".join(f'<h3 style="{HEAD}; font-size: 20px; margin-top: 8px">{a}</h3><p style="margin: 0">{b}</p>' for a, b in t["look"])
    return f'''<main style="max-width: 760px; margin: 0 auto; padding: 24px 24px 0; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px">
{crumbs(t, [t["nav"][2], t["nav"][4]])}
<h1 style="{HEAD}; font-size: clamp(30px, 5vw, 44px); line-height: 1.12">{t["art_h1"]}</h1>
<div style="font-size: 14px; color: {MUTED}">{t["updated"]}</div>
<p style="margin: 0; font-size: 20px">{t["lead"]}</p>
<p style="margin: 0; padding: 12px 16px; background: #E6EEEA; border-radius: 6px; font-size: 14px">{t["disc"]}</p>
{ph(t, 340)}
<section style="border-top: 2px solid {INK}; padding-top: 16px">
<h2 style="{HEAD}; font-size: 22px">{t["short_h"]}</h2>
<ul style="margin: 12px 0 0; padding-left: 20px; display: flex; flex-direction: column; gap: 6px">{short}</ul>
</section>
<h2 style="{HEAD}; font-size: 28px; margin-top: 16px">{t["our_h"]}</h2>
<div style="display: flex; flex-direction: column; gap: 12px">{picks}</div>
<h2 style="{HEAD}; font-size: 28px; margin-top: 16px">{t["look_h"]}</h2>
{look}
</main>'''

boards, order = {}, []
specs = [("home", home, 1700, lambda t: "Nordic Trail Gear"),
         ("category", category, 1900, lambda t: t["cat_h1"]),
         ("article", article, 2100, lambda t: t["art_h1"])]
names = {("home", "no"): "Main", ("home", "en"): "Home-EN", ("category", "no"): "Kategori-NO", ("category", "en"): "Category-EN",
         ("article", "no"): "Artikkel-NO", ("article", "en"): "Article-EN"}
titles = {"Main": "Forside (norsk)", "Home-EN": "Home (English)", "Kategori-NO": "Kategoriside (norsk)", "Category-EN": "Category (English)",
          "Artikkel-NO": "Artikkelmal (norsk)", "Article-EN": "Article template (English)"}
for row, lang in enumerate(["no", "en"]):
    t = L[lang]
    for col, (kind, fn, h, title) in enumerate(specs):
        name = names[(kind, lang)] + ".dc.html"
        html = PAGE.substitute(lang=t["lang"], title=title(t), header=header(t, "", lang), body=fn(t), footer=footer(t), h=h)
        open(f"{OUT}/{name}", "w", encoding="utf-8").write(html)
        boards[name] = {"x": col * 1360, "y": row * 2520, "w": 1280, "h": h, "expand": "fill", "title": titles[name[:-8]]}
        order.append(name)

canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")},
          "title": "Nordic Trail Gear – nettsted", "launch": {"view": "canvas"}, "pages": [], "boards": boards, "order": order,
          "notes": {"no": {"x": 0, "y": -300, "text": "Norsk", "kind": "title1", "maxW": 4000},
                    "en": {"x": 0, "y": 2220, "text": "English", "kind": "title1", "maxW": 4000}},
          "designSystems": []}
json.dump(canvas, open(f"{OUT}/canvas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(order)
