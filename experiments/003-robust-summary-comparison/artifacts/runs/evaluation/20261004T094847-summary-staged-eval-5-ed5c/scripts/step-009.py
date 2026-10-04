b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
n=0
for i,l in enumerate(open(b+'logs/quotes-api.log'),1):
  if 'pool' in l:
    n+=1
    if n<4:print(i,l[:150].rstrip())
print(n)
n=0
for i,l in enumerate(open(b+'logs/ingress-a.log'),1):
  if 'status=503' in l:
    n+=1
    if n<3:print(i,l[:120].rstrip())
print(n)
L=open(b+'metrics/quotes-api.csv').readlines();print(L[0],L[30],L[-1])