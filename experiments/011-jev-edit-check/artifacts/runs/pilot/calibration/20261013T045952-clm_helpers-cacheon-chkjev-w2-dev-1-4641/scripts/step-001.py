import os
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/exporter'):
  for x in f: print(r,x)
print(open('/task/workspace/exporter/__init__.py').read())