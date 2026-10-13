import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    out.sort(key=lambda r: r['id'])\n","    out.sort(key=lambda r: r['id'])\n    truncated = False\n    mr = params.get('max_records')\n    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1 and len(out) > mr:\n        out = out[:mr]; truncated = True\n")
s=s.replace("for r in out]})","for r in out], 'truncated': truncated})")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-600:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=c['entries'][:4]+[{'id':'n5','role':'note','body':'Stage5 (final) implemented: max_records truncation after sort + truncated key. If tests OK, give final.'}]
json.dump(c,open('/task/workspace/context.json','w'))