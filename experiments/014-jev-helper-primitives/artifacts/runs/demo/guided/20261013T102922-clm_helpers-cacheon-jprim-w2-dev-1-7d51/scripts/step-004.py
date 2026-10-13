import subprocess,sys
sys.path.insert(0,'/task/workspace')
print(open('/task/fixtures/current-tests/test_stage.py').read()[:1500])
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("        out.append(r)","""        if r.get('confidential') is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        if params.get('since') is not None and str(r.get('created',''))[:10] < params['since']:
            continue
        out.append(r)""")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
import ctxhelper
req=open('/task/fixtures/stage-2/REQUIREMENTS.md').read()
print(ctxhelper.update(req,{'n.s2':"Stage2 done: confidential True skipped unless admin & purpose=='audit'; params since 'YYYY-MM-DD' -> created>=since (string cmp first 10 chars). OBLIGATION: if format changes from CSV, add top-level 'exported_by'=user['name'] unless withdrawn."}))