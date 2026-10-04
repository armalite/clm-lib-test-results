p='/task/fixtures/stage-3/'
for i,l in enumerate(open(p+'deploy/changes.log'),1):print(i,l.strip()[:250])
c=0
for i,l in enumerate(open(p+'logs/payments-api.log'),1):
  if 'pool exhausted' in l:
    c+=1
    if c<3:print(i,l.strip()[:160])
print('count',c)
m=open(p+'metrics/payments-api.csv').read().splitlines();print(m[0]);print(m[1]);print(m[30])