import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print(p)
print(open('/task/fixtures/round-01/board.md').read()[:1500])
for x in os.listdir('/task/fixtures/round-01/logs'):
  L=open('/task/fixtures/round-01/logs/'+x).read().splitlines()
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l: print(x,i,l[:150])