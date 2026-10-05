import glob
b='/task/fixtures/round-04/'
for n in ['board.md','changes.md']:
  for i,l in enumerate(open(b+n).read().splitlines(),1):print(n,i,l)
for f in sorted(glob.glob(b+'logs/*')):
  c={}
  for i,l in enumerate(open(f).read().splitlines(),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l.lower()) and 'slow query' not in l:
      p=l.split(None,3);k=p[3][:60] if len(p)>3 else l[:60]
      c.setdefault(k,[]).append(i)
  for k,v in c.items():print(f.split('/')[-1],v[:8],len(v),k)
  if not c: print(f.split('/')[-1],'first:',open(f).readline()[:120])