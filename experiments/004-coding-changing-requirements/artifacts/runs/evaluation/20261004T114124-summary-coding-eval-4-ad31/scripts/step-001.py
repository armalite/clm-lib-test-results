import os
for r,d,f in os.walk('/task'):
  for x in f: print(os.path.join(r,x))
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
import glob
for p in glob.glob('/task/workspace/invoice/*'): print(p);print(open(p).read())