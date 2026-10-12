import os,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|FATAL|WARN',l) and not re.search(r'slow query|gc|heartbeat',l):print(f,i,l.rstrip()[:150])