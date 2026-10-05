import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  c={}
  for i,l in enumerate(open(f),1):
    if re.search('WARN|ERROR|429|pool|miss|memory|cert|dns|disk|lag',l,re.I):
      k=re.sub(r'[0-9:.TZ-]{6,}|\d+','#',l)[:90];c.setdefault(k,[]).append(i)
  for k,v in c.items():print(f.split('/')[-1],v[:8],len(v),k.strip())