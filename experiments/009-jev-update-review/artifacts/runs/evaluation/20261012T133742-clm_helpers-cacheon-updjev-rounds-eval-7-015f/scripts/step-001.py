import os
for r,d,f in os.walk('/task/fixtures'):
  for x in f:print(os.path.join(r,x))
print(open('/task/fixtures/round-01/board.md').read()[:1500])
p='/task/fixtures/round-01/changes.md'
if os.path.exists(p):print(open(p).read()[:1000])