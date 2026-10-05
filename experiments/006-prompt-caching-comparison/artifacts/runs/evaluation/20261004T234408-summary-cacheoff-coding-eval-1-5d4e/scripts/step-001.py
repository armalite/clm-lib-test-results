import os
for r,d,f in os.walk('/task'):
  for x in f: print(os.path.join(r,x))
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/invoice'):
  for x in f: print(open(os.path.join(r,x)).read())