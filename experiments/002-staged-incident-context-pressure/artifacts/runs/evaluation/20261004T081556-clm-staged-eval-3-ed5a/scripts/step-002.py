import re,collections
b='/task/fixtures/stage-1/logs/returns-svc.log'
c=collections.Counter()
ex={}
for i,l in enumerate(open(b),1):
 if 'ERROR' in l:
  k=re.sub(r'[\d.]+','N',l[40:])[:90];c[k]+=1;ex.setdefault(k,i)
for k,v in c.most_common(8):print(v,ex[k],k)