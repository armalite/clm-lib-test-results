import os
for r,d,f in os.walk('/task/workspace'):
  print(r,f)
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for f in os.listdir('/task/workspace/exporter'):
  print(f);print(open('/task/workspace/exporter/'+f).read()[:1500])
print(open('/task/fixtures/current-tests/test_stage.py').read()[:2500])