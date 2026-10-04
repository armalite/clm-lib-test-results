b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.strip()[:200])
L=open(b+'logs/returns-svc.log').readlines()
n=0
for i,l in enumerate(L,1):
 if 'ERROR' in l and 'pool' in l:
  n+=1
  if n<3:print(i,l.strip()[:160])
print('poolerr',n)
for i,l in enumerate(open(b+'logs/edge-gw.log'),1):
 if 'status=503' in l:print('edge',i,l.strip()[:120]);break