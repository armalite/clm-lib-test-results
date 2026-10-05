import glob,re
b='/task/fixtures/round-08/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
import os
if os.path.exists(b+'changes.md'):
  for i,l in enumerate(open(b+'changes.md'),1):print('chg',i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];c={}
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search('WARN|ERROR|warn|error',l):
      k=re.sub(r'\d+','N',l[20:90]);c.setdefault(k,[]).append(i)
  for k,v in c.items():print(n,k,v[:15],len(v))