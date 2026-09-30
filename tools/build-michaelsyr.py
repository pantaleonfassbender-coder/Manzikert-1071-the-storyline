"""Build data/michaelsyr.json: Michael the Syrian, Chronicle XV.3-4.

Source: Chronique de Michel le Syrien, tr. J.-B. Chabot, t. III (Paris 1905),
pp. 168-172. Internet Archive MichelLeSyrien3. Public domain.
Conventions in tools/michael_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from michael_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "michaelsyr.json"


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
        "titel": "Michael the Syrian: the view from the Syriac church",
        "autor": "Michael the Syrian (Michael I Rabo, 1126–1199), Syriac Orthodox (Jacobite) patriarch of Antioch from 1166; his Chronicle, finished in the 1190s, in the French translation of J.-B. Chabot (1905)",
        "jahr": "1068–c. 1080, written c. 1195",
        "orig_sprache": "fr",
        "pg_label": "Chabot p.",
        "quelle": "Chronique de Michel le Syrien, patriarche jacobite d'Antioche (1166–1199), ed. and tr. J.-B. Chabot, tome III (Paris: Leroux, 1905), Book XV, chapters 3–4, pp. 168–172. Internet Archive, MichelLeSyrien3 (printed page n = leaf n+8). Public domain.",
        "hinweis": "The French is Chabot's translation of the Syriac, from the OCR read against every page image; his spelling of names, his square-bracketed supplements and his bracketed references to the Syriac text ([578]–[580]) are kept, his footnote marks dropped. The Syriac (Chabot's volume IV) is not carried. The English is this site's working translation from Chabot's French (CC0). Michael's chronicle runs in parallel columns (the empire, the Turks, the church); the module carries the column of the empire and one aside from the column of the Turks. He wrote more than a century after the battle, as head of a church the Greeks had persecuted and living under Turkish and Crusader lords: his dates are often late and his Suleiman anachronistic, but he preserves a Syrian judgement of 1071 found nowhere else.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
