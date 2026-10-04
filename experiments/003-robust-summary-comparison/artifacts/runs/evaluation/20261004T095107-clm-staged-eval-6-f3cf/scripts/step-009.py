import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
n=0
for i,l in enumerate(open(b+'logs/billing-svc.log'),1):
  if re.search('ERROR|WARN|pool',l):
    n+=1
    if n<6:print(i,l.rstrip())
print(n)
for i,l in enumerate(open(b+'metrics/billing-svc.csv'),1):
  if i<4 or i>58:print(i,l.rstrip())