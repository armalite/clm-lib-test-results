import os,glob
d='/task/fixtures/round-06/'
for i,l in enumerate(open(d+'board.md'),1):print(i,l.rstrip())
for i,l in enumerate(open(d+'changes.md'),1):print(i,l.rstrip())
out=[]
for f in sorted(glob.glob(d+'logs/*.log')):
  n=os.path.basename(f);hits=[]
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l: hits.append((i,l.strip()[:130]))
  print(n,len(hits),[h[0] for h in hits])
  for h in hits[:1]: print(' ',h)
  out.append(n+' '+str([h[0] for h in hits]))
open('/task/workspace/notes.md','a').write('R6 logs: '+'; '.join(out)+'\n')
