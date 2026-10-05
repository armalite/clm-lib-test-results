import os
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace'):
  for x in f: print(os.path.join(r,x))
for r,d,f in os.walk('/task/fixtures/current-tests'):
  for x in f: print(os.path.join(r,x))
print(open('/task/workspace/invoice/__init__.py').read())