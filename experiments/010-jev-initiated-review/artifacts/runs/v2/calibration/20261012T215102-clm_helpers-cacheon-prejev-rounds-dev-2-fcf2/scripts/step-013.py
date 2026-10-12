import re,glob
print(open('/task/fixtures/round-04/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|CRIT|SERVFAIL|429|refused|exhaust|OOM|expired|lag|disk|invalid',l,re.I) and 'slow query' not in l.lower():
      print(f.split('/')[-1],i,l.strip()[:150])