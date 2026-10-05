import os
for r,d,f in os.walk('/task'):
  for x in f:print(os.path.join(r,x))
print(open('/task/fixtures/stage-1/REQUIREMENTS.md').read())
for x in os.listdir('/task/workspace/invoice'):print(x);print(open('/task/workspace/invoice/'+x).read())