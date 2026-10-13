import os
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace'):
  for x in f: print(os.path.join(r,x))
print(open('/task/fixtures/current-tests/test_stage.py').read()[:2500])