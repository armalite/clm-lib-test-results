import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1): print(f,i,l.strip()[:200])
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if re.search('ERROR|FATAL|429|lag|expired|ttl',l,re.I): print(p.split('/')[-1],i,l.strip()[:150])