b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip()[:220])
L=open(b+'logs/shipping-api.log').readlines()
n=[i for i,l in enumerate(L,1) if 'pool exhausted' in l]
print(len(n),n[:3]);print(L[n[0]-1][:170] if n else '')
n2=[i for i,l in enumerate(L,1) if 'timed out' in l];print(len(n2),n2[:3])