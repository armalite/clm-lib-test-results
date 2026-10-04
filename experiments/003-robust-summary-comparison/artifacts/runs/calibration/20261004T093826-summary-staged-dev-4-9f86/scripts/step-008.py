b='/task/fixtures/stage-3/'
c=0
for i,l in enumerate(open(b+'logs/profile-svc.log'),1):
  if '22/22' in l:
    c+=1
    if c<3:print(i,l.rstrip())
print(c)
c=0
for i,l in enumerate(open(b+'logs/api-gateway.log'),1):
  if 'status=503' in l and l[11:16]>'10:52':
    c+=1
    if c<2:print(i,l.rstrip()[:120])
print(c)