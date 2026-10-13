import csv, io, json

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    out = []
    for r in records:
        if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if params.get('since') is not None and r['created'] < params['since']:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    truncated = False
    mr = params.get('max_records')
    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1 and len(out) > mr:
        out = out[:mr]
        truncated = True
    return json.dumps({'exported_by': user.get('name'), 'truncated': truncated, 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': r['amount']} for r in out]})
