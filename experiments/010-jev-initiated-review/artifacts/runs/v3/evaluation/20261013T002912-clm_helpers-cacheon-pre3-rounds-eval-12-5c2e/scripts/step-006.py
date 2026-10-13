import re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in os.listdir(b+'logs'):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if not re.search(r'slow query|heartbeat',l) and re.search(r'ERROR|WARN|error|fail|429|expired|pool|lag|OOM|disk|ttl',l,re.I):print(f,i,l.rstrip()[:160])