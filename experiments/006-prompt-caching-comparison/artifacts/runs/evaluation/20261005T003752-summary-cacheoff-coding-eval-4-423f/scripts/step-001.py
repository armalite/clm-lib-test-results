import os,subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace'):
  for x in f: print(r,x)
for x in os.listdir('/task/fixtures/current-tests'): print(x)
print(open('/task/workspace/invoice/__init__.py').read()[:1500])