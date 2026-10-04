import re,collections
L=open('/task/fixtures/stage-1/logs/quotes-api.log').readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[4:])[:70]) for l in L if 'ERROR' in l or 'WARN' in l)
for k,v in c.most_common(8):print(v,k)
for i,l in enumerate(L):
  if 'pool' in l and 'ERROR' in l: print(i+1,l.strip()[:220]);break
for i,l in enumerate(L):
  if 'risk-score' in l and 'ERROR' in l: print(i+1,l.strip()[:220]);break