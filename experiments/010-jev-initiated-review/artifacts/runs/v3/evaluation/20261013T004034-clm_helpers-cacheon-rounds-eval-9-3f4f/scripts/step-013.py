import re,glob
r='/task/fixtures/round-05/'
for i,l in enumerate(open(r+'board.md'),1):print('board',i,l.rstrip())
pat=re.compile(r'heartbeat|health ok|request ok|gc cycle|slow query',re.I)
for f in sorted(glob.glob(r+'logs/*.log')):
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not pat.search(l)]
  n=f.split('/')[-1]
  print(n,len(hits),'first',hits[:2],'last',hits[-1:] if hits else '')
  kinds={}
  for i,l in hits:
    k=re.sub(r'[0-9]+','#',l)[-60:];kinds.setdefault(k,[]).append(i)
  for k,v in list(kinds.items())[:4]:print('  ',v[0],v[-1],len(v),k)