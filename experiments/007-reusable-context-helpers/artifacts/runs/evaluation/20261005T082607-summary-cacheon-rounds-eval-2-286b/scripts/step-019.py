import os,re
b='/task/fixtures/round-07/'
out=[]
for fn in ['board.md','changes.md']:
  for i,l in enumerate(open(b+fn),1):out.append(f'{fn} {i} {l.rstrip()}')
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  out.append(f+' first: '+L[0][:80])
  c={}
  for i,l in enumerate(L,1):
    if ('ERROR' in l or 'WARN' in l or 'heap' in l or 'error' in l) and 'slow query' not in l:
      k=re.sub(r'\d+','#',l[21:])[:70];c.setdefault(k,[]).append(i)
  for k,v in c.items():out.append(f'  {k} {v[:3]} {v[-1]} {len(v)}')
s='\n'.join(out);print(s)
open('/task/workspace/notes.md','a').write('\nR7 raw:\n'+s+'\n')