# Feature story: snow cave. Custom long-form layout; {P} is replaced with the site prefix.
SRC = [
 ("Store norske leksikon: Snøhule", "https://snl.no/sn%C3%B8hule"),
 ("Røde Kors og DNT: Fjellvettreglene", "https://www.rodekors.no/contentassets/b15ab4b7971d40f6875124c69858f758/fjellvettreglene-norsk.pdf"),
 ("Villmarksliv: Snøhule på én-to-tre", "https://www.klikk.no/helse/trening/tester/snohule-pa-n-to-tre-2490496"),
 ("SINTEF Byggforsk: Snøhule (S 330.140)", "https://byggforsk.no/file/index/4768"),
 ("Norges speiderforbund, Vestmarka: Alternative snøbivuakker", "https://vestmarka.speiding.no/wp-content/uploads/sites/275/2023/02/alternative-snobivuakker.pdf"),
]

def fig(lang, k, cap):
    return f'<figure><img src="{{P}}/img/snohule-fig{k}-{lang}.webp" alt="" width="1350" height="630" loading="lazy"><figcaption>{cap}</figcaption></figure>'

def photo(name, cap, cls=""):
    return f'<figure class="shot {cls}"><img src="{{P}}/img/snohule-{name}.webp" alt="" width="1600" height="900" loading="lazy"><figcaption>{cap}</figcaption></figure>'

def video(lang, cap, label):
    return f'''<figure class="film"><video controls playsinline preload="metadata" poster="{{P}}/img/snohule-natt.webp">
<source src="{{P}}/video/snohule.mp4?v=2" type="video/mp4">
<track kind="subtitles" src="{{P}}/video/snohule.{lang}.vtt" srclang="{'nb' if lang == 'no' else 'en'}" label="{label}"{' default' if lang == 'no' else ''}>
</video><figcaption>{cap}</figcaption></figure>'''

NO = dict(
 title="Slik graver du en snøhule når uværet kommer",
 lead="Sikten forsvinner, vinden øker, og hytta er fortsatt to timer unna. Da kan en spade og en snøskavl være det tryggeste valget. Bli med inn i hula, steg for steg.",
 short=["Søk ly tidlig, mens du fortsatt har krefter til å grave.", "Grav i en skavl på lesiden, unna skredterreng.", "Sov høyere enn inngangen, og hold luftehullet åpent."],
 secs=[],
 kicker="Hva gjør du når du ikke rekker fram?",
 html=lambda: f'''
<div class="wrap narrow body story">
<p class="drop">Klokka er litt over to. For en time siden så du hele dalen. Nå ser du skituppene dine og omtrent ti meter til. Vinden har snudd, snøen går vannrett, og sporet bak deg er allerede borte.</p>
<p>Det er her mange gjør feilen. De går videre. Litt til, bare over neste rygg. Men det koster krefter å gå i motvind og dårlig sikt, og krefter er det du trenger for å holde varmen.</p>
<p>Den niende fjellvettregelen fra DNT og Røde Kors er kort: <strong>Spar på kreftene og søk ly om nødvendig.</strong> Poenget er rekkefølgen. Du skal søke ly mens du fortsatt har krefter til å lage det.</p>

<aside class="num"><strong>2 timer</strong><span>bruker to personer på en god snøhule når snøen er grei å grave i, ifølge Villmarksliv. Hard snø eller islag kan doble tiden.</span></aside>

<h2>Se hele turen på ett minutt</h2>
<p>Filmen viser hele forløpet, fra uværet kommer til du ligger i hula. Fortellerstemmen er engelsk, med norsk tekst.</p>
</div>
<div class="wrap">{video("no", "Film: Nordic Trail Gear. Bildene er laget med KI, snittegningen er tegnet etter målene i kildene nederst.", "Norsk")}</div>

<div class="wrap narrow body story">
<h2>Først: finn riktig skavl</h2>
<p>En snøhule graves inn i en skavl, altså snø som vinden har lagt opp på lesiden av en rygg eller en kant. Store norske leksikon regner en skavl på fire til fem meter som ideell. Blir den høyere, øker faren for at hula raser.</p>
<p>Se oppover før du graver. Det skal ikke ligge skredfarlig terreng over deg. Stikk så en skistav eller søkestang inn i skavlen for å kjenne at snøen er dyp nok.</p>
</div>
<div class="wrap">{photo("skavl", "En skavl på lesiden av en rygg. Illustrasjon laget med KI.")}</div>

<div class="wrap narrow body story">
<h2>Så: grav i fire steg</h2>
<p>Du blir varm og fuktig av å grave. Ta av et lag før du begynner, ha hetta på, og legg tørre votter klare til etterpå.</p>
</div>
<div class="wrap"><div class="steps">
{fig("no", 1, "<strong>1. Gang og sovebenk.</strong> Grav en gang rett inn, omtrent så bred som skuldrene dine og så høy som deg. Grav deretter oppover og til sidene, og form sovebenker minst en halv meter over gulvet i gangen.")}
{fig("no", 2, "<strong>2. Kuldegropa.</strong> Kald luft er tyngre enn varm. Den synker ned i gangen og blir liggende der, mens du ligger i den varmere lufta over.")}
{fig("no", 3, "<strong>3. Tak og vegger.</strong> La det stå igjen minst en halv meter snø i tak og vegger. Glatt taket til en jevn bue, så det ikke drypper.")}
{fig("no", 4, "<strong>4. Luft og inngang.</strong> Stikk en skistav gjennom taket til luftehull, og hold det åpent. Tett den øvre delen av inngangen med snøblokker, så du må krype inn.")}
</div></div>

<div class="wrap narrow body story">
<h2>Inne i hula</h2>
<p>Det første du merker, er stillheten. Vinden som ropte utenfor, er blitt en svak dur. Lyset fra et stearinlys fyller hele rommet, fordi snøen kaster det tilbake.</p>
<p>Og det er varmere enn du tror. Store norske leksikon beskriver rundt minus 20 grader ytterst i kuldegropa og rundt null øverst i hula.</p>
</div>
<div class="wrap"><div class="pair">{photo("inne", "Sovebenken ligger høyere enn gangen. Illustrasjon laget med KI.")}{photo("graving", "Gangen graves rett inn i skavlen. Illustrasjon laget med KI.")}</div></div>

<div class="wrap narrow body story">
<section class="short"><h2>Fire ting du gjør før du legger deg</h2><ul>
<li><strong>Ta spaden med inn.</strong> Snøfokk kan tette inngangen i løpet av natta.</li>
<li><strong>Sett skiene rett opp i snøen utenfor.</strong> Da ser andre hvor du er.</li>
<li><strong>Tenn et stearinlys, et stykke fra tak og vegg.</strong> Brenner det dårlig, er det for lite oksygen. Da må du lufte.</li>
<li><strong>Sjekk luftehullet.</strong> Det skal være åpent hele natta.</li>
</ul></section>

<h2>Lufta er det du må passe på</h2>
<p>En snøhule er tett. Det er derfor den er varm, og det er derfor du må lufte. Store norske leksikon advarer om at dårlig luft er farlig når flere sover trangt, fordi du ikke merker symptomene mens du sover. Leksikonet anbefaler faste rutiner for å vekke hverandre.</p>
<p>Bruker du kokeapparat i hula, trenger du enda mer luft. SINTEF Byggforsk skriver at riktig ventilasjon er avgjørende.</p>

<h2>Finner du ingen skavl?</h2>
<p>På flatmark kan du grave en snøgrop: en grøft på omtrent en meters bredde, som du dekker med snøblokker. Den tar mer arbeid enn en hule i skavl, men den gir ly for vinden. Prinsippene er de samme: sitt høyere enn bunnen, og sørg for luft.</p>
</div>
<div class="wrap">{photo("natt", "Skiene står utenfor og viser hvor hula er. Illustrasjon laget med KI.")}</div>

<div class="wrap narrow body story">
<h2>Morgenen etter</h2>
<p>Uvær i fjellet går over. Det som avgjør, er om du har krefter og varme igjen når det skjer. Derfor ligger spaden i sekken på vintertur, sammen med vindsekk, liggeunderlag og sovepose. DNT og Røde Kors regner de fire som det du trenger for å klare en natt ute.</p>
<p>Og derfor bør den første snøhula di graves en fin dag, med kakao på termosen og god tid. Da vet hendene hva de skal gjøre den dagen du trenger det.</p>
<p>Er du i nød og har dekning, ring 112.</p>

<aside class="next"><h2>Les videre</h2><ul>
<li><a href="{{P}}/no/guider/sovepose-temperatur/">Sovepose: slik leser du temperaturmerkingen</a></li>
<li><a href="{{P}}/no/guider/liggeunderlag-r-verdi/">Liggeunderlag og R-verdi: hvor varmt trenger du?</a></li>
<li><a href="{{P}}/no/guider/lag-pa-lag/">Lag på lag: slik kler du deg til tur</a></li>
</ul></aside>

<section class="sources"><h2>Kilder</h2><ul>{"".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in SRC)}</ul>
<p class="note">Saken gir generelle råd og erstatter ikke kurs eller egen erfaring. Følg alltid vær- og skredvarsel. Bilder og film er laget med KI og viser ikke en virkelig hendelse.</p></section>
</div>''')

EN = dict(
 title="How to dig a snow cave when the storm hits",
 lead="Visibility is gone, the wind is rising and the cabin is still two hours away. A shovel and a snowdrift may be your safest option. Come inside the cave, step by step.",
 short=["Seek shelter early, while you still have the strength to dig.", "Dig into a drift on the sheltered side, away from avalanche terrain.", "Sleep higher than the entrance, and keep the air hole open."],
 secs=[],
 kicker="What do you do when you won't make it to the cabin?",
 html=lambda: f'''
<div class="wrap narrow body story">
<p class="drop">It is just past two. An hour ago you could see the whole valley. Now you can see your ski tips and about ten metres beyond them. The wind has turned, the snow is moving sideways, and the track behind you is already gone.</p>
<p>This is where many people make the mistake. They keep going. A bit further, just over the next ridge. But walking into the wind in poor visibility costs energy, and energy is what you need to stay warm.</p>
<p>The ninth rule of the Norwegian mountain code, from the Norwegian Trekking Association and the Red Cross, is short: <strong>save your energy and seek shelter if necessary.</strong> The point is the order. You seek shelter while you still have the strength to build it.</p>

<aside class="num"><strong>2 hours</strong><span>is what two people need for a good snow cave in snow that digs well, according to the Norwegian magazine Villmarksliv. Hard snow or ice layers can double that.</span></aside>

<h2>The whole night in one minute</h2>
<p>The film shows the full sequence, from the storm arriving to lying in the cave.</p>
</div>
<div class="wrap">{video("en", "Film: Nordic Trail Gear. The footage is AI-generated; the cross-section is drawn to the measurements in the sources below.", "English")}</div>

<div class="wrap narrow body story">
<h2>First: find the right drift</h2>
<p>A snow cave is dug into a drift, snow the wind has piled up on the sheltered side of a ridge or an edge. The Norwegian encyclopedia Store norske leksikon considers a drift of four to five metres ideal. Higher than that, and the risk of collapse goes up.</p>
<p>Look uphill before you dig. There should be no avalanche terrain above you. Then push a ski pole or a probe into the drift to check that the snow is deep enough.</p>
</div>
<div class="wrap">{photo("skavl", "A drift on the sheltered side of a ridge. AI-generated illustration.")}</div>

<div class="wrap narrow body story">
<h2>Then: dig in four steps</h2>
<p>Digging makes you warm and damp. Take off a layer before you start, keep your hood up, and have dry mittens ready for afterwards.</p>
</div>
<div class="wrap"><div class="steps">
{fig("en", 1, "<strong>1. Tunnel and sleeping bench.</strong> Dig a tunnel straight in, about as wide as your shoulders and as tall as you. Then dig upwards and to the sides, and shape sleeping benches at least half a metre above the tunnel floor.")}
{fig("en", 2, "<strong>2. The cold trap.</strong> Cold air is heavier than warm air. It sinks into the tunnel and stays there, while you lie in the warmer air above.")}
{fig("en", 3, "<strong>3. Roof and walls.</strong> Leave at least half a metre of snow in the roof and walls. Smooth the ceiling into an even dome so it does not drip.")}
{fig("en", 4, "<strong>4. Air and entrance.</strong> Push a ski pole through the roof to make an air hole, and keep it open. Close the upper part of the entrance with snow blocks, so you have to crawl in.")}
</div></div>

<div class="wrap narrow body story">
<h2>Inside the cave</h2>
<p>The first thing you notice is the silence. The wind that was shouting outside is now a faint hum. One candle lights the whole room, because the snow throws the light back.</p>
<p>And it is warmer than you expect. Store norske leksikon describes around minus 20 degrees at the outer end of the cold trap and around zero at the top of the cave.</p>
</div>
<div class="wrap"><div class="pair">{photo("inne", "The sleeping bench sits higher than the tunnel. AI-generated illustration.")}{photo("graving", "The tunnel goes straight into the drift. AI-generated illustration.")}</div></div>

<div class="wrap narrow body story">
<section class="short"><h2>Four things to do before you lie down</h2><ul>
<li><strong>Bring the shovel inside.</strong> Drifting snow can close the entrance overnight.</li>
<li><strong>Plant your skis upright outside.</strong> They show others where you are.</li>
<li><strong>Light a candle, away from the roof and walls.</strong> If it burns poorly, there is too little oxygen. Let in more air.</li>
<li><strong>Check the air hole.</strong> It must stay open all night.</li>
</ul></section>

<h2>Air is the thing to watch</h2>
<p>A snow cave is airtight. That is why it is warm, and that is why you must ventilate. Store norske leksikon warns that bad air is dangerous when several people sleep close together, because you do not notice the symptoms while asleep. It recommends a routine for waking each other.</p>
<p>If you use a stove in the cave, you need even more air. SINTEF, the Norwegian building research institute, writes that correct ventilation is critical.</p>

<h2>No drift in sight?</h2>
<p>On flat ground you can dig a snow trench: about a metre wide, covered with snow blocks. It takes more work than a cave in a drift, but it gets you out of the wind. The principles are the same: sit higher than the bottom, and make sure you have air.</p>
</div>
<div class="wrap">{photo("natt", "The skis outside show where the cave is. AI-generated illustration.")}</div>

<div class="wrap narrow body story">
<h2>The morning after</h2>
<p>Mountain storms pass. What matters is whether you still have strength and warmth when they do. That is why the shovel goes in the pack on winter trips, together with a wind sack, a sleeping pad and a sleeping bag. The Norwegian Trekking Association and the Red Cross count those four as what you need to get through a night out.</p>
<p>And that is why your first snow cave should be dug on a fine day, with cocoa in the flask and plenty of time. Then your hands know what to do on the day you need it.</p>
<p>In Norway, call 112 if you are in distress and have coverage.</p>

<aside class="next"><h2>Read on</h2><ul>
<li><a href="{{P}}/en/guides/sleeping-bag-ratings/">Sleeping bags: how to read the temperature ratings</a></li>
<li><a href="{{P}}/en/guides/sleeping-pad-r-value/">Sleeping pads and R-value: how warm do you need?</a></li>
<li><a href="{{P}}/en/guides/layering/">Layering: how to dress for the outdoors</a></li>
</ul></aside>

<section class="sources"><h2>Sources</h2><ul>{"".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in SRC)}</ul>
<p class="note">This article gives general advice and does not replace training or experience. Always follow weather and avalanche forecasts. Images and film are AI-generated and do not show a real event.</p></section>
</div>''')

ART = dict(cat=0, slug=dict(no="snohule-i-snostorm", en="snow-cave-in-a-storm"), img="snohule-natt", feature=True, no=NO, en=EN)
