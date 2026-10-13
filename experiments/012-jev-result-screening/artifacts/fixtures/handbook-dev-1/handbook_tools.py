
"""Handbook tools (identical in every condition).

search(query, k=5): print up to k (at most 8) ranked passages as a structured result, and save
  the original under /task/workspace/search-results/ (path printed in the result header).
show(ids): print the named passages in full (never screened).
"""
import json, math, os, re

FIXTURES = os.environ.get("HANDBOOK_FIXTURES", "/task/fixtures/handbook")
SAVE_DIR = os.environ.get("HANDBOOK_SAVE_DIR", "/task/workspace/search-results")
MAX_K = 8
_WORD = re.compile(r"[a-z0-9]+")
_STOP = set("a an and are as at be by for from has have in is it its of on or the this to was were with what which who how does do".split())


def _tok(text):
    return [w for w in _WORD.findall(text.lower()) if w not in _STOP]


def load_passages(root=None):
    out = []
    root = root or FIXTURES
    for name in sorted(os.listdir(root)):
        if not name.endswith(".md"):
            continue
        lines = open(os.path.join(root, name), encoding="utf-8").read().splitlines()
        doc = name[:-3]
        title = lines[0].split(" · ", 1)[1] if " · " in lines[0] else lines[0]
        meta = lines[1]
        sec = None
        for line in lines[2:]:
            m = re.match(r"^§(\d+) (.*)$", line)
            if m:
                sec = {"id": f"{doc} §{m.group(1)}", "doc": doc, "title": title, "heading": m.group(2), "meta": meta, "text": ""}
                out.append(sec)
            elif sec is not None and line.strip():
                sec["text"] = (sec["text"] + " " + line.strip()).strip()
    return out


def header(p):
    return f"=== {p['id']} | {p['title']} — {p['heading']} | {p['meta']}"


def rank(passages, query, k):
    docs = [_tok(p["title"] + " " + p["heading"] + " " + p["text"]) for p in passages]
    n = len(docs)
    avg = sum(len(d) for d in docs) / max(1, n)
    df = {}
    for d in docs:
        for w in set(d):
            df[w] = df.get(w, 0) + 1
    q = _tok(query)
    scored = []
    for i, d in enumerate(docs):
        s = 0.0
        for w in q:
            tf = d.count(w)
            if tf:
                idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * len(d) / avg))
        if s > 0:
            scored.append((-s, passages[i]["id"], i))
    scored.sort()
    return [passages[i] for _, _, i in scored[: max(1, min(int(k), MAX_K))]]


def _next_id():
    os.makedirs(SAVE_DIR, exist_ok=True)
    n = 1 + sum(1 for f in os.listdir(SAVE_DIR) if f.endswith(".json"))
    return f"SR-{n:03d}"


def search(query, k=5):
    hits = rank(load_passages(), str(query), k)
    rid = _next_id()
    path = os.path.join(SAVE_DIR, rid + ".txt")
    q = str(query).replace('"', "'")[:200]
    json.dump({"id": rid, "query": q, "k": int(k), "passages": hits}, open(os.path.join(SAVE_DIR, rid + ".json"), "w"))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# saved search result {rid}: query \"{q}\", k={int(k)}, {len(hits)} passages (original, unscreened)\n")
        for p in hits:
            fh.write("--- " + header(p)[4:] + "\n" + p["text"] + "\n")
    print(f'<<search-result {rid} query="{q}" k={int(k)} returned={len(hits)} saved={path}>>')
    for p in hits:
        print(header(p))
        print(p["text"])
    print(f"<<end search-result {rid}>>")


def show(ids):
    want = [ids] if isinstance(ids, str) else list(ids)
    by_id = {p["id"]: p for p in load_passages()}
    norm = {re.sub(r"\s+", " ", i.replace("#", " §").replace("§ ", "§")).strip(): i for i in want}
    print("<<passages (unscreened): " + ", ".join(norm) + ">>")
    for i in norm:
        p = by_id.get(i)
        print("--- " + header(p)[4:] if p else f"--- {i}: no such passage")
        if p:
            print(p["text"])
    print("<<end passages>>")
