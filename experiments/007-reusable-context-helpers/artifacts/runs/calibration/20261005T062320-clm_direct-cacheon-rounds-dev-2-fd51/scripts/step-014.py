import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*')):
  c={}
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|error|fail|429|expired|SERVFAIL|OOM|disk|pool|invalid',l,re.I) and 'slow query' not in l:
      k=re.sub(r'\d+','#',l)[:150]
      c.setdefault(k,[]).append(i)
  for k,v in c.items():print(f.split('/')[-1],v[:4],len(v),k.strip())