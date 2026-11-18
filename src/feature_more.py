# Feature stories 3 and 4. {P} is replaced with the site prefix.
def photo(name, cap): return f'<figure class="shot"><img src="{{P}}/img/{name}.webp" alt="" width="1600" height="900" loading="lazy"><figcaption>{cap}</figcaption></figure>'
def video(lang, name, poster, cap, label):
    return f'''<figure class="film"><video controls playsinline preload="metadata" poster="{{P}}/img/{poster}.webp">
<source src="{{P}}/video/{name}.mp4" type="video/mp4">
<track kind="subtitles" src="{{P}}/video/{name}.{lang}.vtt" srclang="{'nb' if lang == 'no' else 'en'}" label="{label}"{' default' if lang == 'no' else ''}>
</video><figcaption>{cap}</figcaption></figure>'''
def srcs(S): return "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in S)
def rules(items, start): return f'<ol class="rules" style="--s:{start}">' + "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in items) + "</ol>"
def packs(groups): return '<div class="packs">' + "".join(f'<section><h3>{h}</h3><ul>' + "".join(f"<li>{i}</li>" for i in its) + "</ul></section>" for h, its in groups) + "</div>"
W = lambda x: f'<div class="wrap narrow body story">{x}</div>'
WW = lambda x: f'<div class="wrap">{x}</div>'

S3 = [("Røde Kors og DNT: Fjellvettreglene", "https://www.rodekors.no/contentassets/b15ab4b7971d40f6875124c69858f758/fjellvettreglene-norsk.pdf"),
 ("Store norske leksikon: Fjellvettreglene", "https://snl.no/fjellvettreglene"),
 ("DNT: The Norwegian Mountain Code", "https://www.dnt.no/en/mountaincode"),
 ("DNT: Husk vindsekk på fjelltur", "https://www.dnt.no/en/Trips/tips-and-tricks/articles/bivvy-bag")]
S4 = [("DNT: Pakkeliste for vintertur i fjellet", "https://www.dnt.no/en/Trips/Tips-and-tricks/articles/Packing-list-for-the-mountain-winter-trip/"),
 ("DNT: Husk vindsekk på fjelltur", "https://www.dnt.no/en/Trips/tips-and-tricks/articles/bivvy-bag"),
 ("Røde Kors og DNT: Fjellvettreglene", "https://www.rodekors.no/contentassets/b15ab4b7971d40f6875124c69858f758/fjellvettreglene-norsk.pdf")]

FJ_NO = dict(
 title="Fjellvettreglene forklart: ni setninger som ble til etter en ulykkespåske",
 lead="Påsken 1967 mistet 17 mennesker livet i norske fjell. Samme år kom kampanjen som gjorde ni korte regler til felleseie. Her er hva hver av dem betyr i praksis.",
 short=["Tre regler gjelder før du drar: planlegg, tilpass, sjekk varslene.", "To gjelder sekken: vær forberedt, og ta med det som trengs.", "Fire gjelder underveis: trygge veivalg, kart og kompass, snu i tide, søk ly."],
 secs=[], kicker="Hvorfor kan nesten alle nordmenn «det er ingen skam å snu»?", hero=("fjellvett-hero", "fjellvett-kvister"),
 html=lambda: W('''<p class="drop">Det finnes få tekster nordmenn kan like godt som fjellvettreglene. De henger på hytteveggen og dukker opp overalt før påske. Men det er lett å kunne dem utenat uten å tenke over hva de ber deg om.</p>
<p>Reglene er laget av Den Norske Turistforening og Røde Kors. Store norske leksikon forteller at de første ni reglene kom i 1952, etter flere dødsfall i påskefjellet to år tidligere. Femten år senere, i 1967, omkom 17 mennesker i påskefjellet. Samme år startet kampanjen «Velkommen til fjells – men ta ansvaret selv».</p>
<p>I 2016 ble reglene skrevet om for å passe til hvordan folk bruker fjellet nå, med mer toppturer og bratt terreng. Det er den utgaven som gjelder i dag.</p>
<aside class="num"><strong>9 regler</strong><span>i tre grupper: tre før du drar, to for sekken og fire for selve turen. Slik er de lettere å huske.</span></aside>
<h2>Se alle ni på ett minutt</h2><p>Fortellerstemmen er engelsk, med norsk tekst.</p>''') + WW(video("no", "fjellvett", "fjellvett-kart", "Film: Nordic Trail Gear. Bildene er laget med KI.", "Norsk")) + W('''<h2>Før du drar</h2><p>De tre første reglene handler om det du gjør hjemme. Det er her de fleste dårlige turer kan stoppes.</p>''' + rules([
 ("Planlegg turen og meld fra hvor du går.", "Lag en plan som tåler at noe tar lengre tid. Si fra til noen hvor du skal og når du er tilbake, så vet de hvor de skal lete."),
 ("Tilpass turen etter evne og forhold.", "Turen skal passe den svakeste i følget og dagens føre. En tur som var fin i fjor, kan være for lang i år."),
 ("Ta hensyn til vær- og skredvarsel.", "Les varslene for området du skal til, og forstå hva de betyr for ruta di. Velg enklere terreng når forholdene er krevende.")], 1)) + WW(photo("fjellvett-plan", "Planleggingen gjøres ved kjøkkenbordet. Illustrasjon laget med KI.")) + W('''<h2>I sekken</h2><p>De to neste handler om hva du har med. De gjelder også på korte turer, for det er der folk oftest går uten.</p>''' + rules([
 ("Vær forberedt på uvær og kulde, selv på korte turer.", "Ha med ekstra klær, mat og drikke. Været i fjellet kan snu fortere enn varselet sa."),
 ("Ta med nødvendig utstyr for å kunne hjelpe deg selv og andre.", "Om vinteren betyr det vindsekk, liggeunderlag, sovepose og spade, slik at du klarer en natt ute.")], 4) + '''<p>Vil du se hva dette betyr i praksis, har vi skrevet om <a href="{P}/no/guider/uforutsett-natt-ute/">natta du ikke planla</a> og om <a href="{P}/no/guider/pakkeliste-vintertur/">hva som skal i sekken</a>.</p>''') + WW(photo("fjellvett-kart", "Kart og kompass virker også når telefonen er tom. Illustrasjon laget med KI.")) + W('''<h2>Underveis</h2><p>De fire siste gjelder valgene du tar mens du går. De er de vanskeligste å følge, fordi de ofte betyr å gi opp noe du hadde gledet deg til.</p>''' + rules([
 ("Ta trygge veivalg. Gjenkjenn skredfarlig terreng og usikker is.", "Lær deg å se hvor det er bratt nok til at skred kan gå, og hold deg unna når du er i tvil."),
 ("Bruk kart og kompass. Vit alltid hvor du er.", "Følg med på kartet hele veien, ikke bare når sikten forsvinner. Da er det for sent å finne ut hvor du står."),
 ("Vend i tide, det er ingen skam å snu.", "Bestem på forhånd når dere snur, og hold dere til det. Endre planen lenge før noen er utslitt."),
 ("Spar på kreftene og søk ly om nødvendig.", "Gå i et tempo alle holder hele dagen. Kommer uværet, søker du ly mens du har krefter igjen. Les om <a href=\"{P}/no/guider/snohule-i-snostorm/\">hvordan du graver en snøhule</a>.")], 6)) + WW(photo("fjellvett-snu", "Å snu er et valg, ikke et nederlag. Illustrasjon laget med KI.")) + W('''<h2>Hvorfor de fortsatt virker</h2><p>Ingen av reglene handler om utstyr du må kjøpe eller ferdigheter du må ha. De handler om å ta beslutninger tidlig, mens du har god tid og god oversikt. Det er derfor de er like nyttige på en søndagstur som på en ukestur.</p>
<p>Les dem hjemme. Da husker du dem når det blåser.</p>
<aside class="next"><h2>Les videre</h2><ul>
<li><a href="{P}/no/guider/pakkeliste-vintertur/">Pakkeliste for vintertur: dette skal i sekken</a></li>
<li><a href="{P}/no/guider/uforutsett-natt-ute/">Natta du ikke planla</a></li>
<li><a href="{P}/no/guider/snohule-i-snostorm/">Slik graver du en snøhule når uværet kommer</a></li></ul></aside>
<section class="sources"><h2>Kilder</h2><ul>''' + srcs(S3) + '''</ul><p class="note">Regelteksten er gjengitt fra DNT og Røde Kors. Forklaringene er våre egne og erstatter ikke kurs eller erfaring. Bilder og film er laget med KI og viser ikke virkelige hendelser.</p></section>'''))

FJ_EN = dict(
 title="The Norwegian mountain code explained: nine sentences born from a deadly Easter",
 lead="At Easter 1967, 17 people lost their lives in the Norwegian mountains. The same year, a campaign made nine short rules common knowledge. Here is what each of them means in practice.",
 short=["Three rules apply before you leave: plan, adapt, check the forecasts.", "Two are about the pack: be prepared, and bring what is needed.", "Four apply on the way: safe routes, map and compass, turn back in time, seek shelter."],
 secs=[], kicker="Why does almost every Norwegian know the phrase “there is no shame in turning around”?", hero=("fjellvett-hero", "fjellvett-kvister"),
 html=lambda: W('''<p class="drop">Few texts are as familiar to Norwegians as the mountain code, fjellvettreglene. It hangs on cabin walls and turns up everywhere before Easter. But it is easy to know the rules by heart without thinking about what they ask of you.</p>
<p>The rules come from the Norwegian Trekking Association (DNT) and the Red Cross. According to the encyclopedia Store norske leksikon, the first nine rules were published in 1952, after several deaths in the mountains at Easter two years earlier. Fifteen years later, in 1967, 17 people died in the mountains at Easter. The same year, the campaign “Welcome to the mountains, but take responsibility yourself” began.</p>
<p>In 2016 the rules were rewritten to fit how people use the mountains now, with more summit trips and steep terrain. That is the version in use today.</p>
<aside class="num"><strong>9 rules</strong><span>in three groups: three before you leave, two for the pack and four for the trip itself. They are easier to remember that way.</span></aside>
<h2>All nine in one minute</h2>''') + WW(video("en", "fjellvett", "fjellvett-kart", "Film: Nordic Trail Gear. The footage is AI-generated.", "English")) + W('''<h2>Before you leave</h2><p>The first three rules are about what you do at home. This is where most bad trips can be stopped.</p>''' + rules([
 ("Plan your trip and tell someone where you are going.", "Make a plan that still works if something takes longer. Tell someone where you are going and when you will be back, so they know where to look."),
 ("Adapt the trip to your ability and the conditions.", "The trip should suit the weakest person in the group and the conditions on the day. A trip that was fine last year can be too long this year."),
 ("Pay attention to the weather and avalanche forecasts.", "Read the forecasts for the area you are going to, and understand what they mean for your route. Choose easier terrain when conditions are demanding.")], 1)) + WW(photo("fjellvett-plan", "The planning happens at the kitchen table. AI-generated illustration.")) + W('''<h2>In the pack</h2><p>The next two are about what you carry. They apply on short trips too, because that is where people most often go without.</p>''' + rules([
 ("Be prepared for bad weather and cold, even on short trips.", "Bring extra clothes, food and drink. Mountain weather can turn faster than the forecast said."),
 ("Bring what you need to help yourself and others.", "In winter that means a wind sack, a sleeping pad, a sleeping bag and a shovel, so you can get through a night out.")], 4) + '''<p>To see what this means in practice, read about <a href="{P}/en/guides/unplanned-night-out/">the night you didn't plan</a> and <a href="{P}/en/guides/winter-packing-list/">what goes in the pack</a>.</p>''') + WW(photo("fjellvett-kart", "Map and compass still work when the phone is dead. AI-generated illustration.")) + W('''<h2>On the way</h2><p>The last four are about the choices you make while moving. They are the hardest to follow, because they often mean giving up something you were looking forward to.</p>''' + rules([
 ("Choose safe routes. Recognise avalanche terrain and unsafe ice.", "Learn to see where it is steep enough for avalanches to release, and stay away when you are in doubt."),
 ("Use a map and compass. Always know where you are.", "Follow the map all the way, not just when visibility goes. By then it is too late to work out where you are."),
 ("Turn back in time. There is no shame in turning around.", "Decide in advance when you will turn around, and stick to it. Change the plan long before anyone is exhausted."),
 ("Save your energy and seek shelter if necessary.", "Keep a pace everyone can hold all day. If the storm comes, seek shelter while you still have strength. Read <a href=\"{P}/en/guides/snow-cave-in-a-storm/\">how to dig a snow cave</a>.")], 6)) + WW(photo("fjellvett-snu", "Turning around is a choice, not a defeat. AI-generated illustration.")) + W('''<h2>Why they still work</h2><p>None of the rules is about gear you have to buy or skills you must have. They are about making decisions early, while you have time and a clear view. That is why they are as useful on a Sunday walk as on a week-long trip.</p>
<p>Read them at home. Then you remember them when the wind is blowing.</p>
<aside class="next"><h2>Read on</h2><ul>
<li><a href="{P}/en/guides/winter-packing-list/">Winter packing list: what goes in the pack</a></li>
<li><a href="{P}/en/guides/unplanned-night-out/">The night you didn't plan</a></li>
<li><a href="{P}/en/guides/snow-cave-in-a-storm/">How to dig a snow cave when the storm hits</a></li></ul></aside>
<section class="sources"><h2>Sources</h2><ul>''' + srcs(S3) + '''</ul><p class="note">The rule text follows DNT and the Red Cross. The explanations are our own and do not replace training or experience. Images and film are AI-generated and do not show real events.</p></section>'''))

PK_NO = dict(
 title="Pakkeliste for vintertur: dette skal i sekken",
 lead="En god vintertur starter på stuegulvet kvelden før. Legg alt utover, gruppe for gruppe, så ser du hva som mangler før du står i døra.",
 short=["Ull innerst, varmt mellomlag og vindtett ytterst.", "Vindsekk, liggeunderlag og sovepose skal alltid med, ifølge DNT.", "Utstyret veier vanligvis 10–14 kilo uten ski, støvler, mat og drikke."],
 secs=[], kicker="Hva trenger du egentlig med deg?", hero=("pakk-hero", "pakk-gulv"),
 html=lambda: W('''<p class="drop">Det er kvelden før turen. Skiene står smurt i gangen, og på stuegulvet ligger det klær, poser og småting i en haug som ikke ser ut til å få plass noe sted. Det er helt riktig. Slik skal det se ut.</p>
<p>Å legge alt utover før det går i sekken, er den enkleste kontrollen som finnes. Du ser hva du har, og du ser hva som mangler. Lista under følger pakkelista til Den Norske Turistforening for vintertur i fjellet, sortert i fem grupper.</p>
<aside class="num"><strong>10–14 kg</strong><span>veier utstyret vanligvis, ifølge DNT. Da er ski, støvler, staver, mat og drikke ikke regnet med. Selve sekken ender ofte på rundt åtte kilo.</span></aside>
<h2>Se hele lista på ett minutt</h2><p>Fortellerstemmen er engelsk, med norsk tekst.</p>''') + WW(video("no", "pakkeliste", "pakk-gulv", "Film: Nordic Trail Gear. Bildene er laget med KI.", "Norsk")) + W('''<h2>Fem grupper på gulvet</h2><p>Gå gjennom én gruppe om gangen. Det som ligger igjen på gulvet til slutt, har du glemt å tenke på.</p>''') + WW(packs([
 ("1. Det du har på deg", ["Ullundertøy og ullsokker", "Ullgenser eller fleece", "Vindtett jakke og bukse", "Lue og hals", "Vindvotter med ullvotter inni", "Skistøvler og gamasjer"]),
 ("2. Den tørre reserven", ["Ekstra lue, hals og votter", "Ekstra ullsokker", "Ett ekstra sett ullundertøy", "Tykk ullgenser eller dunjakke", "Regntøy hvis yttertøyet ikke er vanntett"]),
 ("3. Det du håper du aldri trenger", ["Vindsekk", "Liggeunderlag", "Varm sovepose", "Spade og søkestang", "Førstehjelpsutstyr med gnagsårplaster og sportstape", "Refleksvest"]),
 ("4. Det som finner veien", ["Kart, kompass og kartmappe", "Hodelykt", "Telefon og nødlader", "Skibriller"]),
 ("5. Det som holder deg i gang", ["Termos", "Mat og drikke til dagen", "Solbriller og solkrem", "Skismøring, eventuelt feller", "Multiverktøy og tape", "Fyrstikker eller lighter"])])) + WW(photo("pakk-klaer", "Vindtett ytterst, ull under. Illustrasjon laget med KI.")) + W('''<h2>Tre ting DNT sier alltid skal med</h2><p>Vindsekk, varm sovepose og liggeunderlag står i en særstilling på lista. DNT skriver at de alltid skal med på vintertur, fordi det er de som gjør at du klarer en natt ute hvis noe går galt. Les mer i saken om <a href="{P}/no/guider/uforutsett-natt-ute/">natta du ikke planla</a>.</p>
<p>Skredsøker, spade og søkestang hører sammen når du skal ferdes i skredterreng. DNT anbefaler å øve med utstyret før turen.</p>
<h2>To sett ull er lurere enn ett tykt</h2><p>DNT anbefaler to sett ullundertøy: ett du går i, og ett du holder tørt til du er framme. Det tørre settet er det som gir varmen tilbake etter en svett dag.</p>
<p>En isolert jakke er god å ha lett tilgjengelig. Den går utenpå alt i pausene, og du slipper å bli kald mens du spiser.</p>''') + WW(photo("pakk-kart", "Kart, kompass, hodelykt og telefon med nødlader. Illustrasjon laget med KI.")) + W('''<h2>Telefonen skal med, også uten dekning</h2><p>DNT ber deg ta med telefonen selv om du ikke har dekning, fordi den kan hjelpe redningstjenesten å finne deg. Ta med nødlader. Kulde tapper batterier fort, og det har vi skrevet mer om i guiden om <a href="{P}/no/guider/powerbank-kulde/">powerbank i kulde</a>.</p>
<p>Kart og kompass er likevel det du navigerer etter. De går ikke tomme for strøm.</p>''') + WW(photo("pakk-termos", "Termosen er verdt vekta. Illustrasjon laget med KI.")) + W('''<h2>Tung i døra, passe når været snur</h2><p>En sekk som er pakket etter lista, kjennes tung når du løfter den hjemme. Det meste av vekta er ting du håper du ikke får bruk for. Det er hele poenget. Den dagen været snur, er sekken akkurat passe.</p>
<aside class="next"><h2>Les videre</h2><ul>
<li><a href="{P}/no/guider/fjellvettreglene-forklart/">Fjellvettreglene forklart</a></li>
<li><a href="{P}/no/guider/lag-pa-lag/">Lag på lag: slik kler du deg til tur</a></li>
<li><a href="{P}/no/guider/sovepose-temperatur/">Sovepose: slik leser du temperaturmerkingen</a></li></ul></aside>
<section class="sources"><h2>Kilder</h2><ul>''' + srcs(S4) + '''</ul><p class="note">Lista bygger på DNTs pakkeliste for vintertur og er forkortet. Tilpass den til turen, været og følget ditt. Bilder og film er laget med KI.</p></section>'''))

PK_EN = dict(
 title="Winter packing list: what goes in the pack",
 lead="A good winter trip starts on the living room floor the night before. Lay everything out, group by group, and you will see what is missing before you are standing at the door.",
 short=["Wool next to the skin, a warm mid layer and windproof on the outside.", "A wind sack, a sleeping pad and a sleeping bag should always come along, according to DNT.", "The gear usually weighs 10–14 kilos, not counting skis, boots, food and drink."],
 secs=[], kicker="What do you actually need to bring?", hero=("pakk-hero", "pakk-gulv"),
 html=lambda: W('''<p class="drop">It is the night before the trip. The skis are waxed and standing in the hallway, and on the living room floor there is a pile of clothes, bags and small things that does not look like it will fit anywhere. That is exactly right. This is how it should look.</p>
<p>Laying everything out before it goes in the pack is the simplest check there is. You see what you have, and you see what is missing. The list below follows the Norwegian Trekking Association's (DNT) packing list for winter trips in the mountains, sorted into five groups.</p>
<aside class="num"><strong>10–14 kg</strong><span>is what the gear usually weighs, according to DNT. That is without skis, boots, poles, food and drink. The pack itself often ends up at around eight kilos.</span></aside>
<h2>The whole list in one minute</h2>''') + WW(video("en", "pakkeliste", "pakk-gulv", "Film: Nordic Trail Gear. The footage is AI-generated.", "English")) + W('''<h2>Five groups on the floor</h2><p>Go through one group at a time. Whatever is left on the floor at the end is what you forgot to think about.</p>''') + WW(packs([
 ("1. What you wear", ["Wool base layers and wool socks", "Wool sweater or fleece", "Windproof jacket and trousers", "Hat and neck gaiter", "Windproof mittens with wool mittens inside", "Ski boots and gaiters"]),
 ("2. The dry reserve", ["Extra hat, neck gaiter and mittens", "Extra wool socks", "One extra set of wool base layers", "Thick wool sweater or down jacket", "Rain gear if your outer layer is not waterproof"]),
 ("3. What you hope you never need", ["Wind sack", "Sleeping pad", "Warm sleeping bag", "Shovel and probe", "First aid kit with blister plasters and sports tape", "Reflective vest"]),
 ("4. What finds the way", ["Map, compass and map case", "Headlamp", "Phone and power bank", "Ski goggles"]),
 ("5. What keeps you going", ["Thermos", "Food and drink for the day", "Sunglasses and sunscreen", "Ski wax, possibly skins", "Multi-tool and tape", "Matches or a lighter"])])) + WW(photo("pakk-klaer", "Windproof on the outside, wool underneath. AI-generated illustration.")) + W('''<h2>Three things DNT says should always come along</h2><p>The wind sack, the warm sleeping bag and the sleeping pad have a special place on the list. DNT writes that they should always be included on winter trips, because they are what gets you through a night out if something goes wrong. Read more in the story about <a href="{P}/en/guides/unplanned-night-out/">the night you didn't plan</a>.</p>
<p>An avalanche transceiver, shovel and probe belong together when you travel in avalanche terrain. DNT recommends practising with the gear before the trip.</p>
<h2>Two sets of wool beat one thick one</h2><p>DNT recommends two sets of wool base layers: one to ski in, and one kept dry until you arrive. The dry set is what brings the warmth back after a sweaty day.</p>
<p>An insulated jacket is good to keep within easy reach. It goes on over everything during breaks, so you do not get cold while you eat.</p>''') + WW(photo("pakk-kart", "Map, compass, headlamp and a phone with a power bank. AI-generated illustration.")) + W('''<h2>Bring the phone, even without coverage</h2><p>DNT asks you to bring your phone even where there is no signal, because it can help rescuers find you. Bring a power bank. Cold drains batteries quickly, which we cover in the guide to <a href="{P}/en/guides/power-bank-cold/">power banks in the cold</a>.</p>
<p>Map and compass are still what you navigate by. They do not run out of power.</p>''') + WW(photo("pakk-termos", "The thermos is worth its weight. AI-generated illustration.")) + W('''<h2>Heavy at the door, just right when the weather turns</h2><p>A pack filled from this list feels heavy when you lift it at home. Most of the weight is things you hope you will not use. That is the whole point. On the day the weather turns, the pack is just right.</p>
<aside class="next"><h2>Read on</h2><ul>
<li><a href="{P}/en/guides/mountain-code-explained/">The Norwegian mountain code explained</a></li>
<li><a href="{P}/en/guides/layering/">Layering: how to dress for the outdoors</a></li>
<li><a href="{P}/en/guides/sleeping-bag-ratings/">Sleeping bags: how to read the temperature ratings</a></li></ul></aside>
<section class="sources"><h2>Sources</h2><ul>''' + srcs(S4) + '''</ul><p class="note">The list is based on DNT's packing list for winter trips and is shortened. Adapt it to the trip, the weather and your group. Images and film are AI-generated.</p></section>'''))

ARTS = [dict(cat=0, slug=dict(no="fjellvettreglene-forklart", en="mountain-code-explained"), img="fjellvett-kart", feature=True, no=FJ_NO, en=FJ_EN),
        dict(cat=0, slug=dict(no="pakkeliste-vintertur", en="winter-packing-list"), img="pakk-gulv", feature=True, no=PK_NO, en=PK_EN)]
