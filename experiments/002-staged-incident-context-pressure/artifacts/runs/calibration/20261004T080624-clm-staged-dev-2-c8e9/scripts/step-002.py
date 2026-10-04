import collections,re
b='/task/fixtures/stage-1/logs/catalog-api.log'
L=open(b).readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[1:2]+l.split()[4:9])) for l in L if 'ERROR' in l)
print(c.most_common(8))
for i,l in enumerate(L,1):
  if 'ERROR' in l and i>100:print(i,l.rstrip()[:180]);break