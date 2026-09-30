"""Build data/psellos.json: Michael Psellos on Eudokia and Romanos IV.

Source: The History of Psellus, ed. C. Sathas (London 1899), pp. 245-259.
Internet Archive historyofpsellus00pseluoft. Public domain. Conventions in
tools/psellos_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from psellos_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "psellos.json"


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
        "titel": "Psellos: the palace's version",
        "autor": "Michael Psellos (1018–c. 1078), philosopher, courtier and tutor of Michael VII; the Chronographia, its last part written under Michael VII (1071–1078)",
        "jahr": "1067–1072, written after 1071",
        "orig_sprache": "grc",
        "pg_label": "Sathas",
        "quelle": "The History of Psellus, ed. Constantine Sathas (London: Methuen, 1899), pp. 245–259 (the sections on Eudokia, Romanos IV and the beginning of Michael VII), from the Paris manuscript. Internet Archive, University of Toronto copy (historyofpsellus00pseluoft; printed page n = page image n+15). Public domain.",
        "hinweis": "The Greek is Sathas' text. The machine reading sets the accents and breathings on lines of their own, so the text was built from its base letters and read against the page images line by line; his chapter numbers are kept, and his supplements appear in angle brackets as printed. His footnotes (the manuscript's readings he corrected) are not carried, except in notes. The units are his chapters; each shows its Sathas page and line range. The English is this site's working translation (CC0). Psellos was the tutor of Michael VII and writes as a member of his party ('our general', 'us'); he admits advising that Romanos should not be received back, and swears that Michael did not know of the blinding. His famous letter to the blinded Romanos is in his correspondence, not in this history.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
