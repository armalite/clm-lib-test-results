import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print(p,sum(1 for _ in open(p)))
print(open('/task/fixtures/round-01/board.md').read()[:2000])
for x in ['changes.md']:
  p='/task/fixtures/round-01/'+x
  if os.path.exists(p):print(open(p).read()[:1500])