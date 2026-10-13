import re,glob
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|cert|lag|pool|OOM|memory|disk|dns|ttl|miss',l,re.I): hits.append((i,l.strip()[:110]))
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h)
  if hits: print('  lines',[h[0] for h in hits][:30])