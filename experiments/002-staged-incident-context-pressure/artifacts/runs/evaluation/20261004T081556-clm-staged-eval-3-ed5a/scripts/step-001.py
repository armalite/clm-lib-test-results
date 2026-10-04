import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/returns-svc.yaml','deploy/deploys.log','deploy/release-notes-6.33.4-cb27.md','ops/oncall-notes.md']:
 print('##',f)
 for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import re
for f in ['logs/edge-gw.log','logs/returns-svc.log']:
 L=open(b+f).read().splitlines()
 e=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|timeout|exhaust|fail',l,re.I)]
 print('##',f,len(e))
 for x in e[:6]:print(x)