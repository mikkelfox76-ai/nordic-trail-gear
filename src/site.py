"""Builds the whole site into the repo root. Run: python3 src/site.py https://mikkelfox76-ai.github.io /nordic-trail-gear
Add a guide by appending to ARTS in src/articles.py, then run this and push."""
import os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as b
import articles as A

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else ""
PREFIX = sys.argv[2].rstrip("/") if len(sys.argv) > 2 else ""
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("no", "en"): shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
ACC = "#1F5C4A"
b.ph = lambda t, h: ""

X = {
 "no": dict(root=PREFIX + "/no/", cats=["tur-og-camping", "klaer-og-sko", "elektronikk", "jakt-og-fiske"], guides="guider", about="om",
  art="hodelykt-vinter", soon="Kommer snart", none="Guider i denne kategorien kommer snart.", date="Oppdatert 18. november 2026",
  all_h="Alle guider", desc="Guider til turutstyr, klær og elektronikk for nordisk friluftsliv.",
  subs=["Telt, soveposer og kokeutstyr for alt fra helgetur til langtur.",
        "Lag på lag som holder deg tørr og varm, fra ull innerst til skall ytterst.", None,
        "Kikkerter, kniver og fiskeutstyr til sesongen som kommer."],
  foot=["Om oss", "Annonsemerking", "Personvern"], anchors=["", "#annonsemerking", "#personvern"],
  abt=[("Om Nordic Trail Gear", "Nordic Trail Gear lager guider til utstyr for friluftsliv i nordisk klima: turutstyr, klær og elektronikk. Vi sammenligner spesifikasjoner, priser og omtaler, og forklarer hva som betyr noe når du skal velge. Vi sier fra når vi ikke har prøvd et produkt selv."),
         ("Annonsemerking", "Nettstedet finansieres med annonselenker. Når du klikker på en slik lenke og handler i nettbutikken, kan vi få provisjon. Prisen du betaler er den samme. Annonselenker er merket ved hver knapp, og rekkefølgen i guidene bestemmes av vurderingen vår, ikke av provisjonen."),
         ("Personvern", "Vi samler ikke inn personopplysninger på dette nettstedet og bruker ikke egne sporingsverktøy. Når du klikker på en annonselenke, kan nettbutikken og annonsenettverket sette informasjonskapsler for å registrere at kjøpet kom herfra. Det reguleres av deres egne personvernerklæringer.")]),
 "en": dict(root=PREFIX + "/en/", cats=["hiking-camping", "clothing-footwear", "electronics", "hunting-fishing"], guides="guides", about="about",
  art="winter-headlamp", soon="Coming soon", none="Guides in this category are coming soon.", date="Updated 18 November 2026",
  all_h="All guides", desc="Guides to hiking gear, clothing and electronics for Nordic outdoor life.",
  subs=["Tents, sleeping bags and stoves for anything from a weekend out to a long trek.",
        "Layers that keep you dry and warm, from wool next to skin to a shell on top.", None,
        "Binoculars, knives and tackle for the season ahead."],
  foot=["About", "Affiliate disclosure", "Privacy"], anchors=["", "#disclosure", "#privacy"],
  abt=[("About Nordic Trail Gear", "Nordic Trail Gear publishes guides to outdoor gear for Nordic conditions: hiking equipment, clothing and electronics. We compare specs, prices and reviews, and explain what matters when you choose. We say so when we have not handled a product ourselves."),
         ("Affiliate disclosure", "This site is funded by affiliate links. When you click one and buy from the store, we may earn a commission. The price you pay is the same. Affiliate links are labelled next to each button, and the order in our guides follows our assessment, not the commission."),
         ("Privacy", "We do not collect personal data on this site and use no tracking tools of our own. When you click an affiliate link, the store and the affiliate network may set cookies to record that the purchase came from here. That is covered by their own privacy policies.")]),
}


def first(lang):
    t = b.L[lang]
    return dict(title=t["art_h1"], lead=t["lead"], short=t["short"], secs=t["look"])
ARTS = [dict(cat=2, slug=dict(no="hodelykt-vinter", en="winter-headlamp"), no=first("no"), en=first("en"))] + A.ARTS

IMGS = ["headlamp", "powerbank", "gps-watch", "shell-jacket", "layering", "footwear", "tent", "sleeping-bag", "sleeping-pad", "binoculars"]
CATIMG = ["cat-camping", "cat-clothing", "cat-electronics", "cat-fishing"]
def art_img(i): return ARTS[i].get("img") or (IMGS[i] if i < len(IMGS) else None)
def img(name, alt, ratio="16 / 9", lazy=True):
    if not name: return ""
    return f'<img src="{PREFIX}/img/{name}.webp" alt="{alt}" width="1344" height="768"{" loading=\"lazy\"" if lazy else ""} style="width: 100%; height: auto; aspect-ratio: {ratio}; object-fit: cover; border-radius: 6px; display: block">'

def paths(lang):
    x = X[lang]; r = x["root"]
    p = {"home": r, "guides": f'{r}{x["guides"]}/', "about": f'{r}{x["about"]}/'}
    for i, c in enumerate(x["cats"]): p[f"cat{i}"] = f"{r}{c}/"
    for i, a in enumerate(ARTS): p[f"art{i}"] = f'{r}{x["guides"]}/{a["slug"][lang]}/'
    return p

def cards(lang, only=None, limit=None):
    t, p, out, n = b.L[lang], paths(lang), "", 0
    for i in reversed(range(len(ARTS))):
        a = ARTS[i]
        if only is not None and a["cat"] != only: continue
        if limit and n >= limit: break
        n += 1
        out += f"""<article style="background: #FFFFFF; border: 1px solid {b.LINE}; border-radius: 8px; padding: 20px; display: flex; flex-direction: column; gap: 12px">
{img(art_img(i), "")}
<div style="font-size: 13px; font-weight: 600; color: {ACC}; text-transform: uppercase; letter-spacing: 0.06em">{t["cats"][a["cat"]][0]}</div>
<h3 style="{b.HEAD}; font-size: 20px; line-height: 1.25">{a[lang]["title"]}</h3>
<a href="{p[f"art{i}"]}" style="font-weight: 600; padding: 10px 0">{t["read"]} →</a></article>"""
    return out

def page(lang, key, title, desc, body):
    t, x, p, o = b.L[lang], X[lang], paths(lang), paths("en" if lang == "no" else "no")
    t = dict(t, foot=x["foot"])
    html = b.header(t, "", lang) + body + b.footer(t)
    m = {"Nordic Trail Gear": p["home"], t["home"]: p["home"], t["cta"]: p["guides"], t["cta2"]: p["about"], t["nav"][4]: p["guides"],
         "Norsk": (p if lang == "no" else o)[key], "English": (p if lang == "en" else o)[key]}
    for i in range(4): m[t["nav"][i]] = p[f"cat{i}"]; m[t["cats"][i][0]] = p[f"cat{i}"]
    for name, a in zip(x["foot"], x["anchors"]): m[name] = p["about"] + a
    def fix(mo):
        inner = re.sub(r"<[^>]+>", "", mo.group(2)).strip()
        for k in sorted(m, key=len, reverse=True):
            if inner == k or inner.startswith(k): return f'<a href="{m[k]}"{mo.group(1)}>{mo.group(2)}</a>'
        raise SystemExit(f"unmapped link: {inner!r} on {lang}/{key}")
    html = re.sub(r'<a href="#"([^>]*)>(.*?)</a>', fix, html, flags=re.S).replace("{{accent}}", ACC)
    alt = "".join(f'<link rel="alternate" hreflang="{hl}" href="{BASE}{pp[key]}">' for hl, pp in (("nb", p if lang == "no" else o), ("en", p if lang == "en" else o)))
    doc = f"""<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{p[key]}">{alt}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap">
<style>body{{margin:0}}a{{color:#12211C}}a:hover{{color:#1F5C4A}}</style>
</head>
<body>
<div style="background: #F4F6F5; color: #12211C; font-family: Inter, system-ui, sans-serif; font-size: 16px; line-height: 1.55; min-height: 100vh">
{html}
</div>
</body>
</html>"""
    d = OUT + p[key][len(PREFIX):]; os.makedirs(d, exist_ok=True)
    open(d + "index.html", "w", encoding="utf-8").write(doc)
    return p[key]

urls = []
H2 = f"{b.HEAD}; font-size: 28px; margin-top: 16px"
H1 = f"{b.HEAD}; font-size: clamp(30px, 5vw, 44px); line-height: 1.12"
NARROW = "max-width: 760px; margin: 0 auto; padding: 24px 24px 0; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px"
for lang in ("no", "en"):
    t, x = b.L[lang], X[lang]
    b.guide_cards = lambda tt, _l=lang: cards(_l, limit=6)
    hb = b.home(t).replace("</div>\n</div>\n</section>", "</div>\n" + img("hero", x["desc"], "21 / 9", lazy=False) + "\n</div>\n</section>", 1)
    for i in range(4):
        sp = f'<span style="{b.HEAD}; font-size: 20px">{t["cats"][i][0]}</span>'
        assert sp in hb
        hb = hb.replace(sp, img(CATIMG[i], "") + sp, 1)
    urls.append(page(lang, "home", f'Nordic Trail Gear – {t["tag"]}', x["desc"], hb))
    disc = f'<p style="margin: 0; padding: 12px 16px; background: #E6EEEA; border-radius: 6px; font-size: 14px">{t["disc"]}</p>'
    for i in range(4):
        name = t["cats"][i][0]
        h1 = t["cat_h1"] if i == 2 else name
        sub = t["cat_sub"] if i == 2 else x["subs"][i]
        cs = cards(lang, only=i)
        inner = f'<div style="{b.GRID3}">{cs}</div>' if cs else f'<p style="margin: 0; color: {b.MUTED}">{x["none"]}</p>'
        body = f"""<main style="{b.WRAP}; padding-top: 24px; display: flex; flex-direction: column; gap: 24px">
{b.crumbs(t, [name])}
<h1 style="{b.HEAD}; font-size: clamp(32px, 5vw, 48px); line-height: 1.1">{h1}</h1>
<p style="margin: 0; font-size: 18px; color: {b.MUTED}; max-width: 640px">{sub}</p>
{img(CATIMG[i], h1, "21 / 9", lazy=False)}
{disc}
<h2 style="{H2}">{t["more_h"]}</h2>{inner}
</main>"""
        urls.append(page(lang, f"cat{i}", f"{h1} – Nordic Trail Gear", sub, body))
    body = f"""<main style="{b.WRAP}; padding-top: 24px; display: flex; flex-direction: column; gap: 24px">
{b.crumbs(t, [t["nav"][4]])}
<h1 style="{b.HEAD}; font-size: clamp(32px, 5vw, 48px); line-height: 1.1">{x["all_h"]}</h1>
<div style="{b.GRID3}">{cards(lang)}</div>
</main>"""
    urls.append(page(lang, "guides", f'{x["all_h"]} – Nordic Trail Gear', x["desc"], body))
    for i, a in enumerate(ARTS):
        d = a[lang]
        short = "".join(f"<li>{s}</li>" for s in d["short"])
        secs = "".join(f'<h2 style="{b.HEAD}; font-size: 24px; margin-top: 12px">{h}</h2><p style="margin: 0">{c}</p>' for h, c in d["secs"])
        body = f"""<main style="{NARROW}">
{b.crumbs(t, [t["nav"][a["cat"]], t["nav"][4]])}
<h1 style="{H1}">{d["title"]}</h1>
<div style="font-size: 14px; color: {b.MUTED}">{x["date"]}</div>
<p style="margin: 0; font-size: 20px">{d["lead"]}</p>
{img(art_img(i), d["title"], lazy=False)}
<section style="border-top: 2px solid {b.INK}; padding-top: 16px">
<h2 style="{b.HEAD}; font-size: 22px">{t["short_h"]}</h2>
<ul style="margin: 12px 0 0; padding-left: 20px; display: flex; flex-direction: column; gap: 6px">{short}</ul>
</section>
{secs}
</main>"""
        urls.append(page(lang, f"art{i}", f'{d["title"]} – Nordic Trail Gear', d["lead"], body))
    ids = ["", x["anchors"][1][1:], x["anchors"][2][1:]]
    secs = "".join((f'<h1 style="{H1}">{h}</h1>' if i == 0 else f'<h2 id="{ids[i]}" style="{H2}">{h}</h2>') + f'<p style="margin: 0">{txt}</p>' for i, (h, txt) in enumerate(x["abt"]))
    urls.append(page(lang, "about", x["abt"][0][0], x["abt"][0][1][:150], f'<main style="{NARROW}">{b.crumbs(t, [x["foot"][0]])}{secs}</main>'))

open(OUT + "/.nojekyll", "w").write("")
open(OUT + "/index.html", "w").write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Nordic Trail Gear</title><meta name="viewport" content="width=device-width, initial-scale=1"><script>location.replace(/^(nb|no|nn)/i.test(navigator.language||"")?"no/":"en/")</script><noscript><meta http-equiv="refresh" content="0; url=en/"></noscript></head><body><a href="en/">English</a> · <a href="no/">Norsk</a></body></html>')
open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE}{u}</loc></url>" for u in urls) + "</urlset>")
open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}{PREFIX}/sitemap.xml\n")
print(len(urls), "pages")
