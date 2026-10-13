import re
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace('import csv, io','import json')
s=s.replace("        out.append(r)","        since = params.get('since')\n        if since is not None and r['created'] < since:\n            continue\n        out.append(r)")
i=s.index('    buf = io.StringIO()')
s=s[:i]+"    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': r['amount']} for r in out]})\n"
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])