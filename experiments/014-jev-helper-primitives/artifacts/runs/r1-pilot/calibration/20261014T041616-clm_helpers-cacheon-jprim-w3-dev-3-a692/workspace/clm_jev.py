"""clm_jev: ask Jev narrow yes/no questions from your own code (jev-primitive/1).

    import clm_jev
    r = clm_jev.judge("Does the update change the rule stated in this entry?",
                      {"n1": "...entry text...", "n2": "..."},
                      background="...the update text...")
    # r == {"status": "ok", "answers": {"n1": 0.93, "n2": 0.04}, "model": "...", "error": None}
    # r["status"] == "error": r["error"] says why; answers are None. Nothing is retried for you.

Up to 20 items per call; each answer is the probability that the question is true for that item.
The answers are judgments that can be wrong. Your code decides what to do with them.
"""
import json, os, time, uuid

_BOX = "/task/workspace/.clm-jev"


def judge(question, items, background="", criteria=None, timeout=25.0):
    items = {str(k): str(v) for k, v in dict(items).items()}
    os.makedirs(_BOX, exist_ok=True)
    rid = uuid.uuid4().hex[:16]
    req = {"version": "jev-primitive/1", "id": rid, "question": str(question),
           "background": str(background), "items": [{"key": k, "text": v} for k, v in items.items()]}
    if criteria:
        req["criteria"] = {"true": str(criteria["true"]), "false": str(criteria["false"])}
    tmp = os.path.join(_BOX, ".req-" + rid + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(req, fh)
    os.replace(tmp, os.path.join(_BOX, "req-" + rid + ".json"))
    path = os.path.join(_BOX, "resp-" + rid + ".json")
    deadline = time.monotonic() + float(timeout)
    while time.monotonic() < deadline:
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    return json.load(fh)
            except ValueError:
                pass
        time.sleep(0.05)
    return {"status": "error", "error": "no response from the runtime within the timeout",
            "answers": {k: None for k in items}, "model": None}
