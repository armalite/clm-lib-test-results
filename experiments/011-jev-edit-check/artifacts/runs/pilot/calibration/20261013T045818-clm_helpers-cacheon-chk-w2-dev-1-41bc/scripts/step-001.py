import os
for r,d,f in os.walk('/task/fixtures'):print(r,f)
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/exporter'):
  for x in f:print(x,open(os.path.join(r,x)).read())