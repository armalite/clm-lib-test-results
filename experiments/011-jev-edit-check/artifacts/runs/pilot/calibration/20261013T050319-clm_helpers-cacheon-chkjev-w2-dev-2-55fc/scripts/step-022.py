p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    return json.dumps({'exported_by': user.get('name'), 'records'","    truncated = False\n    mr = params.get('max_records')\n    if mr is not None and len(out) > mr:\n        out = out[:mr]\n        truncated = True\n    return json.dumps({'exported_by': user.get('name'), 'truncated': truncated, 'records'")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
import json
c=json.load(open('/task/workspace/context.json'))
keep=[x for x in c['entries'] if x['id'] in('sum1','sum2','sum3','sum4')]
for x in keep:
    if x['id']=='sum4': x['body']=x['body'].replace(' Next: advance to stage 5.','')
keep.append({'id':'sum5','role':'summary','body':"Stage 5 (all 5 released): [NEW Record limit] params may contain 'max_records' int>=1; export only first max_records records (ascending id) remaining after every other rule; JSON object key \"truncated\": true if limit left out >=1 record, else false (also when absent). Implemented in core.py before json.dumps (slice out, truncated flag). Remaining: verify tests then final."})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))