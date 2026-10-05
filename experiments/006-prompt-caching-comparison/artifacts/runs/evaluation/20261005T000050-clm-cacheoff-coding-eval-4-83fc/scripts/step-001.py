import os
for r,d,f in os.walk('/task/fixtures'):
  for x in f:print(os.path.join(r,x))
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/invoice'):
  for x in f:p=os.path.join(r,x);print(p);print(open(p).read())