import re,glob
for f in ['board.md','changes.md']:
 print(f);[print(i+1,l.rstrip()) for i,l in enumerate(open('/task/fixtures/round-05/'+f))]
for p in sorted(glob.glob('/task/fixtures/round-05/logs/*')):
 n=p.split('/')[-1];hits=[]
 for i,l in enumerate(open(p)):
  if re.search(r'ERROR|FATAL|CRIT|error=|SERVFAIL|cert|429|OOM|pool',l,re.I) and 'slow query' not in l: hits.append((i+1,l.strip()[:150]))
 print(n,len(hits));[print(h) for h in hits[:4]];print([h[0] for h in hits])