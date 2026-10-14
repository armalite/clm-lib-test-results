import csv, io


def export_records(records, user, params):
    params = params or {}
    if user.get('role') == 'viewer':
        raise PermissionError('viewer')
    out = []
    admin = user.get('role') == 'admin'
    projs = user.get('projects') or []
    regs = user.get('regions') or []
    inc = params.get('include_archived') is True
    since = params.get('since')
    audit = admin and params.get('purpose') in ('audit', 'regulator')
    for r in records:
        if not admin and r.get('project') not in projs and r.get('owner') != user.get('name'):
            continue
        st = r.get('status')
        if not (st == 'active' or (inc and st == 'archived')):
            continue
        if since and (r.get('updated') or r.get('created', '')) < since:
            continue
        if r.get('confidential') is True and not audit:
            continue
        if r.get('region') == 'eu' and 'eu' not in regs:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:mx]
    import json
    obj = {'records': [{'id': r['id'], 'title': str(r['title']).strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out], 'exported_by': user.get('name')}
    cc = sum(1 for r in out if r.get('confidential') is True)
    if cc and params.get('purpose') != 'audit':
        obj['confidential_count'] = cc
    return json.dumps(obj)
