import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search(r'ERROR|429|restart|mem|OOM|SERVFAIL|batch',l,re.I): print(f.split('/')[-1],i,l.strip()[:110])