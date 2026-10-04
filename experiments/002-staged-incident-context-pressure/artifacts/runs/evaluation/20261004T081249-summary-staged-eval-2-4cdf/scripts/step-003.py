import re,collections
b='/task/fixtures/stage-1/'
for f in ['logs/ingress-a.log','logs/payments-api.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l:
      k=re.sub(r'req=\S+','',re.sub(r'\d+','N',l[24:].split(']',1)[-1]))[:80].strip()
      c[k]+=1;first.setdefault(k,i)
  for k,v in c.most_common(6):print(f,first[k],v,k)
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'risk-score' in l and 'ERROR' not in l:print(i,l.rstrip()[:160]);break
open('/task/workspace/notes.txt','a').write('S1 errors: payments-api.log:179 first risk-score timeout.\n')