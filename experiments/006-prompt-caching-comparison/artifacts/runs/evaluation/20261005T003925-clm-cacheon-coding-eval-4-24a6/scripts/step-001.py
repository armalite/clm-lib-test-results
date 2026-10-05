import os
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for r,d,f in os.walk('/task/workspace/invoice'):print(r,f)
print(os.listdir('/task/fixtures/current-tests'))