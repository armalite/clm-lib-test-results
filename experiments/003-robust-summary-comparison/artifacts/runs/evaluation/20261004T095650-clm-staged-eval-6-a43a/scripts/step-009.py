L=open('/task/fixtures/stage-3/logs/billing-svc.log').readlines()
c=0
for i,l in enumerate(L,1):
  if 'exhausted' in l and '16/16' in l:
    c+=1
    if c<3:print(i,l.rstrip())
print(c)