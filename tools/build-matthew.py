"""Build data/matthew.json: Matthew of Edessa on 1067-1072.

Source: Chronique de Matthieu d'Edesse (962-1136), tr. Edouard Dulaurier
(Paris: Durand, 1858), pp. 159-172 (chapters XCVII-CIV). Internet Archive
chroniquedematt00mattgoog. Public domain. OCR corrected against the page
images; conventions in tools/matthew_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from matthew_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "matthew.json"


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
        "titel": "Matthew of Edessa: the Armenian chronicle",
        "autor": "Matthew of Edessa (d. after 1136), Armenian monk of Edessa; his Chronicle, written in the 1120s–1130s, in the French translation of Édouard Dulaurier (1858)",
        "jahr": "Armenian era 516–521 (1067–1072), written c. 1130",
        "orig_sprache": "fr",
        "pg_label": "Dulaurier p.",
        "quelle": "Chronique de Matthieu d'Édesse (962–1136) avec la continuation de Grégoire le Prêtre jusqu'en 1162, tr. Édouard Dulaurier (Paris: Durand, 1858), pp. 159–172, chapters XCVII–CIV (XCIX left out). Internet Archive, chroniquedematt00mattgoog. Public domain.",
        "hinweis": "The French is Dulaurier's translation of the Armenian, from the OCR corrected against the page images; his spelling of names and his bracketed date conversions are kept, his footnote marks dropped. The Armenian original is not carried. The English is this site's working translation from Dulaurier's French (CC0). Matthew wrote in Crusader Edessa two generations after the battle, as an Armenian who had seen Byzantine rule and Turkish conquest; his hostility to the Romans' treatment of the Armenians, and his anti-Jewish figure for the blinding, are part of the evidence and are carried as printed.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
