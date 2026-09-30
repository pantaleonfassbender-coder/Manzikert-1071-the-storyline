"""OCR helpers for the Bonn Bryennios (ed. Meineke, 1836, bound after
Kinnamos). Two Google scans of the same printing: bry00 =
ioanniscinnamie00meingoog, bry01 = ioanniscinnamie01meingoog. Running heads:
'NICEPHORI BRYENNII' on even pages, 'COMMENTARIORUM L.' on odd pages.
Page images: ioanniscinnamie00meingoog BookReader n = page + 462.
Usage: python tools/bryen.py 35 55"""
import re, sys, difflib
from pathlib import Path

SRC = Path(__file__).parent / "src" / "bryennios"
GREEK = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")

def lines(name):
    return (SRC / f"{name}.txt").read_text(encoding="utf-8").splitlines()

def pages(name):
    L = lines(name)
    heads = [i for i, l in enumerate(L) if re.search(r"NICEPHORI BRYENN|COMMENTARIORUM", l)]
    even = ["NICEPHORI" in L[i] for i in heads]
    # anchor: the page that begins with the Cappadocian council's continuation
    a = next(k for k, i in enumerate(heads) if any("σουλτάνῳ εἰσιόντι" in l for l in L[i + 1:i + 6]))
    cur = {a: 36}
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
        out.setdefault(cur[k], L[i + 1:j])
    return out

def greek_part(block):
    g = []
    for l in block:
        s = l.strip()
        if not s: continue
        if re.match(r"^\d+\.\s", s) and not g == []: break
        if len(GREEK.findall(s)) < max(4, len(s) * 0.35):
            if g and re.search(r"[a-z]{4}", s) and not GREEK.search(s): break
            continue
        s = re.sub(r"^\W{0,3}\d{1,2}\s*", "", s)
        s = re.sub(r"\s+(\d{1,2}|[A-D]|[VP] ?\d+)\s*$", "", s)
        g.append(s)
    return g

def compare(p):
    a = greek_part(pages("bry00").get(p, []))
    P = pages("bry01")
    b = greek_part(P.get(p - 1, [])) + greek_part(P.get(p, [])) + greek_part(P.get(p + 1, []))
    print(f"==== p. {p}  ({len(a)} lines)")
    for x in a:
        best = difflib.get_close_matches(x, b, n=1, cutoff=0.4)
        y = best[0] if best else ""
        wa, wb = x.split(), y.split()
        sm = difflib.SequenceMatcher(None, wa, wb)
        diffs = [f"{' '.join(wa[i1:i2])} | {' '.join(wb[j1:j2])}" for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
        print(x + ("    <" + " ; ".join(diffs) + ">" if diffs else ""))

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for p in range(int(sys.argv[1]), int(sys.argv[2]) + 1): compare(p)
