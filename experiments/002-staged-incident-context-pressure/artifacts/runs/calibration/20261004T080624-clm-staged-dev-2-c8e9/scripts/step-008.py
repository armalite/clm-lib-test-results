L=open('/task/fixtures/stage-3/logs/catalog-api.log').read().splitlines()
c=0
for i,l in enumerate(L,1):
  if '16/16' in l:
    c+=1
    if c<3: print(i,l)
print(c)