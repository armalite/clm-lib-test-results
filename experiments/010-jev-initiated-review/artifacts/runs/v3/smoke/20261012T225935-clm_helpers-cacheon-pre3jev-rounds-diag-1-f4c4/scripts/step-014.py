import re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if not re.search(r'request ok|gc cycle|health ok|heartbeat|slow query',l):print(f[:6],i,l.rstrip()[:110])