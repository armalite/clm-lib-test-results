import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  for i,l in enumerate(open(p),1):
    if not re.search('slow query|request ok|gc|health|heartbeat',l,re.I):print(p.split('/')[-1],i,l.rstrip()[:150])