p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("params.get('include_archived') is True)","params.get('include_archived') is True and user.get('role') == 'admin')")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-600:])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']=n['body'].replace('done through stage 3','done through stage 4')+"\nS4: include_archived honoured only for admin. Implemented."
json.dump({'format':'clm-context/v1','entries':[n]},open('/task/workspace/context.json','w'))