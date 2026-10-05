import glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p),1):
    if ('WARN' in l or 'ERROR' in l) and 'slow query' not in l: print(p.split('/')[-1][:6],i,l.strip()[21:110])