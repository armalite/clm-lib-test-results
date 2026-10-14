import csv, io


def export_records(records, user, params):
    params = params or {}
    if user.get('role') == 'viewer':
        raise PermissionError('viewer')
    out = []
    admin = user.get('role') == 'admin'
    projs = user.get('projects') or []
    regs = user.get('regions') or []
    inc = params.get('include_archived') is True
    since = params.get('since')
    audit = admin and params.get('purpose') == 'audit'
    for r in records:
        if not admin and r.get('project') not in projs:
            continue
        st = r.get('status')
        if not (st == 'active' or (inc and st == 'archived')):
            continue
        if since and r.get('created', '') < since:
            continue
        if r.get('confidential') is True and not audit:
            continue
        if r.get('region') == 'eu' and 'eu' not in regs:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:mx]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], str(r['title']).strip(), r['owner'], r['amount']])
    return buf.getvalue()
