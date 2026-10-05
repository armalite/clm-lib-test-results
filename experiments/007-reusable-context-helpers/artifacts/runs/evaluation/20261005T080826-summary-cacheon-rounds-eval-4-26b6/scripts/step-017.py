import glob,re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];c={}
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search('WARN|ERROR|warn|error',l):
      k=re.sub(r'\d+','N',l[20:90]);c.setdefault(k,[]).append(i)
  for k,v in c.items():print(n,k,v[:15],len(v))