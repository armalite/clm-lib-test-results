import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
c=0
for i,l in enumerate(open(b+'logs/profile-svc.log'),1):
  if 'pool' in l:
    c+=1
    if c<4:print(i,l.rstrip())
print(c)
for i,l in enumerate(open(b+'metrics/profile-svc.csv'),1):
  if i<3:print(i,l.rstrip())