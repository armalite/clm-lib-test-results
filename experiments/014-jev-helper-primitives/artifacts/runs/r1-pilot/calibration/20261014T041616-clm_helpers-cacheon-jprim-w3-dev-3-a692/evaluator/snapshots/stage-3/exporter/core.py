import csv, io, json

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer')
    since = params.get('since')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        if r.get('status') != 'active' and not (r.get('status') == 'archived' and params.get('include_archived') is True):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if since is not None and str(r.get('created',''))[:10] < since:
            continue
        if r.get('region') == 'eu' and 'eu' not in user.get('regions', []):
            continue
        out.append(r)
    mx = params.get('max_records')
    if mx is not None:
        out = out[:mx]
    res = {'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': str(r['title']).strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out]}
    return json.dumps(res)
