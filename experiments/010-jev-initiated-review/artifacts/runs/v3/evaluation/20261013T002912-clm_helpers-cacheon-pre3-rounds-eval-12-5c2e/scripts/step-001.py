import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:
    p=os.path.join(r,x);L=open(p).read().splitlines()
    print(p,len(L))
print(open(b+'board.md').read()[:1500])
if os.path.exists(b+'changes.md'):print(open(b+'changes.md').read()[:1000])