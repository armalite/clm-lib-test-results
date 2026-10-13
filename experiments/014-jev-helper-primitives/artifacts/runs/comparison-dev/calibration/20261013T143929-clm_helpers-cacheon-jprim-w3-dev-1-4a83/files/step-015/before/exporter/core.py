import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role == 'viewer':
            if r.get('owner') != user.get('name'):
                continue
        elif role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        st = r['status']
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True and role == 'admin')):
            continue
        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') in ('audit', 'litigation')):
            continue
        if params.get('since') is not None and str(r['created'])[:10] < params['since']:
            continue
        if str(r.get('region') or '').lower() == 'ch' and 'ch' not in [str(x).lower() for x in (user.get('regions') or [])]:
            continue
        out.append(r)
    mr = params.get('max_records')
    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1:
        out = out[:mr]
    import json
    res = {'exported_by': user.get('name')}
    cc = sum(1 for r in out if r['confidential'] is True)
    if cc and params.get('purpose') != 'audit':
        res['confidential_count'] = cc
    res['records'] = [
        {'id': int(r['id']), 'title': ' '.join(r['title'].split()), 'owner': r['owner'], 'amount': r['amount']} for r in out]
    return json.dumps(res)
