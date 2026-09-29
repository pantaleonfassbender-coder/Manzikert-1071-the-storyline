"""Build data/ibnalathir.json: Ibn al-Athir on the year 463 (1070-71).

Source: Ibn-el-Athiri Chronicon quod perfectissimum inscribitur, ed. C. J.
Tornberg, vol. X (Leiden: Brill, 1864), pp. 42-46. Internet Archive
kamil-Tornberg (vol. 10; jp2 leaves 46-50 = pp. 42-46). Public domain.
Transcribed by eye from the page images; conventions in tools/ibnalathir_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ibnalathir_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "ibnalathir.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "orig": u["orig"], "en": u["en"]}
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Ibn al-Athīr: the year 463",
        "autor": "ʿIzz al-Dīn Ibn al-Athīr (1160–1233), historian of Mosul; al-Kāmil fī l-taʾrīkh ('The Complete History'), written in the 1220s from earlier chronicles now partly lost",
        "jahr": "463 AH (1070–71), written c. 1230",
        "orig_sprache": "ar",
        "rtl": True,
        "pg_label": "Tornberg",
        "quelle": "Ibn-el-Athiri Chronicon quod perfectissimum inscribitur, ed. Carl Johan Tornberg, vol. X (Leiden: Brill, 1864), pp. 42–46, year 463. Internet Archive, kamil-Tornberg (vol. 10, jp2 leaves 46–50). Public domain.",
        "hinweis": "The Arabic is Tornberg's text, transcribed by eye from the page images, with the OCR as a first draft. Spelling as printed: Tornberg writes final ى for ي, omits most hamzas (القايم, ماية) and writes بغداذ; his occasional vowel signs and his footnote marks are not carried, and his manuscript variants are given in the notes where they touch the sense. The units and the line breaks inside them are the site's; each unit shows Tornberg's page. The English is this site's working translation, close to the Arabic and dedicated to the public domain (CC0). Ibn al-Athīr wrote a century and a half after the battle, at a court that looked back to the Seljuk sultans as champions of the Abbasid caliphate; the pious frame of the victory is his.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
