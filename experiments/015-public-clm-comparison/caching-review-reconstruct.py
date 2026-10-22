"""Supporting script for caching-review.md (2026-10-22). Usage, from a clm-lib checkout with the p015 environment:
    .venv-p015/bin/python caching-review-reconstruct.py <exported session dir> <the export's contract.json>

Read-only, offline: rebuild each recorded attempt's Anthropic request body with the pinned adapter (an in-memory
transport, a placeholder key, no network), then compare consecutive bodies with the recorded cache usage.

Reconstructed evidence: it shows what the pinned adapter emits for the recorded request, not a historical cache hit.
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

import httpx
from pydantic import TypeAdapter
from pydantic_ai.messages import ModelMessagesTypeAdapter
from pydantic_ai.models import ModelRequestParameters

from clm_lib.p015.live import ModelConfig, live_model

PARAMS = TypeAdapter(ModelRequestParameters)
REPLY = {"id": "msg_x", "type": "message", "role": "assistant", "model": "claude-sonnet-5",
         "content": [{"type": "text", "text": "x"}], "stop_reason": "end_turn", "stop_sequence": None,
         "usage": {"input_tokens": 1, "output_tokens": 1}}


def bodies(run: Path, model_cfg: dict[str, Any]) -> list[dict[str, Any]]:
    captured: list[dict[str, Any]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(json.loads(request.content))
        return httpx.Response(200, json=REPLY)

    cfg = ModelConfig(**model_cfg)
    model = live_model(cfg, http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
                       api_key="offline-placeholder")
    out = []
    rows = [json.loads(x) for x in (run / "attempts.jsonl").read_text().splitlines()]
    started = {r["attempt"]: r for r in rows if r["event"] == "started"}
    finished = {r["attempt"]: r for r in rows if r["event"] == "finished"}

    async def go() -> None:
        for k in sorted(started):
            s = started[k]
            msgs = ModelMessagesTypeAdapter.validate_python(s["messages"])
            params = PARAMS.validate_python(s["parameters"])
            n = len(captured)
            await model.request(msgs, s["settings"], params)
            body = captured[n]
            f = finished.get(k, {})
            out.append({"attempt": k, "category": s["category"], "body": body, "reported": f.get("reported"),
                        "outcome": f.get("outcome"),
                        "ts": [m.get("timestamp") for m in s["messages"] if m.get("kind") == "response"][-1:]})

    asyncio.run(go())
    return out


def blocks(body: dict[str, Any]) -> list[tuple[str, str]]:
    """The cacheable prefix in provider order, one entry per block, without cache_control markers."""
    def clean(x: Any) -> str:
        if isinstance(x, dict):
            x = {k: v for k, v in x.items() if k != "cache_control"}
        return json.dumps(x, sort_keys=True)
    out = [("tool", clean(t)) for t in body.get("tools", [])]
    system = body.get("system")
    if isinstance(system, str):
        out.append(("system", clean({"type": "text", "text": system})))
    else:
        out += [("system", clean(b)) for b in system or []]
    for i, m in enumerate(body["messages"]):
        content = m["content"] if isinstance(m["content"], list) else [{"type": "text", "text": m["content"]}]
        out += [(f"{m['role']}[{i}]", clean(c)) for c in content]
    return out


def markers(body: dict[str, Any]) -> list[str]:
    out = []
    if body.get("cache_control"):
        out.append(f"top-level {body['cache_control']}")
    out += [f"tool {t['name']} {t['cache_control']}" for t in body.get("tools", []) if "cache_control" in t]
    system = body.get("system")
    if isinstance(system, list):
        out += [f"system[{i}] {b['cache_control']}" for i, b in enumerate(system) if "cache_control" in b]
    for i, m in enumerate(body["messages"]):
        if isinstance(m["content"], list):
            out += [f"messages[{i}].content[{j}]" for j, c in enumerate(m["content"]) if "cache_control" in c]
    return out


def compare(prev: dict[str, Any], cur: dict[str, Any]) -> dict[str, Any]:
    a, b = blocks(prev), blocks(cur)
    same = 0
    while same < min(len(a), len(b)) and a[same] == b[same]:
        same += 1
    chars = lambda xs: sum(len(x[1]) for x in xs)  # noqa: E731
    first = b[same][0] if same < len(b) else "(none)"
    return {"prev_blocks": len(a), "cur_blocks": len(b), "common_blocks": same, "prefix_is_whole_prev": same == len(a),
            "appended_blocks": len(b) - same, "first_change": first, "common_chars": chars(b[:same]),
            "total_chars": chars(b), "positions_from_end_to_prev_end": len(b) - len(a) if same == len(a) else None}


if __name__ == "__main__":
    run = Path(sys.argv[1])
    model_cfg = json.loads(Path(sys.argv[2]).read_text())["model"]
    rows = bodies(run, model_cfg)
    by_cat: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)
    for cat, rs in by_cat.items():
        print(f"== {run.name} category={cat}: {len(rs)} requests; markers of the first: {markers(rs[0]['body'])}")
        tools0 = [t for t in rs[0]["body"].get("tools", [])]
        sys0 = rs[0]["body"].get("system")
        for i, r in enumerate(rs):
            rep = r["reported"] or {}
            row = {"attempt": r["attempt"], "read": rep.get("cache_read_tokens"), "write": rep.get("cache_write_tokens"),
                   "uncached": rep.get("input_tokens_uncached"), "total": rep.get("input_tokens_total"),
                   "tools_same_as_first": r["body"].get("tools") == tools0,
                   "system_same_as_first": r["body"].get("system") == sys0}
            if i:
                row |= compare(rs[i - 1]["body"], r["body"])
            print(json.dumps(row))
