import collections,re
b='/task/fixtures/stage-1/logs/quotes-api.log'
L=open(b).readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[4:9])) for l in L if 'INFO' not in l)
for k,v in c.most_common(12):print(v,k)
for i,l in enumerate(L,1):
  if 'pool' in l or 'timeout' in l:
    print(i,l.strip()[:180]);break
for i,l in enumerate(open('/task/fixtures/stage-1/logs/ingress-a.log'),1):
  if ' 50' in l:print(i,l.strip()[:180]);break