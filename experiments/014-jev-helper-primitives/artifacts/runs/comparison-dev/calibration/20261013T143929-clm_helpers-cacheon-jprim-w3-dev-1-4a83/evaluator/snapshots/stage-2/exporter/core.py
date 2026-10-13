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
        if params.get('since') is not None and str(r['created'])[:10] < params['since']:
            continue
        if r.get('region') == 'ch' and 'ch' not in (user.get('regions') or []):
            continue
        out.append(r)
    mr = params.get('max_records')
    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1:
        out = out[:mr]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], r['title'].strip(), r['owner'], r['amount']])
    return buf.getvalue()
