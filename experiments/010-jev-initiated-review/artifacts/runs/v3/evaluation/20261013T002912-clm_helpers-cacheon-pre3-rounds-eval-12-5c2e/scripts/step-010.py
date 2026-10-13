import re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in os.listdir(b+'logs'):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search('ERROR|WARN|FATAL|CRIT',l):print(f,i,l.rstrip()[:150])