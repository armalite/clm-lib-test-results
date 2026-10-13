import glob,re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];c={}
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|WARN|error|warn',l) and 'slow' not in l.lower():
      k=re.sub(r'\d+','#',l.strip())[-90:];c.setdefault(k,[]).append(i)
  for k,v in c.items():print(n,v[0],v[-1],len(v),k)