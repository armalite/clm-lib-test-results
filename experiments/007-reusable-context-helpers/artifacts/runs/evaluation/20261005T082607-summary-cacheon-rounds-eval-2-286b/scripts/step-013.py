import os,re
b='/task/fixtures/round-05/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  print(f,'first:',L[0][:90])
  c={}
  for i,l in enumerate(L,1):
    if ('ERROR' in l or 'WARN' in l or 'heap' in l) and 'slow query' not in l:
      k=re.sub(r'\d+','#',l[21:])[:70];c.setdefault(k,[]).append(i)
  for k,v in c.items():print(' ',k,v[:3],v[-1],len(v))