"""dev-cache1: the predeclared per-call caching analysis of the two guarded-clm sessions (read-only, offline).

    python3 dev-cache1-analysis.py EXPORT_A EXPORT_B [--json OUT.json] [--markdown OUT.md]

EXPORT_A and EXPORT_B are the launcher exports of dev-cache1-a and dev-cache1-b (each holds sessions/<run_id>/). Only
the exported records are read: every attempt's recorded request (what was sent, after guarded-clm rebuilt it), the
provider-reported usage, the trace and the session record. Nothing is sent anywhere; no token counting is done.

Each main-model attempt is classified from its own recorded request and the previous attempt's:
- `first`: the session's first request;
- `turn_start`: the task section changed (a new user turn);
- `ordinary`: the same task, and the previous request's working-context entries are a prefix of this one's;
- `after_change`: the same task, but earlier entries changed or went (an accepted edit took effect);
- `retry`: a further attempt of the same logical call (p015-retry/1).

The classes are the protocol's; the reads, writes and uncached input are the provider's own figures. A class with no
attempts is reported as not exercised.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

CLASSES = ("first", "ordinary", "turn_start", "after_change", "retry")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def session_dir(export: Path) -> Path:
    [found] = [p.parent for p in export.rglob("session.json") if p.parent.name.endswith("guarded_clm.r1")]
    return found


def user_text(started: dict[str, Any]) -> str:
    parts = [p for m in started["messages"] if m.get("kind") == "request" for p in m["parts"]
             if p.get("part_kind") == "user-prompt"]  # fmt: skip
    content = parts[-1]["content"]
    return content if isinstance(content, str) else "".join(x for x in content if isinstance(x, str))


def sections(text: str) -> tuple[str, list[str], str]:
    task = text.split("<task>\n", 1)[1].split("\n</task>", 1)[0]
    body = text.split("<working_context>\n", 1)[1].split("</working_context>", 1)[0]
    status = text.split("<runtime_status>\n", 1)[1]
    return task, [line for line in body.split("\n") if line.strip()], status


def calls(run: Path) -> list[dict[str, Any]]:
    rows = read_jsonl(run / "attempts.jsonl")
    started = {r["attempt"]: r for r in rows if r["event"] == "started"}
    finished = {r["attempt"]: r for r in rows if r["event"] == "finished"}
    out: list[dict[str, Any]] = []
    previous: tuple[str, list[str]] | None = None
    seen_calls: set[Any] = set()
    for k in sorted(finished):
        f, s = finished[k], started.get(k)
        row: dict[str, Any] = {"attempt": k, "category": f.get("category", "main"), "outcome": f["outcome"],
                               "charged_usd": f.get("charged_usd", 0.0), "latency_s": f.get("latency_s")}  # fmt: skip
        rep = f.get("reported") or {}
        row |= {key: rep.get(key) for key in ("cache_read_tokens", "cache_write_tokens", "input_tokens_uncached",
                                               "input_tokens_total", "output_tokens")}  # fmt: skip
        if s is None:  # refused before dispatch: never sent
            row["class"] = "refused"
            out.append(row)
            continue
        task, entries, status = sections(user_text(s))
        if f.get("logical_call") in seen_calls:
            row["class"] = "retry"
        elif previous is None:
            row["class"] = "first"
        elif task != previous[0]:
            row["class"] = "turn_start"
        elif entries[: len(previous[1])] == previous[1]:
            row["class"] = "ordinary"
        else:
            row["class"] = "after_change"
        seen_calls.add(f.get("logical_call"))
        row["entries"], row["pressure"] = len(entries), "PRESSURE" in status
        total = row["input_tokens_total"] or 0
        row["read_share"] = round((row["cache_read_tokens"] or 0) / total, 4) if total else None
        previous = (task, entries)
        out.append(row)
    return out


def summary(run: Path) -> dict[str, Any]:
    session = json.loads((run / "session.json").read_text(encoding="utf-8"))
    rows = calls(run)
    trace = read_jsonl(run / "trace.jsonl")
    result = session.get("launch_result") or {}
    by_class = {}
    for c in CLASSES:
        rs = [r for r in rows if r["class"] == c]
        tot = sum(r["input_tokens_total"] or 0 for r in rs)
        by_class[c] = {
            "attempts": len(rs),
            "read": sum(r["cache_read_tokens"] or 0 for r in rs),
            "written": sum(r["cache_write_tokens"] or 0 for r in rs),
            "uncached": sum(r["input_tokens_uncached"] or 0 for r in rs),
            "input_total": tot,
            "read_share": round(sum(r["cache_read_tokens"] or 0 for r in rs) / tot, 4) if tot else None,
            "exercised": bool(rs),
        }
    settings = session.get("settings") or {}
    return {
        "run_id": session["run_id"],
        "request_layout": settings.get("request_layout"),
        "cache_point": settings.get("cache_point"),
        "cache_settings": {k: v for k, v in sorted((session.get("model_settings") or {}).items())
                           if k.startswith("anthropic_cache")},  # fmt: skip
        "outcome": result.get("outcome"),
        "endings": result.get("endings"),
        "points": result.get("points"),
        "out_of": result.get("out_of"),
        "recall_points": result.get("recall_points"),
        "attempts": len(rows),
        "provider_errors": sum(1 for r in rows if r["outcome"] not in ("ok", "refused")),
        "refused": sum(1 for r in rows if r["outcome"] == "refused"),
        "charged_usd": round(sum(r["charged_usd"] or 0.0 for r in rows), 6),
        "latency_s": round(sum(r["latency_s"] or 0.0 for r in rows), 1),
        "pressure_requests": sum(1 for r in rows if r.get("pressure")),
        "over_limit_records": sum(1 for r in trace if r.get("type") == "lite_over_limit"),
        "edits": [r.get("status") for r in trace if r.get("type") == "lite_edit"],
        "by_class": by_class,
        "calls": rows,
    }


def markdown(a: dict[str, Any], b: dict[str, Any]) -> str:
    out = ["# dev-cache1: per-call caching analysis (generated by dev-cache1-analysis.py)", ""]
    out += ["| | A | B |", "| --- | --- | --- |"]
    for key in ("run_id", "request_layout", "cache_point", "cache_settings", "outcome", "points", "recall_points",
                "attempts", "provider_errors", "charged_usd", "latency_s", "pressure_requests", "over_limit_records",
                "edits"):  # fmt: skip
        out.append(f"| {key} | {a[key]} | {b[key]} |")
    out += ["", "| class | A attempts | A read share | B attempts | B read share |", "| --- | --- | --- | --- | --- |"]
    for c in CLASSES:
        ca, cb = a["by_class"][c], b["by_class"][c]
        cell = lambda x: x["read_share"] if x["exercised"] else "not exercised"  # noqa: E731
        out.append(f"| {c} | {ca['attempts']} | {cell(ca)} | {cb['attempts']} | {cell(cb)} |")
    for name, s in (("A", a), ("B", b)):
        out += ["", f"## {name}: every attempt", "",
                "| attempt | class | read | written | uncached | total | entries | charged |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |"]  # fmt: skip
        for r in s["calls"]:
            out.append(f"| {r['attempt']} | {r['class']} | {r['cache_read_tokens']} | {r['cache_write_tokens']} | "
                       f"{r['input_tokens_uncached']} | {r['input_tokens_total']} | {r.get('entries')} | "
                       f"{r['charged_usd']} |")  # fmt: skip
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    a, b = (summary(session_dir(Path(x))) for x in argv[:2])
    rest = argv[2:]
    if "--json" in rest:
        Path(rest[rest.index("--json") + 1]).write_text(json.dumps({"a": a, "b": b}, indent=1) + "\n")
    text = markdown(a, b)
    if "--markdown" in rest:
        Path(rest[rest.index("--markdown") + 1]).write_text(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
