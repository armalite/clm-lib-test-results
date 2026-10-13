import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines();n=f.split('/')[-1]
  c={}
  for i,l in enumerate(L,1):
    if re.search('ERROR|WARN|FATAL|err',l):
      k=re.sub(r'[0-9:.TZ-]{6,}|\d+','#',l)[:90]
      c.setdefault(k,[]).append(i)
  for k,v in c.items():print(n,v[0],v[-1],len(v),k)