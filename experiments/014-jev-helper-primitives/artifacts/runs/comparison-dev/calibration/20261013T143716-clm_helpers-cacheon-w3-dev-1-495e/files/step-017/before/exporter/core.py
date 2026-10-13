import json

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    since = params.get('since')
    regions = [str(x).lower() for x in (user.get('regions') or [])]
    out = []
    for r in records:
        if role == 'viewer':
            if r.get('owner') != user.get('name'):
                continue
        elif role != 'admin' and r.get('project') not in (user.get('projects') or []) and r.get('owner') != user.get('name'):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True and role == 'admin')):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') in ('audit', 'litigation')):
            continue
        if since is not None and str(r.get('created', ''))[:10] < since:
            continue
        if str(r.get('region') or '').lower() == 'ch' and 'ch' not in regions:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:mx]
    recs = []
    for r in out:
        t = r['title']
        recs.append({'id': r['id'], 'title': ' '.join(t.split()) if isinstance(t, str) else t, 'owner': r['owner'], 'amount': r['amount']})
    res = {'exported_by': user.get('name'), 'records': recs}
    if role == 'admin' and params.get('purpose') == 'litigation':
        res['confidential_count'] = sum(1 for r in out if r.get('confidential') is True)
    return json.dumps(res)
