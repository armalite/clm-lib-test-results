import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip()[:250])
L=open(b+'logs/payments-api.log').read().splitlines()
n=0
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    n+=1
    if n<4:print(i,l[:200])
print('errs',n)
M=open(b+'metrics/payments-api.csv').read().splitlines()
print(M[0]);print(M[30])