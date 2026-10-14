import json

def export_records(records, user, params):
    params = params or {}
    role = user.get("role")
    out = []
    for r in sorted(records, key=lambda r: r["id"]):
        if role == "viewer":
            if r.get("owner") != user.get("name"):
                continue
        elif role != "admin" and r.get("project") not in user.get("projects", []) and r.get("owner") != user.get("name"):
            continue
        st = r.get("status")
        if st != "active" and not (st == "archived" and params.get("include_archived") is True and role == "admin"):
            continue
        s = params.get("since")
        if s is not None and (r.get("updated") or r["created"]) < s:
            continue
        if r.get("confidential") is True and not (role == "admin" and params.get("purpose") in ("audit", "regulator")):
            continue
        if r.get("region") == "eu" and "eu" not in (user.get("regions") or []):
            continue
        out.append(r)
    m = params.get("max_records")
    if m is not None:
        out = out[:min(m, 20)]
    recs = [{"id": r["id"], "title": r["title"].strip(), "owner": r["owner"], "amount": r["amount"]} for r in out]
    res = {"records": recs, "exported_by": user.get("name")}
    if role == "admin" and params.get("purpose") == "regulator":
        res["confidential_count"] = sum(1 for r in out if r.get("confidential") is True)
    return json.dumps(res)
