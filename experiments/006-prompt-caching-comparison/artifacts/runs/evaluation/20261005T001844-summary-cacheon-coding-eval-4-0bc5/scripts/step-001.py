import os,subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace'):
  for x in f: print(r,x)
print(os.listdir('/task/fixtures/current-tests'))