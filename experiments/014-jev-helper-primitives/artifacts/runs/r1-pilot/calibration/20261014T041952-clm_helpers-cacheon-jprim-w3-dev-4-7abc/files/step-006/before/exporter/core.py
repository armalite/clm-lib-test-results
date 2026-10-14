import csv, io

def export_records(records, user, params):
    params = params or {}
    out = []
    for r in sorted(records, key=lambda r: r["id"]):
        if user.get("role") != "admin" and r["project"] not in user.get("projects", []):
            continue
        if r["status"] != "active" and not (r["status"] == "archived" and params.get("include_archived") is True):
            continue
        s = params.get("since")
        if s is not None and r["created"] < s:
            continue
        out.append(r)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["id", "title", "owner", "amount"])
    for r in out:
        w.writerow([r["id"], r["title"].strip(), r["owner"], r["amount"]])
    return buf.getvalue()
