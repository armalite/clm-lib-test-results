import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  n=p.split('/')[-1];c={}
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|error|429|expired|fail',l):
      k=re.sub(r'\d+','#',l[20:90]);c.setdefault(k,[]).append(i)
  for k,v in c.items():print(n,len(v),v[:4],k)