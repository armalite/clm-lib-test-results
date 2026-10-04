import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
n=0
for i,l in enumerate(open(b+'logs/billing-svc.log'),1):
  if 'ERROR' in l:
    n+=1
    if n<4:print(i,l.rstrip())
print(n)
for i,l in enumerate(open(b+'logs/front-proxy.log'),1):
  if '503' in l:print(i,l.rstrip());break