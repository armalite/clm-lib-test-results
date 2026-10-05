import os,subprocess
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace'):print(r,f)
print(os.listdir('/task/fixtures/current-tests'))
print(open('/task/workspace/invoice/__init__.py').read()[:1500])