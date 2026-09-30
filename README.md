# Manzikert 1071: the storyline

A documentary apparatus for the battle of Manzikert (26 August 1071) and the Byzantine civil war that followed it, 1068–1072: public-domain sources with the original beside the English, a timeline linked into the texts, and plates from the manuscripts that turned the scene into a legend.

Its thesis is the eyewitness's own: the battle was lost in an evening, but the empire's eastern frontier was lost in the civil war that followed, when the Doukas family refused, fought and blinded the emperor the sultan had released.

Stage 1 (September 2026) carries four modules:

- **Attaleiates: the campaign and the civil war** — Michael Attaleiates, a judge who rode with the army, *Historia*, ed. Bekker (Bonn 1853), pp. 148–180: the march from Theodosiopolis, the divided army, the retaking of Manzikert, the battle, the captivity and release; then the coup in Constantinople, the civil war, the terms at Adana, the blinding and Romanos' death on Prote. Greek, set from two independent OCRs and read against the page images line by line, with a working English translation.

- **Psellos: the palace's version** — *Chronographia*, ed. Sathas (London 1899), pp. 245–259: Eudokia's marriage, Romanos' reign and campaigns, the battle and the news, the coup in the palace in which Psellos advised against receiving Romanos back, the civil war and the blinding. Greek read against the page images, with a working translation.
- **Ibn al-Athīr: the year 463** — *al-Kāmil fī l-taʾrīkh*, ed. Tornberg, vol. X (Leiden 1864), pp. 42–46: Aleppo and the sultan's war for the caliph, then the king of the Rūm at Malazkird, the capture, the ransom and the fifty years' truce. Arabic, transcribed by eye from the page images, with a working translation.
- **Matthew of Edessa: the Armenian chronicle** — chapters XCVII–CIV (1067–1072) in Dulaurier's French (Paris 1858), pp. 159–172, corrected against the page images, with a working English translation: the empress and Romanos, the sultan in Armenia, the sack of Sebasteia, the battle, the blinding, the death of Alp Arslan.

A **Compare** page sets the four voices side by side on seven moments (the meeting of sultan and captive, the peace refused, the divided army, the treason, the treaty and the coup, whether to receive him back, the blinding).

Planned modules and their sources (Bryennios, Skylitzes Continuatus and Zonaras, Aristakes, Michael the Syrian, Gibbon) are listed on the Texts page (`data/modules.json`).

## Building the data

```
python tools/build-attaleiates.py
python tools/build-ibnalathir.py
python tools/build-matthew.py
python tools/build-psellos.py
```

The texts are kept in `tools/attaleiates_text.py`, `tools/ibnalathir_text.py`, `tools/matthew_text.py` and `tools/psellos_text.py`. `tools/bonn.py 148 168` prints the two OCRs of the Bonn Attaleiates side by side with their differences; it expects the OCR files in `tools/src/` (Internet Archive `michaelisattali01bekkgoog_djvu.txt` saved as `att01.txt`, and `michaelisattali00presgoog_djvu.txt` as `attPres.txt`).

## Running locally

Any static server, e.g. `python -m http.server 8135`.

Licences: see `LICENSES.md`.
