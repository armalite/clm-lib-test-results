import re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|error=|SERVFAIL|429|cert|pool|OOM|disk|lag|inflight',l,re.I):print(f.split('/')[-1],i,l.strip()[:150])
print(open('/task/fixtures/round-04/board.md').read())