import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:print(os.path.join(r,x),os.path.getsize(os.path.join(r,x)))
print(open(b+'board.md').read()[:1500])
if os.path.exists(b+'changes.md'):print(open(b+'changes.md').read()[:1500])