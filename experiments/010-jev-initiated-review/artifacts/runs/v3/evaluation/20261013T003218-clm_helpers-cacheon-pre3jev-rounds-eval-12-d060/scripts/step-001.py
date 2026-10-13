import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:print(os.path.join(r,x))
print(open(b+'board.md').read()[:1500])
c=b+'changes.md'
if os.path.exists(c):print(open(c).read()[:1000])