import re
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  print(f);print(open(b+f).read())
L=open(b+'logs/payments-api.log').read().splitlines()
c=0
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    print(i,l);c+=1
    if c>5:break
print(open(b+'metrics/payments-api.csv').read().splitlines()[:3])
I=open(b+'logs/ingress-a.log').read().splitlines()
for i,l in enumerate(I,1):
  if '503' in l: print(i,l);break