import os
for r,d,f in os.walk('/task/fixtures'):
  for x in f:print(os.path.join(r,x))
for r,d,f in os.walk('/task/workspace/invoice'):
  for x in f:print(os.path.join(r,x))
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
import glob
for p in glob.glob('/task/workspace/invoice/*.py'):print(p,open(p).read())