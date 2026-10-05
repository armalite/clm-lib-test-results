import os,re
b='/task/fixtures/round-08/'
out=[]
for fn in ['board.md','changes.md']:
  for i,l in enumerate(open(b+fn),1):out.append(f'{fn} {i} {l.rstrip()[:200]}')
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  c={}
  for i,l in enumerate(L,1):
    if ('ERROR' in l or 'WARN' in l or 'heap' in l) and 'slow qu' not in l:
      k=re.sub(r'\d+','#',l[21:])[:90];c.setdefault(k,[]).append(i)
  for k,v in c.items():out.append(f'{f} {k} {v[0]}-{v[-1]} {len(v)}')
s='\n'.join(out);print(s)
open('/task/workspace/notes.md','a').write('\nR8 raw:\n'+s+'\n')