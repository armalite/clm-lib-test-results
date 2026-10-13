import json


def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer cannot export')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        if r['confidential'] and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if r.get('status') != 'active' and not (params.get('include_archived') is True and user.get('role') == 'admin' and r.get('status') == 'archived'):
            continue
        since = params.get('since')
        if since is not None and r['created'] < since:
            continue
        out.append(r)
    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': r['amount']} for r in out]})
