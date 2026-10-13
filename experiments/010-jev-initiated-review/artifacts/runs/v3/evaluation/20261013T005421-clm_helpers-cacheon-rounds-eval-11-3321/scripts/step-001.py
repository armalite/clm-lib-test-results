import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:print(os.path.join(r,x),sum(1 for _ in open(os.path.join(r,x))))
print(open(b+'board.md').read()[:2000])
import glob
for p in glob.glob(b+'changes.md'):print(open(p).read()[:1500])