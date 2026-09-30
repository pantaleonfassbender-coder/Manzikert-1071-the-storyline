"""Build data/bryennios.json: Nikephoros Bryennios, Book I, chapters 12-25.

Source: Nicephori Bryennii Commentarii, ed. Meineke (Bonn 1836), pp. 35-55.
Internet Archive ioanniscinnamie00meingoog / 01meingoog. Public domain.
Conventions in tools/bryennios_text.py; OCR comparison in tools/bryen.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bryennios_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "bryennios.json"


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
        "titel": "Bryennios: the family's version",
        "autor": "Nikephoros Bryennios the Younger (c. 1080–1137), Caesar, husband of Anna Komnene and grandson of the general of 1071; Hyle Historias ('Materials for History'), written in the 1120s–1130s for the empress Eirene Doukaina, daughter of Andronikos Doukas",
        "jahr": "1071–1072, written c. 1130",
        "orig_sprache": "grc",
        "pg_label": "Bonn",
        "quelle": "Nicephori Bryennii Commentarii, ed. August Meineke, Corpus Scriptorum Historiae Byzantinae (Bonn: Weber, 1836), Book I, chapters 12–25, pp. 35–55, bound with Kinnamos. Internet Archive, Google scan ioanniscinnamie00meingoog (printed page n = page image n+462), checked against a second scan (ioanniscinnamie01meingoog). Public domain.",
        "hinweis": "The Greek is Meineke's text, set from two independent OCRs and read against the page images line by line; the printer's curly theta is set as θ and hyphenations are joined. The lacuna Possinus marked at the start of chapter 20 is kept as asterisks. Meineke's apparatus is not carried, except in notes. The units are his chapters or parts of them; each shows its Bonn page and line range. The English is this site's working translation (CC0); Possinus' facing Latin was consulted. Bryennios copies Psellos in whole sentences and adds the family's details: his grandfather's counsel and wounds, Andronikos Doukas' virtues and his protest against the blinding, the trial of Anna Dalassene.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
