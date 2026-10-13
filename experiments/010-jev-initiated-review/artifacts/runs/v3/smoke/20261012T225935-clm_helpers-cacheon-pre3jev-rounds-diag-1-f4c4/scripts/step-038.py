import re
print(open('/task/fixtures/round-09/board.md').read())
import os
for f in sorted(os.listdir('/task/fixtures/round-09/logs')):
  for i,l in enumerate(open('/task/fixtures/round-09/logs/'+f),1):
    if not re.search(r'slow query|request ok|gc|health|heartbeat',l,re.I) and re.search(r'ERR|WARN|error|fail|429|cert|dns|disk|lag|pool|heap|miss',l,re.I):
      print(f,i,l.strip()[:150])