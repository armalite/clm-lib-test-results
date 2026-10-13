import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    return json.dumps({'exported_by': user.get('name'), 'records':","    truncated = False\n    mr = params.get('max_records')\n    if mr is not None and len(out) > mr:\n        out = out[:mr]\n        truncated = True\n    return json.dumps({'exported_by': user.get('name'), 'truncated': truncated, 'records':")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]+[{'id':'n5','role':'note','body':'Stage5 implemented: max_records slice after sort, truncated key in JSON.'}]
json.dump(c,open('/task/workspace/context.json','w'))