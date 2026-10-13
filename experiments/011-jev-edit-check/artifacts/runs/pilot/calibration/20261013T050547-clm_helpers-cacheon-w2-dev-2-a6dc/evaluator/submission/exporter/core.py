import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer cannot export')
    out = []
    for r in records:
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True and user.get('role') == 'admin')):
            continue
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        if r['confidential'] and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if params.get('since') is not None and str(r.get('created',''))[:10] < params['since']:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    truncated = False
    mr = params.get('max_records')
    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1 and len(out) > mr:
        out = out[:mr]; truncated = True
    import json
    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': str(r['amount'])} for r in out], 'truncated': truncated})
