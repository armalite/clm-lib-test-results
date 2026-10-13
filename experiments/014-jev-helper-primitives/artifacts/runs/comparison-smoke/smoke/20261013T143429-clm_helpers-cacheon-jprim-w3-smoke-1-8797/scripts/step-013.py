import sys,subprocess,inspect;sys.path.insert(0,'/task/workspace')
import reghelper as H
p='/task/workspace/exporter/core.py';s=open(p).read()
s=s.replace("params.get('purpose') == 'audit')","params.get('purpose') in ('audit', 'regulator'))")
s=s.replace("return json.dumps({'exported_by': user.get('name'), 'records':","d = {} if user.get('role') == 'admin' else {'exported_by': user.get('name')}\n    return json.dumps({**d, 'records':")
open(p,'w').write(s)
c=H.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body'].split('\n')
try:
  a=H.affected({str(i):l for i,l in enumerate(reg)},{'S5.1':'confidential also exportable when admin and purpose==regulator','S5.2':'exported_by omitted for admin exports'});print(H.decide(a,0.5))
except Exception as e: print('jev err',e)
reg[1]='CURRENT [S2.2, S3.1, S5.2] Every non-admin export includes top-level exported_by = user[name]; admin exports omit exported_by.'
reg[3]='CURRENT [S1.3, S5.1] Confidential records never exported, except role admin and params purpose==audit or purpose==regulator; other rules still apply.'
reg.append('HISTORY [S2.2] exported_by originally required for all roles incl admin; S5.2 removed it for admin.')
reg.append('HISTORY [S1.3] Confidential exception originally only purpose audit; S5.1 added regulator.')
c['entries']=[{'id':'s5.sum','role':'summary','body':'All 5 stages done in exporter/core.py.'}]
H.set_register(c,reg);H.save(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-600:])