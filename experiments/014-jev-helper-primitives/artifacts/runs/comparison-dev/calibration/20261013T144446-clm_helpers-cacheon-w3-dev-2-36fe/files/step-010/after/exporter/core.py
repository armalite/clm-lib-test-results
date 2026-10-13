import json


def export_records(records, user, params):
    params = params or {}
    role = user.get("role")
    if role == "viewer":
        raise PermissionError("viewer")
    out = []
    for r in sorted(records, key=lambda r: r["id"]):
        if role != "admin" and r.get("project") not in user.get("projects", []) and r.get("owner") != user.get("name"):
            continue
        st = r.get("status")
        if not (st == "active" or (st == "archived" and params.get("include_archived") is True)):
            continue
        since = params.get("since")
        if since is not None and (r.get("updated") or r["created"]) < since:
            continue
        if r.get("confidential") is True and not (role == "admin" and params.get("purpose") in ("audit", "legal")):
            continue
        if r.get("region") == "eu" and "eu" not in (user.get("regions") or []):
            continue
        out.append(r)
    mx = params.get("max_records")
    if isinstance(mx, int) and mx >= 1:
        out = out[:mx]
    recs = [{"id": r["id"], "title": r["title"].strip(), "owner": r["owner"], "amount": r["amount"]} for r in out]
    res = {"exported_by": user.get("name"), "records": recs}
    if params.get("purpose") != "audit" and any(r.get("confidential") is True for r in out):
        res["confidential_count"] = sum(1 for r in out if r.get("confidential") is True)
    return json.dumps(res)
