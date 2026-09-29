"""Build data/attaleiates.json: Michael Attaleiates on the campaign of 1071.

Source: Michaelis Attaliotae Historia, ed. Immanuel Bekker, Corpus Scriptorum
Historiae Byzantinae (Bonn: Weber, 1853), pp. 148-168. Internet Archive
michaelisattali01bekkgoog (Oxford copy, digitised by Google): printed page
n = leaf n+20. Public domain.

The Greek was set from the OCR of two scans of the Oxford printing (the second
is michaelisattali00presgoog) and read against the page images line by line;
tools/bonn.py prints the two OCRs side by side with their differences, and
the words that neither OCR read correctly were taken from the images. Page 167
is missing from both OCRs and was transcribed from the image. Conventions are
in tools/attaleiates_text.py. The English is this site's working translation
(CC0); Bekker's facing Latin translation was consulted.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from attaleiates_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "attaleiates.json"


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
        "titel": "Attaleiates: the campaign of 1071",
        "autor": "Michael Attaleiates (c. 1022–c. 1080), judge and member of the senate, who rode with the army in 1071; Historia, written c. 1079–80 for Nikephoros III Botaneiates",
        "jahr": "1071, written c. 1080",
        "orig_sprache": "grc",
        "pg_label": "Bonn",
        "quelle": "Michaelis Attaliotae Historia, ed. Immanuel Bekker, Corpus Scriptorum Historiae Byzantinae (Bonn: Weber, 1853), pp. 148–168, Greek with Bekker's Latin translation. Internet Archive, Oxford copy digitised by Google (michaelisattali01bekkgoog; printed page n = leaf n+20), checked against a second scan (michaelisattali00presgoog). Public domain.",
        "hinweis": "The Greek is Bekker's text, set from two independent OCRs and corrected line by line against the page images; the printer's curly theta is set as θ, line-end hyphenations are joined, and the few misprints corrected are named in the notes. Bekker's apparatus is not carried, except where a note gives it. Each unit is cited by section and number, e.g. Att. Battle [13]; its Bonn page and line range is shown beside it. The English is this site's working translation, close to the Greek and dedicated to the public domain (CC0); it is an aid to reading, not a critical translation. Attaleiates wrote for Nikephoros III, who rose against the Doukai; his sympathy for Romanos and his silence about names are part of the evidence.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
