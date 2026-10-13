import re,os
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in os.listdir(b+'logs'):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if not re.search('slow query|request ok|heartbeat|gc |health ok',l)]
  print(s,len(L),L[:1],L[-1:] if L else '')