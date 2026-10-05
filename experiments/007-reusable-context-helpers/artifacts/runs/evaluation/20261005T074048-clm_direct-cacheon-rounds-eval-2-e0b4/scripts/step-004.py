import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(p),1):
    if re.search('ERROR|CRIT|FATAL|429|pool|expired|DNS|lag|disk|OOM|restart',l,re.I) and 'slow query' not in l:print(p.split('/')[-1],i,l.rstrip()[:160])