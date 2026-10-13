import collections
L=open('/task/fixtures/round-04/logs/shipping-svc.log').read().splitlines()
print(len(L))
for i in (0,1,len(L)//2):print(i+1,L[i][:200])
for i,l in enumerate(L,1):
  if any(k in l.lower() for k in ('err','fail','exhaust','conn','disk')):print(i,l[:160])