import re
print(open('/task/fixtures/stage-3/deploy/changes.log').read())
L=open('/task/fixtures/stage-3/logs/quotes-api.log').read().splitlines()
n=0
for i,l in enumerate(L,1):
  if re.search(r'pool|ERROR|exhaust',l,re.I):
    n+=1
    if n<6: print(i,l[:200])
print(n)
print(open('/task/fixtures/stage-3/metrics/quotes-api.csv').read()[:600])