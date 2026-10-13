import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        st = r['status']
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        out.append(r)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], r['title'], r['owner'], r['amount']])
    return buf.getvalue()
