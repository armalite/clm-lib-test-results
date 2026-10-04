import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
n=0
for i,l in enumerate(open(b+'logs/returns-svc.log'),1):
  if re.search('pool|ERROR',l,re.I):
    n+=1
    if n<6:print(i,l.rstrip())
print(n)
print(open(b+'metrics/returns-svc.csv').readlines()[:3])