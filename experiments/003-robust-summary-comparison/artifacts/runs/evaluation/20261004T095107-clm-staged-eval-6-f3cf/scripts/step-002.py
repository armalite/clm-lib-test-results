import collections,re
b='/task/fixtures/stage-1/logs/'
L=open(b+'billing-svc.log').readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[1:2]+l.split()[4:9])) for l in L if 'INFO' not in l)
for k,v in c.most_common(12):print(v,k)
for i,l in enumerate(L,1):
  if 'pool' in l or 'timeout' in l.lower():print(i,l.rstrip()[:170]);break
for i,l in enumerate(L,1):
  if i>400 and ('pool' in l or 'timed out' in l):print(i,l.rstrip()[:170]);break