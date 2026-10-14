import json

def export_records(records, user, params):
    params = params or {}
    role = user.get("role")
    if role == "viewer":
        raise PermissionError("viewer")
    out = []
    for r in sorted(records, key=lambda r: r["id"]):
        if role != "admin" and r.get("project") not in user.get("projects", []):
            continue
        st = r.get("status")
        if st != "active" and not (st == "archived" and params.get("include_archived") is True):
            continue
        s = params.get("since")
        if s is not None and (r.get("updated") or r["created"]) < s:
            continue
        if r.get("confidential") is True and not (role == "admin" and params.get("purpose") == "audit"):
            continue
        if r.get("region") == "eu" and "eu" not in (user.get("regions") or []):
            continue
        out.append(r)
    m = params.get("max_records")
    if m is not None:
        out = out[:m]
    recs = [{"id": r["id"], "title": r["title"].strip(), "owner": r["owner"], "amount": r["amount"]} for r in out]
    return json.dumps({"records": recs, "exported_by": user.get("name")})
