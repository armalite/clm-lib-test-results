import json

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    since = params.get('since')
    regions = user.get('regions') or []
    out = []
    for r in records:
        if role != 'admin' and r.get('project') not in (user.get('projects') or []) and r.get('owner') != user.get('name'):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if since is not None and str(r.get('created', ''))[:10] < since:
            continue
        if r.get('region') == 'ch' and 'ch' not in regions:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:mx]
    recs = []
    for r in out:
        t = r['title']
        recs.append({'id': r['id'], 'title': t.strip() if isinstance(t, str) else t, 'owner': r['owner'], 'amount': r['amount']})
    return json.dumps({'exported_by': user.get('name'), 'records': recs})
