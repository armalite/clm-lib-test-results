import json


def export_records(records, user, params):
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer may not export')
    if role == 'admin':
        sel = list(records)
    else:
        projs = set(user.get('projects') or [])
        sel = [r for r in records if r.get('project') in projs]
    sel = sorted(sel, key=lambda r: int(r['id']))
    out = {'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': r['amount']} for r in sel],
           'exported_by': user.get('name')}
    return json.dumps(out)
