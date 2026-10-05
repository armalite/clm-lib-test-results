import os,subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/invoice'):
  for x in f: p=os.path.join(r,x);print(p);print(open(p).read()[:1500])
print(os.listdir('/task/fixtures/current-tests'))