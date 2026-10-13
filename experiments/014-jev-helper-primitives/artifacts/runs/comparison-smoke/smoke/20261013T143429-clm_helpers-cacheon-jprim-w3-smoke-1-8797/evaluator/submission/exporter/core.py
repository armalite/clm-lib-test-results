import csv, io

def export_records(records, user, params):
    params = params or {}
    admin = user.get('role') == 'admin'
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if not admin and r.get('project') not in user.get('projects', []) and not (user.get('role') not in ('admin','viewer') and r.get('owner') == user.get('name')):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True and user.get('role') == 'admin')):
            continue
        if r.get('confidential') and not (admin and params.get('purpose') in ('audit', 'regulator')):
            continue
        out.append(r)
    import json
    d = {} if user.get('role') == 'admin' else {'exported_by': user.get('name')}
    return json.dumps({**d, 'records': [{'id': int(r['id']), 'title': ' '.join(str(r['title']).split()), 'owner': r['owner'], 'amount': str(r['amount'])} for r in out]})
