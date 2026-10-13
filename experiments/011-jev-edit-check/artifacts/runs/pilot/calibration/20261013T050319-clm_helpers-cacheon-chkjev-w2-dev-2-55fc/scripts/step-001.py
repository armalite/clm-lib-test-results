import os
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/exporter'):
  for x in f: p=os.path.join(r,x);print(p);print(open(p).read()[:1500])
print(open('/task/fixtures/current-tests/test_stage.py').read()[:2500])