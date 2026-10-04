import re,collections
b='/task/fixtures/stage-1/'
for f in ['logs/billing-svc.log','logs/front-proxy.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or ' 5' in l[:200] and 'status=5' in l:
      k=re.sub(r'\d+','N',l[25:])[:80]
      c[k]+=1
      first.setdefault(k,(i,l.rstrip()[:220]))
  for k,n in c.most_common(6):print(f,n,first[k])
open('/task/workspace/notes.txt','w').write('stage1: RN 6.24.0-4314 line9 pricing timeout 2500->800; line18 db pool 48->10. oncall suspects timeout.\n')