/* Manzikert 1071 — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { byzantium: "Byzantium", seljuk: "The Seljuks", armenian: "Armenia", syriac: "Syriac", reception: "Reception" };
const LANGS = { grc: "Greek", ar: "Arabic", fr: "French", la: "Latin" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("manzikert_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  const pl = plateOf("fr236");
  view.innerHTML = `
  <div class="hero">
    <div>
      <span class="tag">1068–1072 · Romanos IV Diogenes · Alp Arslan · the Doukai</span>
      <h1>A battle lost, and an empire lost at home</h1>
      <p class="lede">On 26 August 1071, near the fortress of Manzikert north of Lake Van, the army of the Byzantine emperor Romanos IV Diogenes broke in the evening, and the emperor was taken fighting on foot.
      Eight days later the sultan Alp Arslan let him go with a treaty. It was the capital, not the sultan, that finished him: the Doukas family, whose sons he had been made to share the throne with, refused him, fought him, and blinded him in the summer of 1072.</p>
      <p class="readable">This apparatus follows the battle and the civil war through the documents of those who fought, lost, negotiated and remembered them.
      Every text is public domain and carried in whole sections, with the original beside the English, a timeline that links into the texts, and plates from the manuscripts that made the scene a legend.
      It begins with the only eyewitness account from either side.</p>
      <p class="quote">"What is more pitiable than … the whole Roman state seen overturned, and an empire perceived to have collapsed in an instant?"
      <br><span class="fine">Michael Attaleiates, who was there ·
      <a href="#/text/attaleiates/battle/14">Att. Battle [14]</a></span></p>
    </div>
    <figure><img src="assets/plates/${pl.id}.jpg" alt="${esc(pl.titel)}">
      <figcaption>${esc(pl.caption)} <a href="#/plates">All plates →</a></figcaption></figure>
  </div>

  <h2>What the apparatus carries</h2>
  <div class="grid g2">${D.mods.shipped.map(card).join("")}</div>

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>Was the battle the catastrophe?</h3>
      <p>The eyewitness says the empire collapsed in an instant, and then that the harder story is what came after: "from here on, who could tell the host of hardships that followed?" <a href="#/text/attaleiates/captivity/8">Att. Capt. [8]</a> The emperor came home with a treaty; the civil war left the frontier without anyone to hold it, and ended with the historian turning to address the emperor who ordered the blinding: "What do you say, emperor?" (<a href="#/text/attaleiates/blinding/3">Att. Blind. [3]</a>)</p></div>
    <div class="panel"><h3>Who broke the army?</h3>
      <p>Half of it never reached the battle; its commander, hearing of the sultan, marched away (<a href="#/text/attaleiates/battle/7">Att. Battle [7]</a>). The rear broke at a rumour that "most people" laid at the door of a Doukas (<a href="#/text/attaleiates/battle/12">Att. Battle [12]</a>). Attaleiates, writing for the Doukai's enemy, names no one.</p></div>
    <div class="panel"><h3>Who tells it?</h3>
      <p>A Byzantine judge in the emperor's tent; a historian of the Seljuk sultans' heirs in Mosul, for whom the battle was a Friday victory given by God (<a href="#/text/ibnalathir/battle/5">IA Battle [5]</a>); and an Armenian monk of Edessa, for whom the emperor who sacked Sebasteia was cursed before he set out (<a href="#/text/matthew/battle/2">Matt. Battle [2]</a>). The palace that deposed Romanos speaks through his stepson's tutor, who advised against receiving him back (<a href="#/text/psellos/coup/1">Psell. Coup [1]</a>). The family that did it answers through the grandson of one of its generals, writing for Andronikos Doukas' daughter (<a href="#/text/bryennios/civil/3">Bry. Civil [3]</a>). A Syriac patriarch of the 1190s sees the Armenians, persecuted by the Greeks, flee first (<a href="#/text/michaelsyr/battle/1">Mich. Battle [1]</a>). <a href="#/compare">Compare</a> sets them side by side. The legend of the emperor as footstool belongs to fifteenth-century France (<a href="#/plates">Plates</a>), and Gibbon in 1788 made the whole a set piece of the European canon (<a href="#/text/gibbon/battle/4">Gibbon Battle [4]</a>). The most important Muslim account, preserved by Sibṭ ibn al-Jawzī, is <a href="#/texts">not carried</a>: its only edition is not public domain.</p></div>
    <div class="panel"><h3>Can the story be played?</h3>
      <p>The companion game <a href="https://manzikert-1071-the-game.netlify.app/" target="_blank" rel="noopener"><em>The Turned Standard</em></a> is built on these texts: as Romanos you hold a mercenary army and a hostile court together, march on Manzikert card by card after Attaleiates, and its accounting separates what the field decided from what the City decided. A second role, <a href="https://manzikert-1071-the-game.netlify.app/sultan.html" target="_blank" rel="noopener">the sultan</a>, plays Alp Arslan's war for Baghdad, the battle from the other side and what the victory won. Every card links back to its passage here. The game is also on <a href="https://leofassb.itch.io/the-turned-standard" target="_blank" rel="noopener">itch.io</a>, with a <a href="https://leofassb.itch.io/the-turned-standard/devlog" target="_blank" rel="noopener">devlog</a> on how it was tested.</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">Seven modules, each readable in full. What is not carried, and why, is listed below: one gap by necessity, two by choice.</p>
    <h2>Carried</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>
    <h2 id="missing">Not carried</h2><div class="grid g2">${(D.mods.missing || []).map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">not carried</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const origName = LANGS[t.orig_sprache] || "Original";
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + English`], ["orig", origName], ["en", "English"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(t.orig_sprache)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("manzikert_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Compare</span><h1>Two sides of one moment</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← All comparisons</a></p><p class="fine">Loading…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(t.autor)}</b><br><span class="fine">${esc(t.jahr)} · ${esc(sec.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← All comparisons</a></p>
    <span class="tag">Compare</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>1049–today</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>The emperor, the seal, and the legend</h1>
    <p class="lede">No picture of the battle was made by anyone who saw it. What survives from the time is a seal; what the later Middle Ages made of the scene is Fortune's wheel.</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing that is out of copyright, and its source is named on its page. Modern editions and translations in copyright (among them the recent English translations of Attaleiates, Psellos and Ibn al-Athīr) are not used.</p>
    <p><b>OCR repaired against the page.</b> The Greek comes from the Bonn Corpus: two independent machine readings of the same printing are compared word by word, and every place where they disagree, or where both fail, is read from the page image. The Arabic of Tornberg's edition is transcribed by eye from the page, with the machine reading as a first draft. Dulaurier's French is corrected against the page where the machine failed. The build scripts record how.</p>
    <p><b>Spelling as printed.</b> The editor's text is kept, with his accents and punctuation; the printer's curly theta is set as θ. Misprints corrected are named in the notes, and the editor's own doubts are given where they matter.</p>
    <p><b>Working translations.</b> Where no public-domain English exists, which for this battle is almost everywhere, the site gives its own working translation, close to the original and dedicated to the public domain (CC0). It is an aid to reading, not a critical translation.</p>
    <p><b>Voices and distances.</b> Attaleiates was with the army and wrote within a decade, for an emperor who had overthrown the Doukai; he names no traitor. Ibn al-Athīr wrote in Mosul in the 1220s from earlier chronicles, in praise of the sultans as champions of the caliph. Psellos wrote for the emperor who had Romanos deposed, and Bryennios for the daughter of the man who took him at Adana. Matthew of Edessa wrote in the 1120s–1130s as an Armenian who blamed the Romans for Armenia's ruin. Each is carried in its own language beside the English: Greek and Arabic from nineteenth-century editions read against the page, Matthew in Dulaurier's French of 1858 (the Armenian is not yet carried). Psellos, the tutor of Michael VII, gives the palace's version and his own part in it. Bryennios, writing two generations later for Andronikos Doukas' daughter, gives the family's version.</p>
    <p><b>Two late voices.</b> Michael the Syrian, patriarch of the Syriac Orthodox church, wrote in the 1190s, a century and more after the battle, as the head of a church the Greeks had persecuted, under Turkish and Crusader lords; he is carried in Chabot's French of 1905 (the Syriac is not). Gibbon wrote in 1788 without Attaleiates, Ibn al-Athīr or Michael, none of which was printed; his English is carried as first printed, and the notes show where each of his sentences comes from.</p>
    <p><b>What is missing.</b> The most important Muslim account is not here. Sibṭ ibn al-Jawzī (d. 1256) preserves the report of Ghars al-Niʿma, a Baghdad contemporary of the battle; its only edition (Sevim, Ankara 1968) is not public domain, and no older printing exists. The same holds for al-Ḥusaynī's Seljuk court chronicle. The Seljuk side is therefore told here by Ibn al-Athīr, who wrote in the 1220s from earlier chronicles, and otherwise by the sultan's enemies. The Armenian of Matthew and the Syriac of Michael are not transcribed. Skylitzes Continuatus, Zonaras and Aristakes are left out by choice. The <a href="#/texts">Texts</a> page lists each gap with its source.</p>
    <p><b>Dates.</b> The text is followed; the timeline gives the dates of modern accounts for what the text does not date, and says so.</p>
    </div>
    <h2>Sources carried</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>
    <h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });
