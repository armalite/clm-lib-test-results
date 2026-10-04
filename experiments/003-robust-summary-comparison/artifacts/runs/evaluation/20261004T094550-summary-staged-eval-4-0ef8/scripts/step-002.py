import re,collections
b='/task/fixtures/stage-1/'
for f in ['logs/ingress-a.log','logs/payments-api.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l:
      k=re.sub(r'\d+','N',l[24:].split(']')[-1])[:80]
      c[k]+=1
      if k not in first:first[k]=(i,l.rstrip()[:180])
  for k,v in c.most_common(8):print(f,v,first[k])
