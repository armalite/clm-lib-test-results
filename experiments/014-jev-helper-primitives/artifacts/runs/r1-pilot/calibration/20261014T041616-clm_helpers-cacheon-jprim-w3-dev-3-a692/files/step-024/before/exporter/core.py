import csv, io, json

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    since = params.get('since')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role == 'viewer':
            if r.get('owner') != user.get('name'):
                continue
        elif role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        if r.get('status') != 'active' and not (r.get('status') == 'archived' and params.get('include_archived') is True and role == 'admin'):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') in ('audit','legal')):
            continue
        if since is not None and str(r.get('created',''))[:10] < since:
            continue
        if str(r.get('region') or '').lower() == 'eu' and 'eu' not in [str(x).lower() for x in user.get('regions', [])]:
            continue
        out.append(r)
    mx = params.get('max_records')
    if mx is not None:
        out = out[:min(mx, 30)]
    res = {'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': ' '.join(str(r['title']).split()), 'owner': r['owner'], 'amount': r['amount']} for r in out]}
    if role == 'admin' and params.get('purpose') == 'legal':
        res['confidential_count'] = sum(1 for r in out if r.get('confidential') is True)
    if role == 'admin':
        res.pop('exported_by', None)
    return json.dumps(res)
