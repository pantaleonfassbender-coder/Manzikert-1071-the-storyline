"""Build data/gibbon.json: Gibbon, Decline and Fall, ch. LVII (1788).

Source: The History of the Decline and Fall of the Roman Empire, vol. V
(London: Strahan and Cadell, 1788), pp. 660-668. Public domain.
Conventions in tools/gibbon_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gibbon_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "gibbon.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "en": u["en"]}
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Gibbon, chapter 57 (1788)",
        "autor": "Edward Gibbon (1737–1794), The History of the Decline and Fall of the Roman Empire, chapter LVII, in the first edition of its last volumes (1788)",
        "jahr": "1788",
        "orig_sprache": "en",
        "pg_label": "1788 vol. V p.",
        "quelle": "Edward Gibbon, The History of the Decline and Fall of the Roman Empire, vol. V (London: A. Strahan and T. Cadell, 1788), chapter LVII, pp. 660–668. Internet Archive, bim_eighteenth-century_the-history-of-the-decli_gibbon-edward_1788_5_0 (printed page n = leaf n+13). Public domain.",
        "hinweis": "Gibbon's own English, as printed in 1788: set from the Project Gutenberg etext and corrected word by word against the first edition's page images, whose spelling (valour, recal, scymetar, negociation) is kept and whose readings are followed where the etext departs from them ('Romanus led his army', not 'Romulus'; 'wasted', not 'spent'; and in note 37 Bryennios' Greek, which the etext turns into its opposite). The long s is printed as s. Gibbon's footnotes on the passage are given in each unit's notes. He wrote without Attaleiates, Ibn al-Athīr or Michael the Syrian, from Skylitzes, Zonaras and Bryennios on one side and the Latin and French versions of Elmacin, Bar Hebraeus and d'Herbelot on the other; the notes trace his sentences back to the texts this site carries. No translation is needed or given.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
