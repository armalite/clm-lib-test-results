import json
import csv, io, json

def export_records(records, user, params):
    params = params or {}
    admin = user.get('role') == 'admin'
    out = []
    for r in records:
        own = user.get('role') not in ('admin','viewer') and r.get('owner') == user.get('name')
        if not admin and not own and r.get('project') not in user.get('projects', []):
            continue
        if r.get('confidential') is True and not (admin and params.get('purpose') == 'audit'):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True and user.get('role') == 'admin')):
            continue
        out.append(r)
    out.sort(key=lambda r: r['id'])
    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': ' '.join(str(r['title']).split()), 'owner': r['owner'], 'amount': str(r['amount'])} for r in out]})
