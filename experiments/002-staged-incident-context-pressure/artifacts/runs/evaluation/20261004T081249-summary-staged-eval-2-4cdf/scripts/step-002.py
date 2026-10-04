import re,collections
b='/task/fixtures/stage-1/'
for f in ['logs/ingress-a.log','logs/payments-api.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l:
      k=re.sub(r'\d+','N',l[24:].split(']',1)[-1])[:70]
      c[k]+=1;first.setdefault(k,i)
  for k,v in c.most_common(8):print(f,first[k],v,k)
open('/task/workspace/notes.txt','w').write('S1: deploy 5.36.1-f33d deploys.log:4; RN line13 risk timeout 2500->800; line16 pool 60->14. oncall suspects timeout.\n')