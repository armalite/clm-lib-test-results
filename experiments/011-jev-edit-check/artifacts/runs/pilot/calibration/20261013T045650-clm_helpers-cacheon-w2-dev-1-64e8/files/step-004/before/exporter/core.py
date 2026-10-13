import csv, io


def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer cannot export')
    out = []
    for r in records:
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([int(r['id']), r['title'], r['owner'], r['amount']])
    return buf.getvalue()
