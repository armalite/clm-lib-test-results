b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
L=open(b+'logs/quotes-api.log').readlines()
n=[i for i,l in enumerate(L,1) if 'pool exhausted' in l];print(len(n),n[:5]);
if n:print(L[n[0]-1][:170])
G=open(b+'logs/api-gateway.log').readlines()
g=[i for i,l in enumerate(G,1) if 'status=5' in l];print(len(g),g[:5])
m=open(b+'metrics/quotes-api.csv').readlines();print(m[0],m[30],m[-1])