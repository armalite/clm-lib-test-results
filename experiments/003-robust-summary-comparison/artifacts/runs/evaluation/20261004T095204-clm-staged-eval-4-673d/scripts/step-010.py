import re
print(open('/task/fixtures/stage-3/deploy/changes.log').read())
L=open('/task/fixtures/stage-3/logs/payments-api.log').read().splitlines()
c=0
for i,l in enumerate(L,1):
  if 'ERROR' in l and c<4: print(i,l);c+=1
m=open('/task/fixtures/stage-3/metrics/payments-api.csv').read().splitlines();print(m[0]);print(m[-1])