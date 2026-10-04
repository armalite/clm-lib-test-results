import re
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
 print('##',f)
 for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
c={}
for i,l in enumerate(open(b+'logs/returns-svc.log'),1):
 if 'ERROR' in l:
  k=re.sub(r'\d+','N',l[50:100])
  if k not in c:c[k]=i;print(i,l.rstrip()[:150])
open('/task/workspace/notes.txt','a').write('s2 released\n')