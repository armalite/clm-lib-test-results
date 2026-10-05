import os
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/invoice'):print(r,f)
for f in os.listdir('/task/fixtures/current-tests'):print(f)
print(open('/task/workspace/invoice/__init__.py').read()[:1500])