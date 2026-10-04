import re
for l in open('/task/fixtures/stage-3/deploy/changes.log'):print(l.rstrip())
L=open('/task/fixtures/stage-3/logs/billing-svc.log').readlines()
n=0
for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
    n+=1
    if n<6:print(i,l.rstrip())
print(n)
print(open('/task/fixtures/stage-3/metrics/billing-svc.csv').readlines()[:3])