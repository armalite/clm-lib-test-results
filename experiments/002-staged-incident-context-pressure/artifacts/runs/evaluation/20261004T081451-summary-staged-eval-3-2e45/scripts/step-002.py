import re
b='/task/fixtures/stage-1/logs/returns-svc.log'
c={}
for i,l in enumerate(open(b),1):
 if 'ERROR' in l or 'WARN' in l:
  k=re.sub(r'\d+','N',l[50:110])
  if k not in c:c[k]=i;print(i,l.rstrip()[:160])
open('/task/workspace/notes.txt','w').write('s1: rn 6.33.4-cb27 line5 tax timeout 2500->750; line19 pool 48->10; deploy deploys.log:3\n')