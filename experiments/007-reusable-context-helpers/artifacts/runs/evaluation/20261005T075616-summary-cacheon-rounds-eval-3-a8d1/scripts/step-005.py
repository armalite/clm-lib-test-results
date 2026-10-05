import glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  c={}
  for i,l in enumerate(open(f).read().splitlines(),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:
      k=l.split(None,3)[3][:60] if len(l.split(None,3))>3 else l
      c.setdefault(k,[]).append(i)
  for k,v in c.items():print(f.split('/')[-1],v[:8],len(v),k)