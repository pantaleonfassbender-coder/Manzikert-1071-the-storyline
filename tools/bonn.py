"""Helpers for the Bonn Corpus (CSHB) Attaleiates, 1853.

Two Google scans of the same Oxford printing have independent Greek OCR
(att01 = michaelisattali01bekkgoog, attPres = michaelisattali00presgoog).
page_greek() returns the Greek text lines of a printed page from one OCR;
compare() prints both with the words that differ flagged, for correction
against the page images."""
import re, sys, difflib, unicodedata
from pathlib import Path

SRC = Path(__file__).parent / "src"
GREEK = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")
HEAD = re.compile(r"(HISTORIA|MICHAEL|ATTALIOT)")

def lines(name):
    return (SRC / f"{name}.txt").read_text(encoding="utf-8").splitlines()

def pages(name):
    """Split the OCR at running heads: {page: [lines]}. Versos carry
    "MICHAELIS ATTALIOTAE" (even pages), rectos "HISTORIA" (odd). The OCR
    garbles many numbers and drops some heads, so numbers are counted from an
    anchor page using the parity of each head;
    a dropped head leaves two pages in one block under the earlier number."""
    L = lines(name)
    heads = [i for i, l in enumerate(L) if HEAD.search(l)]
    even = ["MICHAEL" in L[i] or "ATTALIOT" in L[i] for i in heads]
    # anchor: p. 148 begins "στρατόπεδον. ἐφάνη" in both printings
    a = next(k for k, i in enumerate(heads)
             if any(l.strip().startswith("στρατόπεδον. ἐφάνη") or l.strip().startswith("στρατόπεδον, ἐφάνη") for l in L[i + 1:i + 14]))
    cur = {a: 148}
    for k in range(a + 1, len(heads)):
        c = cur[k - 1] + 1
        if (c % 2 == 0) != even[k]: c += 1
        cur[k] = c
    for k in range(a - 1, -1, -1):
        c = cur[k + 1] - 1
        if (c % 2 == 0) != even[k]: c -= 1
        cur[k] = c
    out = {}
    for k, i in enumerate(heads):
        j = heads[k + 1] if k + 1 < len(heads) else len(L)
        out[cur[k]] = L[i + 1:j]
    return out

def greek_part(block):
    """Greek lines of a page, before the apparatus/Latin; drops marginal numbers."""
    g = []
    for l in block:
        s = l.strip()
        if not s: continue
        if re.match(r"^\d+\.\s", s) and len(GREEK.findall(s)) < 40: break  # apparatus
        if len(GREEK.findall(s)) < max(4, len(s) * 0.35):
            if g and re.search(r"[a-z]{4}", s) and not GREEK.search(s): break  # Latin starts
            continue
        s = re.sub(r"^\W{0,3}\d{1,2}\s*", "", s)          # marginal line numbers
        s = re.sub(r"\s+\d{1,2}\s*$", "", s)
        s = re.sub(r"\s*f\.\s*\d+\s*[rv]\.?", "", s)       # codex folio marks
        g.append(s)
    return g

def compare(p):
    a = greek_part(pages("att01").get(p, []))
    P = pages("attPres")
    b = greek_part(P.get(p - 1, [])) + greek_part(P.get(p, [])) + greek_part(P.get(p + 1, []))
    print(f"==== p. {p}  ({len(a)} lines)")
    for x in a:
        best = difflib.get_close_matches(x, b, n=1, cutoff=0.4)
        y = best[0] if best else ""
        wa, wb = x.split(), y.split()
        sm = difflib.SequenceMatcher(None, wa, wb)
        diffs = [f"{' '.join(wa[i1:i2])} | {' '.join(wb[j1:j2])}" for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
        print(x + ("    ⟨" + " ; ".join(diffs) + "⟩" if diffs else ""))

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for p in range(int(sys.argv[1]), int(sys.argv[2]) + 1): compare(p)
