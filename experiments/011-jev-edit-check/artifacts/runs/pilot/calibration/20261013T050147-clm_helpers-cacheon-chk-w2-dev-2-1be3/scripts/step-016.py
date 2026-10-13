p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("    return json.dumps({'exported_by': user.get('name'), 'records'","    truncated = False\n    mr = params.get('max_records')\n    if isinstance(mr, int) and not isinstance(mr, bool) and mr >= 1 and len(out) > mr:\n        out = out[:mr]\n        truncated = True\n    return json.dumps({'exported_by': user.get('name'), 'truncated': truncated, 'records'")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])