import re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|FATAL|CRIT|429|timeout|exhaust|expired|NXDOMAIN|OOM|disk|lag|ttl',l,re.I):print(p.split('/')[-1],i,l.rstrip()[:160])