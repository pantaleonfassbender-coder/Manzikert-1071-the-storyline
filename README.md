# Manzikert 1071: the storyline

A documentary apparatus for the battle of Manzikert (26 August 1071) and the Byzantine civil war that followed it, 1068–1072: public-domain sources with the original beside the English, a timeline linked into the texts, and plates from the manuscripts that turned the scene into a legend.

Its thesis is the eyewitness's own: the battle was lost in an evening, but the empire's eastern frontier was lost in the civil war that followed, when the Doukas family refused, fought and blinded the emperor the sultan had released.

**Stage 1 is closed (September 2026).** It carries seven modules:

- **Attaleiates: the campaign and the civil war** — Michael Attaleiates, a judge who rode with the army, *Historia*, ed. Bekker (Bonn 1853), pp. 148–180: the march from Theodosiopolis, the divided army, the retaking of Manzikert, the battle, the captivity and release; then the coup in Constantinople, the civil war, the terms at Adana, the blinding and Romanos' death on Prote. Greek, set from two independent OCRs and read against the page images line by line, with a working English translation.

- **Psellos: the palace's version** — *Chronographia*, ed. Sathas (London 1899), pp. 245–259: Eudokia's marriage, Romanos' reign and campaigns, the battle and the news, the coup in the palace in which Psellos advised against receiving Romanos back, the civil war and the blinding. Greek read against the page images, with a working translation.
- **Bryennios: the family's version** — *Hyle Historias*, ed. Meineke (Bonn 1836), Book I chapters 12–25, pp. 35–55: the campaign, the order of battle and the rearguard that 'withdrew', the coup, the trial of Anna Dalassene, the civil war and Andronikos' protest against the blinding. Greek from two OCRs read against the page images, with a working translation.
- **Michael the Syrian: the view from the Syriac church** — *Chronique*, tr. J.-B. Chabot, tome III (Paris 1905), Book XV chapters 3–4, pp. 168–172: Romanos, the two vows, the Armenians who fled first, the sultan's nephew and the stolen capture, the blinding, Suleiman and Atsiz after 1071. Chabot's French read against the page images, with a working translation.
- **Gibbon, chapter 57 (1788)** — *Decline and Fall*, vol. V (London 1788), pp. 660–668: the passage on Romanos and Alp Arslan in Gibbon's English as first printed, corrected against the page images where the Gutenberg etext departs from it, with his footnotes and notes tracing his sentences to the sources carried here.
- **Ibn al-Athīr: the year 463** — *al-Kāmil fī l-taʾrīkh*, ed. Tornberg, vol. X (Leiden 1864), pp. 42–46: Aleppo and the sultan's war for the caliph, then the king of the Rūm at Malazkird, the capture, the ransom and the fifty years' truce. Arabic, transcribed by eye from the page images, with a working translation.
- **Matthew of Edessa: the Armenian chronicle** — chapters XCVII–CIV (1067–1072) in Dulaurier's French (Paris 1858), pp. 159–172, corrected against the page images, with a working English translation: the empress and Romanos, the sultan in Armenia, the sack of Sebasteia, the battle, the blinding, the death of Alp Arslan.

A **Compare** page sets the seven voices side by side on seven moments (the meeting of sultan and captive, the peace refused, the divided army, the treason, the treaty and the coup, whether to receive him back, the blinding).

What is **not carried**, and why, is listed on the Texts page (`data/modules.json`, key `missing`): above all Sibṭ ibn al-Jawzī, who preserves the most important Muslim account, and whose only edition (Sevim, Ankara 1968) is not public domain; al-Ḥusaynī; the Armenian and Syriac originals; and, by choice, Skylitzes Continuatus, Zonaras and Aristakes.

## Building the data

```
python tools/build-attaleiates.py
python tools/build-ibnalathir.py
python tools/build-matthew.py
python tools/build-psellos.py
python tools/build-bryennios.py
python tools/build-michaelsyr.py
python tools/build-gibbon.py
```

The texts are kept in `tools/attaleiates_text.py`, `tools/ibnalathir_text.py`, `tools/matthew_text.py` `tools/psellos_text.py`, `tools/bryennios_text.py`, `tools/michael_text.py` and `tools/gibbon_text.py`. `tools/bonn.py 148 168` prints the two OCRs of the Bonn Attaleiates side by side with their differences; it expects the OCR files in `tools/src/` (Internet Archive `michaelisattali01bekkgoog_djvu.txt` saved as `att01.txt`, and `michaelisattali00presgoog_djvu.txt` as `attPres.txt`).

## Running locally

Any static server, e.g. `python -m http.server 8135`.

Licences: see `LICENSES.md`.
