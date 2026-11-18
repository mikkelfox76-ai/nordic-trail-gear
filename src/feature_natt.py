# Feature story: an unplanned night out. {P} is replaced with the site prefix.
SRC = [
 ("DNT: Husk vindsekk på fjelltur", "https://www.dnt.no/en/Trips/tips-and-tricks/articles/bivvy-bag"),
 ("Røde Kors og DNT: Fjellvettreglene", "https://www.rodekors.no/contentassets/b15ab4b7971d40f6875124c69858f758/fjellvettreglene-norsk.pdf"),
 ("Norsk Helseinformatikk: Førstehjelp ved nedkjøling", "https://nhi.no/forstehjelp/varmekuldeskader/nedkjoling-hypotermi"),
 ("Dagbladet: Røde Kors om ventetid på redning", "https://www.dagbladet.no/nyheter/dette-redder-liv/73630826"),
]
def fig(lang, k, cap): return f'<figure><img src="{{P}}/img/natt-fig{k}-{lang}.webp" alt="" width="1350" height="630" loading="lazy"><figcaption>{cap}</figcaption></figure>'
def photo(name, cap): return f'<figure class="shot"><img src="{{P}}/img/natt-{name}.webp" alt="" width="1600" height="900" loading="lazy"><figcaption>{cap}</figcaption></figure>'
def video(lang, cap, label):
    return f'''<figure class="film"><video controls playsinline preload="metadata" poster="{{P}}/img/natt-vindsekk.webp">
<source src="{{P}}/video/natt-ute.mp4" type="video/mp4">
<track kind="subtitles" src="{{P}}/video/natt-ute.{lang}.vtt" srclang="{'nb' if lang == 'no' else 'en'}" label="{label}"{' default' if lang == 'no' else ''}>
</video><figcaption>{cap}</figcaption></figure>'''
def srcs(): return "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in SRC)

NO = dict(
 title="Natta du ikke planla: slik klarer du deg med det du har i sekken",
 lead="En forstuet ankel, et feil veivalg eller et uvær som kom for tidlig. Plutselig blir dagsturen til en natt ute. Her er det som holder deg varm til det lysner.",
 short=["Stopp mens du har krefter, og finn le for vinden.", "Stopp de tre varmetyvene: vind, kald bakke og våte klær.", "Vindsekk, liggeunderlag, sovepose og spade er det du trenger i sekken om vinteren."],
 secs=[], kicker="Hva gjør du når mørket kommer før du er hjemme?",
 hero=("natt-hero", "natt-skumring"),
 html=lambda: f'''
<div class="wrap narrow body story">
<p class="drop">Dere skulle vært nede ved bilen for en time siden. Men så tråkket den ene av dere over, og tempoet falt til det halve. Nå blir lyset blått, vinden tar seg opp, og det er fortsatt langt igjen.</p>
<p>De fleste netter ute som ikke var planlagt, begynner slik. Ikke med et stort drama, men med noe lite som tar tid. Det farlige er sjelden selve skaden. Det er kulden som kommer mens dere venter.</p>
<p>Røde Kors har pekt på at det kan ta lang tid før hjelpen kommer fram når været er dårlig og helikopteret ikke kan fly. I mellomtiden er det dere selv som må holde varmen.</p>

<aside class="num"><strong>500 gram</strong><span>veier en vindsekk, ifølge DNT. Den rommer to voksne og et barn, og DNT kaller den obligatorisk på vintertur i fjellet.</span></aside>

<h2>Se hele natta på ett minutt</h2>
<p>Filmen viser hva som stjeler varmen, og hva du gjør med det. Fortellerstemmen er engelsk, med norsk tekst.</p>
</div>
<div class="wrap">{video("no", "Film: Nordic Trail Gear. Bildene er laget med KI.", "Norsk")}</div>

<div class="wrap narrow body story">
<h2>Først: stopp i tide</h2>
<p>Fjellvettreglene sier at du skal være forberedt på uvær og kulde, selv på korte turer, og at du skal søke ly om nødvendig. Det vanskelige er å bestemme seg. Å stoppe føles som å gi opp.</p>
<p>Men det er lettere å lage ly mens fingrene virker og hodet er klart. Finn le for vinden, bak en stein, en skavl eller en kant i terrenget.</p>
</div>
<div class="wrap">{photo("vindsekk", "Nede på bakken, i le av steinen og på liggeunderlaget, med vindsekken rundt seg. Illustrasjon laget med KI.")}</div>

<div class="wrap narrow body story">
<h2>Så: stopp de tre varmetyvene</h2>
<p>Nedkjøling oppstår når kroppen taper mer varme enn den lager. Norsk Helseinformatikk peker på at vind og fuktighet får det til å gå fortere. I tillegg kommer bakken du sitter på.</p>
</div>
<div class="wrap"><div class="steps">
{fig("no", 1, "<strong>Tre ting stjeler varmen.</strong> Vinden blåser den bort, bakken trekker den ut nedenfra, og våte klær holder ikke på den.")}
{fig("no", 2, "<strong>1. Vindsekken stopper vinden.</strong> Trekk den over dere og sett dere tett sammen. Den er vindtett, men den isolerer lite alene.")}
{fig("no", 3, "<strong>2. Sitt på noe.</strong> Bruk liggeunderlaget eller sekken, aldri rett på snøen eller bakken.")}
{fig("no", 4, "<strong>3. Tørt ytterst, lue på.</strong> Ta tørre lag utenpå og tørr lue på hodet. Spis, og drikk noe varmt.")}
</div></div>

<div class="wrap narrow body story">
<h2>Vindsekken er ikke en sovepose</h2>
<p>DNT er tydelig på begrensningen: En vindsekk gir godt vern mot vær og vind, men det blir kaldt å sitte lenge eller overnatte i den. Sovepose og liggeunderlag gir bedre vern mot kulden.</p>
<p>Derfor er rekkefølgen i sekken viktig. Vindsekken stopper vinden. Underlaget stopper bakken. Soveposen holder på varmen du har. Og om vinteren gjør spaden at du kan <a href="{{P}}/no/guider/snohule-i-snostorm/">grave deg inn i snøen</a> når den er dyp nok.</p>
</div>
<div class="wrap">{photo("utstyr", "Vindsekk, spade, liggeunderlag, sovepose, termos, hodelykt og votter. Illustrasjon laget med KI.")}</div>

<div class="wrap narrow body story">
<section class="short"><h2>Tegn på nedkjøling du skal se etter hos hverandre</h2><ul>
<li><strong>Skjelving.</strong></li>
<li><strong>Utydelig tale.</strong></li>
<li><strong>Klossete bevegelser.</strong></li>
<li><strong>Trøtthet og likegyldighet.</strong> Den som er nedkjølt, merker det ofte ikke selv.</li>
</ul></section>
<p>Ser du disse tegnene, skjerm personen mot vinden, dekk til hodet og få noe mellom kroppen og bakken. Kan dere ikke bytte våte klær uten at det blir kaldere, tar dere tørre klær utenpå de våte. Gi varm drikke uten alkohol. Ring 113.</p>

<h2>Gjør dere lette å finne</h2>
<p>Ring tidlig hvis dere trenger hjelp, mens telefonen har strøm og dere vet hvor dere er. 112 er nødnummeret til politiet, som leder redningsaksjoner. 113 er medisinsk nødhjelp. Spar på batteriet etterpå, og ha hodelykta klar.</p>
</div>
<div class="wrap">{photo("lys", "Lys i mørket gjør det lettere å finne dere. Illustrasjon laget med KI.")}</div>

<div class="wrap narrow body story">
<h2>Morgenen etter</h2>
<p>En natt ute med riktig utstyr er lang, kald og kjedelig. Uten det kan den bli farlig. Forskjellen veier noen få kilo og ligger nederst i sekken på alle turer der du kan bli værende lenger enn planlagt.</p>
<p>Prøv vindsekken i en matpause før du trenger den. Da vet dere hvordan dere kommer inn i den når det blåser.</p>

<aside class="next"><h2>Les videre</h2><ul>
<li><a href="{{P}}/no/guider/snohule-i-snostorm/">Slik graver du en snøhule når uværet kommer</a></li>
<li><a href="{{P}}/no/guider/lag-pa-lag/">Lag på lag: slik kler du deg til tur</a></li>
<li><a href="{{P}}/no/guider/hodelykt-vinter/">Hodelykt til vinterbruk</a></li>
</ul></aside>

<section class="sources"><h2>Kilder</h2><ul>{srcs()}</ul>
<p class="note">Saken gir generelle råd og erstatter ikke kurs i førstehjelp eller egen erfaring. Bilder og film er laget med KI og viser ikke en virkelig hendelse.</p></section>
</div>''')

EN = dict(
 title="The night you didn't plan: getting through it with what's in your pack",
 lead="A twisted ankle, a wrong turn or a storm that arrived early. Suddenly the day trip becomes a night out. This is what keeps you warm until it gets light.",
 short=["Stop while you still have energy, and get out of the wind.", "Stop the three heat thieves: wind, cold ground and wet clothes.", "A wind sack, a sleeping pad, a sleeping bag and a shovel are what you need in the pack in winter."],
 secs=[], kicker="What do you do when darkness comes before you are home?",
 hero=("natt-hero", "natt-skumring"),
 html=lambda: f'''
<div class="wrap narrow body story">
<p class="drop">You should have been back at the car an hour ago. But then one of you rolled an ankle, and the pace dropped by half. Now the light is turning blue, the wind is picking up, and there is still a long way to go.</p>
<p>Most unplanned nights out begin like this. Not with a big drama, but with something small that takes time. The danger is rarely the injury itself. It is the cold that arrives while you wait.</p>
<p>The Norwegian Red Cross has pointed out that help can take a long time to reach you when the weather is bad and the helicopter cannot fly. Until then, keeping warm is up to you.</p>

<aside class="num"><strong>500 grams</strong><span>is what a wind sack weighs, according to the Norwegian Trekking Association (DNT). It holds two adults and a child, and DNT calls it mandatory on winter trips in the mountains.</span></aside>

<h2>The whole night in one minute</h2>
<p>The film shows what steals your warmth, and what to do about it.</p>
</div>
<div class="wrap">{video("en", "Film: Nordic Trail Gear. The footage is AI-generated.", "English")}</div>

<div class="wrap narrow body story">
<h2>First: stop in time</h2>
<p>The Norwegian mountain code says to be prepared for bad weather and cold, even on short trips, and to seek shelter if necessary. The hard part is deciding. Stopping feels like giving up.</p>
<p>But it is easier to make shelter while your fingers work and your head is clear. Get out of the wind, behind a boulder, a snowdrift or an edge in the terrain.</p>
</div>
<div class="wrap">{photo("vindsekk", "Down on the ground, sheltered by the boulder and on the sleeping pad, with the wind sack around them. AI-generated illustration.")}</div>

<div class="wrap narrow body story">
<h2>Then: stop the three heat thieves</h2>
<p>Hypothermia sets in when the body loses more heat than it produces. The Norwegian health reference NHI points out that wind and moisture speed it up. Then there is the ground you sit on.</p>
</div>
<div class="wrap"><div class="steps">
{fig("en", 1, "<strong>Three things steal your warmth.</strong> The wind blows it away, the ground draws it out from below, and wet clothes do not hold it.")}
{fig("en", 2, "<strong>1. The wind sack stops the wind.</strong> Pull it over you and sit close together. It is windproof, but it insulates little on its own.")}
{fig("en", 3, "<strong>2. Sit on something.</strong> Use your sleeping pad or your pack, never straight on the snow or the ground.")}
{fig("en", 4, "<strong>3. Dry on the outside, hat on.</strong> Put dry layers on top and a dry hat on your head. Eat, and drink something warm.")}
</div></div>

<div class="wrap narrow body story">
<h2>A wind sack is not a sleeping bag</h2>
<p>DNT is clear about the limit: a wind sack protects well against wind and weather, but it gets cold if you sit for a long time or spend the night in it. A sleeping bag and a sleeping pad protect better against the cold.</p>
<p>That is why the order in the pack matters. The wind sack stops the wind. The pad stops the ground. The sleeping bag keeps the warmth you have. And in winter, the shovel lets you <a href="{{P}}/en/guides/snow-cave-in-a-storm/">dig into the snow</a> when it is deep enough.</p>
</div>
<div class="wrap">{photo("utstyr", "Wind sack, shovel, sleeping pad, sleeping bag, flask, headlamp and mittens. AI-generated illustration.")}</div>

<div class="wrap narrow body story">
<section class="short"><h2>Signs of hypothermia to watch for in each other</h2><ul>
<li><strong>Shivering.</strong></li>
<li><strong>Slurred speech.</strong></li>
<li><strong>Clumsy movements.</strong></li>
<li><strong>Tiredness and apathy.</strong> The person who is cold often does not notice it.</li>
</ul></section>
<p>If you see these signs, shield the person from the wind, cover their head and get something between their body and the ground. If you cannot change wet clothes without making things colder, put dry clothes on top of the wet ones. Give warm drinks without alcohol. In Norway, call 113.</p>

<h2>Make yourselves easy to find</h2>
<p>Call early if you need help, while the phone has power and you know where you are. In Norway, 112 is the police emergency number, and the police lead rescue operations. 113 is for medical emergencies. Save the battery afterwards, and keep your headlamp ready.</p>
</div>
<div class="wrap">{photo("lys", "Light in the dark makes you easier to find. AI-generated illustration.")}</div>

<div class="wrap narrow body story">
<h2>The morning after</h2>
<p>A night out with the right gear is long, cold and boring. Without it, it can be dangerous. The difference weighs a few kilos and sits at the bottom of the pack on every trip where you might end up staying longer than planned.</p>
<p>Try the wind sack during a lunch break before you need it. Then you know how to get inside it when the wind is blowing.</p>

<aside class="next"><h2>Read on</h2><ul>
<li><a href="{{P}}/en/guides/snow-cave-in-a-storm/">How to dig a snow cave when the storm hits</a></li>
<li><a href="{{P}}/en/guides/layering/">Layering: how to dress for the outdoors</a></li>
<li><a href="{{P}}/en/guides/winter-headlamp/">Headlamps for winter use</a></li>
</ul></aside>

<section class="sources"><h2>Sources</h2><ul>{srcs()}</ul>
<p class="note">This article gives general advice and does not replace first-aid training or experience. Images and film are AI-generated and do not show a real event.</p></section>
</div>''')

ART = dict(cat=0, slug=dict(no="uforutsett-natt-ute", en="unplanned-night-out"), img="natt-vindsekk", feature=True, no=NO, en=EN)
