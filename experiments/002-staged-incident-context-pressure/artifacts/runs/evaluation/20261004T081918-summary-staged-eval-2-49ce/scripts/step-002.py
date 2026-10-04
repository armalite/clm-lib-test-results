import collections,re
b='/task/fixtures/stage-1/'
for f in ['logs/ingress-a.log','logs/payments-api.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or ' 5' in l[20:80]:
      k=re.sub(r'\d+','N',l[24:])[:90]
      c[k]+=1;first.setdefault(k,i)
  for k,v in c.most_common(8):print(f,first[k],v,k)
open('/task/workspace/notes.txt','w').write('s1: RN 5.36.1 line13 risk timeout 2500->800; line16 pool 60->14; deploy 08:18:43 deploys.log:4\n')