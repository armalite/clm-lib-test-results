import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|SERVFAIL|cert|429|OOM|pool|lag|disk|invalid|max_inflight',l,re.I) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:150])