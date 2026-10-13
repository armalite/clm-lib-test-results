import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    out = []
    for r in records:
        if role == 'viewer':
            if r.get('owner') != user.get('name'):
                continue
        elif role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True and role == 'admin')):
            continue
        since = params.get('since')
        if since is not None and (r.get('updated') or r.get('created', '')) < since:
            continue
        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') in ('audit', 'legal')):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    mx = params.get('max_records')
    if isinstance(mx, int) and not isinstance(mx, bool) and mx >= 1:
        out = out[:min(mx, 25)]
    import json
    recs=[{'id': int(r['id']), 'title': r['title'].strip(), 'owner': r['owner'], 'project': r.get('project'), 'amount': r['amount']} for r in out]
    doc={}
    if role != 'admin':
        doc['exported_by']=user.get('name')
    doc['records']=recs
    doc['confidential_count']=sum(1 for r in out if r.get('confidential') is True)
    return json.dumps(doc)
