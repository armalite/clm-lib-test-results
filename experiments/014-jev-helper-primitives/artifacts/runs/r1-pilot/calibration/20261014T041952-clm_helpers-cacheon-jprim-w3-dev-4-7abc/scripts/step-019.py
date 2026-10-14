import sys,subprocess;sys.path.insert(0,'/task/workspace')
import regmaint
regmaint.update(6)
p='/task/workspace/exporter/core.py';s=open(p).read()
import re
for i,l in enumerate(s.splitlines(),1):
  if 'eu' in l or 'region' in l: print(i,l)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])
c=regmaint.load()
for e in c['entries']:
  if e['id'] in('reg.S2.6','reg.S6.1','reg.S6.2'):print(e['id'],e['body'][:200])