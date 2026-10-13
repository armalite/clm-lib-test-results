import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+f),1) if not re.search('slow query|request ok|gc|health|heartbeat',l,re.I)]
  print(f,len(L))
  for i,l in L[:4]:print(' ',i,l[:130])