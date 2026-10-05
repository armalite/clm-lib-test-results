import os,subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace'):print(r,f)
print(os.listdir('/task/fixtures/current-tests'))
for r,d,f in os.walk('/task/workspace/invoice'):
  for x in f:
    if x.endswith('.py'):print(x,open(os.path.join(r,x)).read())