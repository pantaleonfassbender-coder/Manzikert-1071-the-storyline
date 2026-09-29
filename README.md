# Manzikert 1071: the storyline

A documentary apparatus for the battle of Manzikert (26 August 1071) and the Byzantine civil war that followed it, 1068–1072: public-domain sources with the original beside the English, a timeline linked into the texts, and plates from the manuscripts that turned the scene into a legend.

Its thesis is the eyewitness's own: the battle was lost in an evening, but the empire's eastern frontier was lost in the civil war that followed, when the Doukas family refused, fought and blinded the emperor the sultan had released.

Stage 1 (September 2026) carries one module:

- **Attaleiates: the campaign of 1071** — Michael Attaleiates, a judge who rode with the army, *Historia*, ed. Bekker (Bonn 1853), pp. 148–168: the march from Theodosiopolis, the divided army, the retaking of Manzikert, the battle, the captivity and release. Greek, set from two independent OCRs and read against the page images line by line, with a working English translation.

Planned modules and their sources (Ibn al-Athīr, Matthew of Edessa, Psellos, Bryennios, Aristakes, Michael the Syrian, Gibbon, and the rest of Attaleiates) are listed on the Texts page (`data/modules.json`).

## Building the data

```
python tools/build-attaleiates.py
```

The Greek text is kept in `tools/attaleiates_text.py`. `tools/bonn.py 148 168` prints the two OCRs of the Bonn Attaleiates side by side with their differences; it expects the OCR files in `tools/src/` (Internet Archive `michaelisattali01bekkgoog_djvu.txt` saved as `att01.txt`, and `michaelisattali00presgoog_djvu.txt` as `attPres.txt`).

## Running locally

Any static server, e.g. `python -m http.server 8135`.

Licences: see `LICENSES.md`.
