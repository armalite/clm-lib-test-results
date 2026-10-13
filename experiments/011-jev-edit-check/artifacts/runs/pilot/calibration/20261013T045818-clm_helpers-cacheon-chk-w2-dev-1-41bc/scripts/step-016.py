p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    recs = _filter(records, user, params)\n","    recs = _filter(records, user, params)\n    mr = params.get('max_records')\n    truncated = False\n    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1 and len(recs) > mr:\n        recs = recs[:mr]; truncated = True\n")
s=s.replace("'records': out})","'records': out, 'truncated': truncated})")
open(p,'w').write(s)
import subprocess,sys,json
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(q.stderr[-600:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace('Status: stages 1-4','S5 NEW max_records slice + truncated bool key.\nStatus: stages 1-5')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))