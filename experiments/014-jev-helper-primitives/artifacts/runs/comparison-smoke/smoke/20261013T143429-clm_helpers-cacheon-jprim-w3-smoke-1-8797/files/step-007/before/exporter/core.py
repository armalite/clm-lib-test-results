import csv, io

def export_records(records, user, params):
    params = params or {}
    admin = user.get('role') == 'admin'
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if not admin and r.get('project') not in user.get('projects', []):
            continue
        st = r.get('status')
        if not (st == 'active' or (st == 'archived' and params.get('include_archived') is True)):
            continue
        if r.get('confidential') and not (admin and params.get('purpose') == 'audit'):
            continue
        out.append(r)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id','title','owner','amount'])
    for r in out:
        w.writerow([r['id'], str(r['title']).strip(), r['owner'], r['amount']])
    return buf.getvalue()
