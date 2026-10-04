import collections,re
b='/task/fixtures/stage-1/logs/billing-svc.log'
L=open(b).readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[1:2]+l.split()[4:9])) for l in L)
for k,v in c.most_common(15):print(v,k)
for i,l in enumerate(L,1):
 if 'ERROR' in l:print(i,l.strip()[:180]);break