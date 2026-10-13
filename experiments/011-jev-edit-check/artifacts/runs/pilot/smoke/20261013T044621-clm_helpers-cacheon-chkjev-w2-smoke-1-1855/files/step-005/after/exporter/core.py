import csv, io


def export_records(records, user, params):
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    if role == 'admin':
        sel = list(records)
    else:
        projs = set(user.get('projects') or [])
        sel = [r for r in records if r['project'] in projs]
    sel = sorted(sel, key=lambda r: r['id'])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator=chr(10))
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in sel:
        w.writerow([int(r['id']), r['title'], r['owner'], r['amount']])
    return buf.getvalue()
