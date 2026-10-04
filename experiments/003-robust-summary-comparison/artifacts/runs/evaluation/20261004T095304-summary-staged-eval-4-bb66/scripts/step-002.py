import collections,re
b='/task/fixtures/stage-1/logs/payments-api.log'
c=collections.Counter()
ex={}
for i,l in enumerate(open(b),1):
  if 'ERROR' in l or 'WARN' in l:
    k=re.sub(r'\d+','N',l.split(']',1)[-1])[:90]
    c[k]+=1;ex.setdefault(k,i)
for k,v in c.most_common(8):print(v,ex[k],k)