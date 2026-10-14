src=open('exporter/core.py').read()
src=src.replace("params.get('include_archived') is True)","params.get('include_archived') is True and role == 'admin')")
src=src.replace("if r.get('region') == 'eu' and 'eu' not in user.get('regions', []):","if str(r.get('region') or '').lower() == 'eu' and 'eu' not in [str(x).lower() for x in user.get('regions', [])]:")
src=src.replace("str(r['title']).strip()","' '.join(str(r['title']).split())")
open('exporter/core.py','w').write(src)
import subprocess,sys
p=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(p.stderr[-800:])
import reghelper
reghelper.update(4)