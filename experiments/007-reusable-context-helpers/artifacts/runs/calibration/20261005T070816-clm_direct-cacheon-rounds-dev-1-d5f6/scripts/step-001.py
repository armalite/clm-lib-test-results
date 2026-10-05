import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print(p,len(open(p).read().splitlines()))
print(open('/task/fixtures/round-01/board.md').read()[:1500])
import os
p='/task/fixtures/round-01/changes.md'
if os.path.exists(p):print(open(p).read()[:1500])