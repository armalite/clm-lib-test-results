import csv, io


def export_records(records, user, params):
    params = params or {}
    out = []
    admin = user.get('role') == 'admin'
    projs = user.get('projects') or []
    inc = params.get('include_archived') is True
    since = params.get('since')
    for r in records:
        if not admin and r.get('project') not in projs:
            continue
        st = r.get('status')
        if not (st == 'active' or (inc and st == 'archived')):
            continue
        if since and r.get('created', '') < since:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], str(r['title']).strip(), r['owner'], r['amount']])
    return buf.getvalue()
