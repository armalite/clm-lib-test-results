"""014 follow-up design (development material): how much context-maintenance work recorded runs did.

Usage (from this folder):  python displaceable_work.py
Reads only exported artifacts in this results repository (no clm-lib import, no API calls).

For each selected run it reports the cost split by token class (using the dated price recorded
in the run's run.json) and the context-maintenance work visible in the traces:
- accepted context edits, and how many model-written (non-runtime) entries each added,
  rewrote or removed;
- characters of model-written entry text that the edits introduced (new or changed bodies):
  an upper bound on the note text Claude had to emit itself, since the step script carries it;
- the share of all output tokens that this text represents (at 3.5 characters per token, a
  rough conversion that is stated, not measured);
- prompt-cache writes in the request after each edit (an edit invalidates the cached prefix
  from the first changed block onward);
- steps whose code names an earlier stage's or round's source folder (rereading).
These are measurements of what ordinary CLM spent, not estimates of what Jev would save.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

EXP = Path(__file__).resolve().parents[2]
RUNTIME_ID = re.compile(r"^s\d+\.(act|obs|rcpt)$|^u-|^sys")
FIXTURE_DIR = re.compile(r"/task/fixtures/(?:stage|round)-0*(\d+)")
CHARS_PER_TOKEN = 3.5  # rough conversion for code/notes text; stated, not measured
RUNS = {
    # ordinary clm_helpers runs on the W2 changing-requirements workload (011 pilot, condition A)
    "W2 A dev-1 (011)": "011-jev-edit-check/artifacts/runs/pilot/calibration/20261013T045650-clm_helpers-cacheon-w2-dev-1-64e8",
    "W2 A dev-2 (011)": "011-jev-edit-check/artifacts/runs/pilot/calibration/20261013T050547-clm_helpers-cacheon-w2-dev-2-a6dc",
    # the 014 prompted demonstration (configured Jev helper), for contrast
    "W2 014 demo": "014-jev-helper-primitives/artifacts/runs/demo/guided/20261013T102922-clm_helpers-cacheon-jprim-w2-dev-1-7d51",
}


def _incident_a_runs() -> dict[str, str]:
    """Ordinary CLM (condition A) runs of the 010 v3 evaluation on the incident-rounds workload."""
    base = EXP / "010-jev-initiated-review/artifacts/runs/v3/evaluation"
    out = {}
    for d in sorted(base.glob("*-clm_helpers-cacheon-rounds-eval-*")):
        out[f"rounds A {d.name.split('-rounds-')[1][:-5]} ({d.name[9:15]})"] = str(d.relative_to(EXP))
    return out


def entries(run: Path, rev: int) -> dict[str, dict]:
    p = run / "context" / f"rev-{rev:04d}.json"
    return {e["id"]: e for e in json.loads(p.read_text())["entries"]} if p.exists() else {}


def analyse(name: str, run: Path) -> dict:
    s = json.loads((run / "summary.json").read_text())
    price = json.loads((run / "run.json").read_text())["price"]
    ev = [json.loads(x) for x in (run / "events.jsonl").read_text().splitlines()]
    u = s["usage_provider_reported"]
    cost = {
        "uncached_in": u["input_tokens_uncached"] * price["input"] / 1e6,
        "cache_read": u["cache_read_input_tokens"] * price["cache_read"] / 1e6,
        "cache_write": u["cache_creation_input_tokens"] * price["cache_write_5m"] / 1e6,
        "output": u["output_tokens"] * price["output"] / 1e6,
    }
    edits = [e for e in ev if e["event"] == "context_edit" and e.get("status") == "accepted" and e.get("changed")]
    reqs = {e["step"]: e for e in ev if e["event"] == "request"}
    resp = {e["step"]: e for e in ev if e["event"] == "response"}
    written_chars, model_entries_changed, post_edit_cache_write = 0, [], []
    for e in edits:
        before, after = entries(run, e["before_revision"]), entries(run, e["after_revision"])
        changed = [
            i for i, x in after.items()
            if not RUNTIME_ID.match(i) and (i not in before or before[i]["body"] != x["body"])
        ]
        removed = [i for i in before if not RUNTIME_ID.match(i) and i not in after]
        written_chars += sum(len(after[i]["body"]) for i in changed)
        model_entries_changed.append((e["step"], len(changed), len(removed), len([i for i in after if not RUNTIME_ID.match(i)])))
        nxt = resp.get(e["step"] + 1)
        if nxt:
            post_edit_cache_write.append(nxt["usage"].get("cache_creation_input_tokens", 0))
    # Rereads: step scripts that name an earlier stage/round's fixture folder than the latest
    # released one (the runtime trace records workspace files only, so the script text is used).
    rereads, latest = 0, 1
    for e in ev:
        if e["event"] == "stage_released":
            latest = max(latest, e["stage"])
        elif e["event"] == "execution_start":
            code = (run / e["script"]).read_text()
            older = {int(n) for n in FIXTURE_DIR.findall(code) if int(n) < latest}
            rereads += bool(older)
    out_tok = u["output_tokens"]
    return {
        "run": name,
        "outcome": f"{s['score'].get('passed', s['score'].get('checks_passed', '?'))}/{s['score'].get('checks', '?')}",
        "usd": round(s["cost"]["incurred_usd"], 4),
        "split_pct": {k: round(100 * v / max(sum(cost.values()), 1e-9)) for k, v in cost.items()},
        "calls": s["counts"]["provider_calls"],
        "output_tokens": out_tok,
        "edits": len(edits),
        "model_entries_per_edit(step,changed,removed,total)": model_entries_changed,
        "note_text_chars_written": written_chars,
        "note_text_share_of_output_pct": round(100 * written_chars / CHARS_PER_TOKEN / max(out_tok, 1)),
        "mean_cache_write_after_edit": round(sum(post_edit_cache_write) / max(len(post_edit_cache_write), 1)),
        "mean_cache_write_all": round(u["cache_creation_input_tokens"] / max(s["counts"]["provider_calls"], 1)),
        "max_context_est_tokens": max((r.get("context_tokens_est") or json.loads((run / r["file"]).read_text())["meta"]["est_input_tokens"]) for r in reqs.values()),
        "steps_rereading_earlier_sources": rereads,
    }


def main() -> None:
    for name, rel in {**RUNS, **_incident_a_runs()}.items():
        print(json.dumps(analyse(name, EXP / rel)))


if __name__ == "__main__":
    main()
