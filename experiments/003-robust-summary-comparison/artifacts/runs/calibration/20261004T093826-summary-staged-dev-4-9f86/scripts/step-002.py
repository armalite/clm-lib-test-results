import collections,re
b='/task/fixtures/stage-1/logs/'
L=open(b+'profile-svc.log').read().splitlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[1:2]+l.split()[4:9])) for l in L)
for k,v in c.most_common(15):print(v,k[:150])
for i,l in enumerate(L,1):
 if 'ERROR' in l: print(i,l[:220]);break
G=open(b+'api-gateway.log').read().splitlines()
print(collections.Counter(re.search(r'status=(\d+)',l).group(1) if 'status=' in l else '-' for l in G))