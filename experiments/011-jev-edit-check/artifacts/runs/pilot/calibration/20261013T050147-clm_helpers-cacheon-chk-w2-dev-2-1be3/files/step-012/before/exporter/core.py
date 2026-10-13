import csv, io, json


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
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        if params.get('since') is not None and str(r.get('created',''))[:10] < params['since']:
            continue
        out.append(r)
    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': str(r['amount'])} for r in out]})
