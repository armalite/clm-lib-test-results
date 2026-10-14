import json
import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    out = []
    since = params.get('since')
    for r in records:
        if role == 'viewer':
            if r.get('owner') != user.get('name'):
                continue
        elif role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and role == 'admin' and params.get('include_archived') is True)):
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') in ('audit', 'legal')):
            continue
        if since is not None and str(r.get('created', ''))[:10] < since:
            continue
        if str(r.get('region') or '').lower() == 'eu' and 'eu' not in [str(x).lower() for x in (user.get('regions') or [])]:
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and mx >= 1:
        out = out[:mx]
    recs = []
    for r in out:
        t = r['title']
        recs.append({'id': int(r['id']), 'title': ' '.join(t.split()) if isinstance(t, str) else t, 'owner': r['owner'], 'amount': r['amount']})
    doc = {'records': recs}
    if role != 'admin':
        doc['exported_by'] = user.get('name')
    if params.get('purpose') == 'legal' and role == 'admin':
        doc['confidential_count'] = sum(1 for r in out if r.get('confidential') is True)
    return json.dumps(doc)
