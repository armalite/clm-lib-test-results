p='/task/workspace/exporter/core.py'
s=open(p).read()
i=s.index('def export_records')
s=s[:i].replace('import csv, io','import json')+'''def export_records(records, user, params):
    params = params or {}
    recs = _filter(records, user, params)
    out = [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': str(r['amount'])} for r in recs]
    return json.dumps({'exported_by': user.get('name'), 'records': out})
'''
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-800:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace('Status: stages 1-2 implemented, tests pass.','S3 CHANGED format: json.dumps({"exported_by":name,"records":[{id int,title,owner,amount str}]}) asc id; CSV rule replaced.\nStatus: stages 1-3 implemented (core.py: _filter + export_records).')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))