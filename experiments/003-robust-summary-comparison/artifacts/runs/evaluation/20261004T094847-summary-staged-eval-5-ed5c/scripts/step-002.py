import re,collections
b='/task/fixtures/stage-1/logs/quotes-api.log'
L=open(b).read().splitlines()
c=collections.Counter(re.sub(r'[0-9]+','N',l[25:])[:90] for l in L if 'ERROR' in l or 'WARN' in l)
for k,v in c.most_common(8):print(v,k)
for i,l in enumerate(L,1):
  if 'ERROR' in l:print(i,l[:200]);break