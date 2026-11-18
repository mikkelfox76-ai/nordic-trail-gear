"""Builds the whole site into the repo root.
Run from the repo root: python3 src/site.py https://mikkelfox76-ai.github.io /nordic-trail-gear
Add a guide: append to ARTS in src/articles.py (both languages, optional "img", and "date": "YYYY-MM-DD" for the publish date; "updated" when revised), put the image in img/, run this, commit, push.
Texts: src/build.py (L: menu, front page, first guide), src/texts.py (X: URLs, category intros, footer, about). Design: css/style.css."""
import os, sys, math, shutil, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as b
import articles as A
import feature_snohule as FS
import feature_natt as FN
from texts import X

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else ""
PREFIX = sys.argv[2].rstrip("/") if len(sys.argv) > 2 else ""
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("no", "en"): shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)

EXTRA = {"no": dict(more="Flere guider", site="Nettstedet", pause="Pause video", play="Spill video"),
         "en": dict(more="More guides", site="The site", pause="Pause video", play="Play video")}
IMGS = ["headlamp", "powerbank", "gps-watch", "shell-jacket", "layering", "footwear", "tent", "sleeping-bag", "sleeping-pad", "binoculars"]
CATIMG = ["cat-camping", "cat-clothing", "cat-electronics", "cat-fishing"]
MARK = '<svg aria-hidden="true" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linejoin="round"><path d="M3 26 L12 9 L17 18 L21 12 L29 26 Z"/></svg>'

def first(lang):
    t = b.L[lang]
    return dict(title=t["art_h1"], lead=t["lead"], short=t["short"], secs=t["look"])
ARTS = [dict(cat=2, slug=dict(no="hodelykt-vinter", en="winter-headlamp"), no=first("no"), en=first("en"))] + A.ARTS
import os
for _f in (FS.ART, FN.ART):
    if not _f.get('draft') or os.environ.get('NTG_DRAFT'): ARTS.append(_f)

TODAY = datetime.date.today().isoformat()
LAUNCH = "2026-11-18"
ORG = {"@type": "Organization", "name": "Nordic Trail Gear", "url": BASE + "/", "logo": f"{BASE}{PREFIX}/img/logo.png", "sameAs": ["https://www.facebook.com/profile.php?id=61596897741938"]}
def ld(*objs):
    """JSON-LD script tags (structured data for search engines)."""
    return "".join('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", **o}, ensure_ascii=False).replace("</", "<\\/") + "</script>\n" for o in objs)
def crumb_ld(lang, trail):
    items = [(b.L[lang]["home"], paths(lang)["home"])] + trail
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": n, "item": BASE + h} for k, (n, h) in enumerate(items)]}
def art_img(i): return ARTS[i].get("img") or (IMGS[i] if i < len(IMGS) else "hero")
def src(name): return f"{PREFIX}/img/{name}.webp"
def bgvideo(lang, name):
    """Silent looping background clip with a still poster and a pause button. Falls back to the still image if the clip is missing."""
    e = EXTRA[lang]
    if not os.path.exists(f"{OUT}/video/{name}.mp4"):
        return f'<img class="bg" src="{src(name)}" alt="" width="1344" height="768" fetchpriority="high">'
    return (f'<video class="bg" autoplay muted loop playsinline preload="metadata" poster="{src("poster-" + name)}" aria-hidden="true"><source src="{PREFIX}/video/{name}.mp4" type="video/mp4"></video>'
            f'<button class="vtoggle" type="button" data-pause="{e["pause"]}" data-play="{e["play"]}">{e["pause"]}</button>')
JS = """<script>(()=>{const m=matchMedia('(prefers-reduced-motion: reduce)');document.querySelectorAll('video.bg').forEach(v=>{const b=v.parentElement.querySelector('.vtoggle');if(m.matches){v.removeAttribute('autoplay');v.pause()}const set=()=>{b.textContent=v.paused?b.dataset.play:b.dataset.pause};b.addEventListener('click',()=>{v.paused?v.play():v.pause()});v.addEventListener('play',set);v.addEventListener('pause',set);set()});if(matchMedia('(hover:hover) and (pointer:fine)').matches&&!m.matches){document.querySelectorAll('.tile,.row,.feature').forEach(c=>{const k=c.classList.contains('feature')?3:c.classList.contains('row')?6:9,s=(p,v)=>c.style.setProperty(p,v);c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;s('--rx',-y*k+'deg');s('--ry',x*k+'deg');s('--mx',x*100+50+'%');s('--my',y*100+50+'%');s('--px',-x*16+'px');s('--py',-y*16+'px')});c.addEventListener('pointerleave',()=>['--rx','--ry','--px','--py'].forEach(p=>c.style.removeProperty(p)))})}})()</script>"""

def paths(lang):
    x = X[lang]; r = PREFIX + x["root"]
    p = {"home": r, "guides": f'{r}{x["guides"]}/', "about": f'{r}{x["about"]}/'}
    for i, c in enumerate(x["cats"]): p[f"cat{i}"] = f"{r}{c}/"
    for i, a in enumerate(ARTS): p[f"art{i}"] = f'{r}{x["guides"]}/{a["slug"][lang]}/'
    return p

def rows(lang, idx, cls=""):
    t, p = b.L[lang], paths(lang)
    out = "".join(f'''<a class="row" href="{p[f"art{i}"]}"><img src="{src(art_img(i))}" alt="" width="336" height="252" loading="lazy">
<span><span class="cat">{t["cats"][ARTS[i]["cat"]][0]}</span><h3>{ARTS[i][lang]["title"]}</h3></span></a>''' for i in idx)
    return f'<div class="rows {cls}">{out}</div>'

def crumbs(lang, trail):
    t, p = b.L[lang], paths(lang)
    items = [(t["home"], p["home"])] + trail
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(f'<a href="{h}">{n}</a>' for n, h in items) + "</nav>"

def page(lang, key, title, desc, body, image="hero", cls="", data="", kind="website"):
    t, x, e, p = b.L[lang], X[lang], EXTRA[lang], paths(lang)
    o = paths("en" if lang == "no" else "no")
    no, en = (p, o) if lang == "no" else (o, p)
    cur = lambda k: ' aria-current="page"' if key == k else ""
    nav = "".join(f'<a href="{p[f"cat{i}"]}"{cur(f"cat{i}")}>{t["nav"][i]}</a>' for i in range(4)) + f'<a href="{p["guides"]}"{cur("guides")}>{t["nav"][4]}</a>'
    catl = "".join(f'<li><a href="{p[f"cat{i}"]}">{t["nav"][i]}</a></li>' for i in range(4))
    info = "".join(f'<li><a href="{p["about"]}{a}">{n}</a></li>' for n, a in zip(x["foot"], x["anchors"]))
    doc = f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{p[key]}">
<link rel="alternate" hreflang="nb" href="{BASE}{no[key]}">
<link rel="alternate" hreflang="en" href="{BASE}{en[key]}">
<link rel="alternate" hreflang="x-default" href="{BASE}{en[key]}">
<link rel="icon" href="{PREFIX}/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}{src(image)}">
<meta property="og:url" content="{BASE}{p[key]}">
<meta property="og:type" content="{kind}">
<meta property="og:site_name" content="Nordic Trail Gear">
<meta property="og:locale" content="{"nb_NO" if lang == "no" else "en_GB"}">
<meta name="twitter:card" content="summary_large_image">
{data}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{PREFIX}/css/style.css?v=7">
</head>
<body class="{cls}">
<header class="top"><div class="wrap">
<a class="brand" href="{p["home"]}"><span class="mark">{MARK}</span>Nordic Trail Gear</a>
<nav class="nav" aria-label="Main">{nav}</nav>
<div class="lang"><a href="{no[key]}" lang="nb"{' aria-current="true"' if lang == "no" else ""}>NO</a><a href="{en[key]}" lang="en"{' aria-current="true"' if lang == "en" else ""}>EN</a></div>
</div></header>
<main>
{body}
</main>
<footer class="foot"><div class="wrap">
<div><a class="brand" href="{p["home"]}">{MARK}Nordic Trail Gear</a><p>{t["disc"]}</p></div>
<div><h2>{t["cats_h"]}</h2><ul>{catl}</ul></div>
<div><h2>{e["site"]}</h2><ul><li><a href="{p["guides"]}">{x["all_h"]}</a></li>{info}<li><a href="https://www.facebook.com/profile.php?id=61596897741938" rel="me noopener">Facebook</a></li></ul></div>
</div></footer>
{JS}
</body>
</html>'''
    d = OUT + p[key][len(PREFIX):]; os.makedirs(d, exist_ok=True)
    open(d + "index.html", "w", encoding="utf-8").write(doc)
    return p[key]

urls = []
dates = {}
for lang in ("no", "en"):
    t, x, e, p = b.L[lang], X[lang], EXTRA[lang], paths(lang)
    newest = list(reversed(range(len(ARTS))))
    f = newest[0]
    tiles = "".join(f'<a class="tile" href="{p[f"cat{i}"]}"><img src="{src(CATIMG[i])}" alt="" width="672" height="896" loading="lazy"><span><strong>{t["cats"][i][0]}</strong><small>{t["cats"][i][1]}</small></span></a>' for i in range(4))
    how = "".join(f"<div><h3>{a}</h3><p>{c}</p></div>" for a, c in t["how"])
    body = f'''<section class="hero">{bgvideo(lang, "hero")}
<div class="wrap"><h1>{t["h1"]}</h1><p>{t["sub"]}</p>
<div class="btns"><a class="btn btn-signal" href="{p["guides"]}">{t["cta"]}</a><a class="btn btn-line" href="{p["about"]}">{t["cta2"]}</a></div></div></section>
<section class="sec"><div class="wrap"><h2>{t["cats_h"]}</h2><div class="tiles">{tiles}</div></div></section>
<section class="sec"><div class="wrap"><h2>{t["guides_h"]}</h2>
<a class="feature" href="{p[f"art{f}"]}"><img src="{src(art_img(f))}" alt="" width="1344" height="840" loading="lazy">
<span><span class="cat">{t["cats"][ARTS[f]["cat"]][0]}</span><h3>{ARTS[f][lang]["title"]}</h3><p>{ARTS[f][lang]["lead"]}</p></span></a>
{rows(lang, newest[1:7])}</div></section>
<section class="band"><div class="wrap"><h2>{t["how_h"]}</h2><div class="cols">{how}</div></div></section>'''
    urls.append(page(lang, "home", f'Nordic Trail Gear – {t["tag"]}', x["desc"], body, cls="home", data=ld({"@type": "WebSite", "name": "Nordic Trail Gear", "url": BASE + p["home"], "inLanguage": t["lang"], "publisher": ORG}, ORG)))
    for i in range(4):
        name = t["cats"][i][0]
        h1 = t["cat_h1"] if i == 2 else name
        sub = t["cat_sub"] if i == 2 else x["subs"][i]
        idx = [k for k in newest if ARTS[k]["cat"] == i]
        inner = rows(lang, idx, "full") if idx else f'<p class="note">{x["none"]}</p>'
        body = f'''<section class="banner">{bgvideo(lang, CATIMG[i])}
<div class="wrap">{crumbs(lang, [(name, p[f"cat{i}"])])}<h1>{h1}</h1><p>{sub}</p></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap"><h2>{t["more_h"]}</h2>{inner}<p class="note">{t["disc"]}</p></div></section>'''
        urls.append(page(lang, f"cat{i}", f"{h1} – Nordic Trail Gear", sub, body, CATIMG[i], data=ld(crumb_ld(lang, [(name, p[f"cat{i}"])]))))
    body = f'''<section class="plain"><div class="wrap">{crumbs(lang, [(t["nav"][4], p["guides"])])}<h1>{x["all_h"]}</h1>{rows(lang, newest, "full")}</div></section>'''
    urls.append(page(lang, "guides", f'{x["all_h"]} – Nordic Trail Gear', x["desc"], body, data=ld(crumb_ld(lang, [(t["nav"][4], p["guides"])]))))
    for i, a in enumerate(ARTS):
        d, c = a[lang], a["cat"]
        rel = ([k for k in newest if k != i and ARTS[k]["cat"] == c] + [k for k in newest if k != i and ARTS[k]["cat"] != c])[:4]
        day = a.get("date", LAUNCH); dates[p[f"art{i}"]] = a.get("updated", day)
        data = ld({"@type": "Article", "headline": d["title"], "description": d["lead"], "image": [BASE + src(art_img(i))], "datePublished": day, "dateModified": a.get("updated", day), "inLanguage": t["lang"], "author": ORG, "publisher": ORG, "mainEntityOfPage": BASE + p[f"art{i}"]},
                  crumb_ld(lang, [(t["nav"][c], p[f"cat{c}"]), (t["nav"][4], p["guides"]), (d["title"], p[f"art{i}"])]))
        short = "".join(f"<li>{s}</li>" for s in d["short"])
        secs = "".join(f"<h2>{h}</h2><p>{txt}</p>" for h, txt in d["secs"])
        if d.get("html"):
            body = f'''<article class="article story-page"><section class="banner story-hero"><video class="bg" autoplay muted loop playsinline preload="metadata" poster="{src(d.get("hero", ("snohule-hero", "snohule-storm"))[1])}" aria-hidden="true"><source src="{PREFIX}/video/{d.get("hero", ("snohule-hero", "snohule-storm"))[0]}.mp4" type="video/mp4"></video><button class="vtoggle" type="button" data-pause="{e["pause"]}" data-play="{e["play"]}">{e["pause"]}</button>
<div class="wrap">{crumbs(lang, [(t["nav"][c], p[f"cat{c}"]), (t["nav"][4], p["guides"])])}<p class="kicker">{d["kicker"]}</p><h1>{d["title"]}</h1><p>{d["lead"]}</p><p class="date">{x["date"]}</p></div></section>
{d["html"]().replace("{P}", PREFIX)}</article>
<section class="sec"><div class="wrap"><h2>{e["more"]}</h2>{rows(lang, rel)}</div></section>'''
            urls.append(page(lang, f"art{i}", f'{d["title"]} – Nordic Trail Gear', d["lead"], body, art_img(i), data=data, kind="article"))
            continue
        body = f'''<article class="article"><header><div class="wrap">{crumbs(lang, [(t["nav"][c], p[f"cat{c}"]), (t["nav"][4], p["guides"])])}
<h1>{d["title"]}</h1><p class="date">{x["date"]}</p><p class="lede">{d["lead"]}</p></div></header>
<div class="wrap"><img class="lead-img" src="{src(art_img(i))}" alt="" width="1344" height="756" fetchpriority="high"></div>
<div class="wrap narrow body"><section class="short"><h2>{t["short_h"]}</h2><ul>{short}</ul></section>{secs}<p class="note">{t["disc"]}</p></div></article>
<section class="sec"><div class="wrap"><h2>{e["more"]}</h2>{rows(lang, rel)}</div></section>'''
        urls.append(page(lang, f"art{i}", f'{d["title"]} – Nordic Trail Gear', d["lead"], body, art_img(i), data=data, kind="article"))
    ids = [a[1:] for a in x["anchors"]]
    secs = "".join((f'<h1>{h}</h1><p style="margin-top:18px">{txt}</p>' if k == 0 else f'<h2 id="{ids[k]}">{h}</h2><p>{txt}</p>') for k, (h, txt) in enumerate(x["abt"]))
    body = f'<section class="plain"><div class="wrap narrow body" style="padding-top:0">{crumbs(lang, [(x["foot"][0], p["about"])])}{secs}</div></section>'
    urls.append(page(lang, "about", f'{x["abt"][0][0]}', x["abt"][0][1][:150], body))

# contour-line pattern for the dark band
rings = []
for cx, cy, n in ((300, 220, 9), (1050, 120, 7), (820, 430, 8)):
    for r in range(1, n + 1):
        pts = []
        for k in range(0, 361, 8):
            a = math.radians(k); rr = r * 34 * (1 + 0.16 * math.sin(3 * a + cx) + 0.09 * math.sin(5 * a + r))
            pts.append(f"{cx + rr * math.cos(a):.0f},{cy + rr * 0.72 * math.sin(a):.0f}")
        rings.append(f'<polygon points="{" ".join(pts)}"/>')
open(OUT + "/img/contour.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 520" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#fff" stroke-opacity=".09" stroke-width="1.2">{"".join(rings)}</g></svg>')
open(OUT + "/img/contour-dark.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 520" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="#1F5C4A" stroke-opacity=".13" stroke-width="1.2">{"".join(rings)}</g></svg>')

open(OUT + "/.nojekyll", "w").write("")
open(OUT + "/index.html", "w").write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Nordic Trail Gear</title><meta name="viewport" content="width=device-width, initial-scale=1"><script>location.replace(/^(nb|no|nn)/i.test(navigator.language||"")?"no/":"en/")</script><noscript><meta http-equiv="refresh" content="0; url=en/"></noscript></head><body><a href="en/">English</a> · <a href="no/">Norsk</a></body></html>')
open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE}{u}</loc><lastmod>{dates.get(u, TODAY)}</lastmod></url>" for u in urls) + "</urlset>")
open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}{PREFIX}/sitemap.xml\n")
print(len(urls), "pages")
