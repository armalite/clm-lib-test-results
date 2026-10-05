import os,re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
noise=re.compile(r'slow query|heartbeat|health ok|gc cycle|request ok')
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if not noise.search(l) and not re.search(r' (INFO|DEBUG) ',l)]
  print(f,len(h))
  for x in h[:4]: print(x)
  if len(h)>4: print('last',h[-1])
  if not h: print('first',L[0][:110])
