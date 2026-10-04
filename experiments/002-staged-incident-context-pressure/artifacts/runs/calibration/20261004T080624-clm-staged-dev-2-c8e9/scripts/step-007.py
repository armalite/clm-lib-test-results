import re
print(open('/task/fixtures/stage-3/deploy/changes.log').read())
L=open('/task/fixtures/stage-3/logs/catalog-api.log').read().splitlines()
c=0
for i,l in enumerate(L,1):
  if re.search('ERROR|pool|exhaust',l):
    c+=1
    if c<6: print(i,l)
print(c)
print(open('/task/fixtures/stage-3/metrics/catalog-api.csv').read()[:600])