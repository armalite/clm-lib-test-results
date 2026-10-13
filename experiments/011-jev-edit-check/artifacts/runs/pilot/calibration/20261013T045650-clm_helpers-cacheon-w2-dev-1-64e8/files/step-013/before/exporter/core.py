import csv, io, json


def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer cannot export')
    out = []
    for r in records:
        if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        since = params.get('since')
        if since is not None and str(r.get('created'))[:10] < since:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': r['amount']} for r in out]})
