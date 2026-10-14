p='/task/workspace/exporter/core.py'
L=open(p).read().split('\n')
print(L[26:28])
if L[27].strip()=='continue':
    del L[26:28]
open(p,'w').write('\n'.join(L))
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-800:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]
reg['body']=reg['body'].replace("CURRENT [S2.6] region 'eu' exported only if 'eu' in user['regions'] (admins too).","HISTORY [S2.6, S6.1] region 'eu' was exported only if 'eu' in user['regions']; withdrawn by S6.1: all regions exported under ordinary rules.\nHISTORY [S6.2] Note: web UI shows 50 records/page; exports unchanged.")
c['entries']=[reg,{'id':'prog','role':'note','body':'Stages 1-6 implemented in exporter/core.py (JSON output).'}]
json.dump(c,open('/task/workspace/context.json','w'))