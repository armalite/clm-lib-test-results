import re,glob
print(open('/task/fixtures/round-03/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|SERVFAIL|cert|OOM|disk|lag|pool',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])