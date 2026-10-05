import os,glob
d='/task/fixtures/round-04/'
print(open(d+'board.md').read())
for f in sorted(glob.glob(d+'logs/*.log')):
  n=os.path.basename(f);hits=[]
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: hits.append((i,l.strip()[:150]))
  print(n,len(hits),[h[0] for h in hits])
  for h in hits[:2]: print(' ',h)
print(open(d+'logs/auth-svc.log').readline()[:200])