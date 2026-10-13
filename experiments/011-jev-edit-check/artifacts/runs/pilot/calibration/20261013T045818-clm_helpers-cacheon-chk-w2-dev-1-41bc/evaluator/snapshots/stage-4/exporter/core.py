"""Exporter implementation."""
import json


def _filter(records, user, params):
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer cannot export')
    out = []
    for r in records:
        if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):
            continue
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        since = params.get('since')
        if since is not None and r['created'] < since:
            continue
        out.append(r)
    return sorted(out, key=lambda r: r['id'])


def export_records(records, user, params):
    params = params or {}
    recs = _filter(records, user, params)
    out = [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': str(r['amount'])} for r in recs]
    return json.dumps({'exported_by': user.get('name'), 'records': out})
