import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer')
    out = []
    for r in records:
        if role != 'admin' and r.get('project') not in user.get('projects', []):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        since = params.get('since')
        if since is not None and (r.get('updated') or r.get('created', '')) < since:
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if r.get('region') == 'eu' and 'eu' not in (user.get('regions') or []):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:mx]
    import json
    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'].strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out]})
