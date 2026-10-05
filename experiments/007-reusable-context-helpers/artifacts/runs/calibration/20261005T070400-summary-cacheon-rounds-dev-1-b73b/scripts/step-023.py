import os,re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
noise=re.compile(r'slow query|heartbeat|health ok|gc cycle|request ok')
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if not noise.search(l)]
  print(f,len(L))
  for x in L[:4]: print(x)
  if L: print('last',L[-1])