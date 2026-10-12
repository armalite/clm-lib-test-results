import glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l: print(p.split('/')[-1],i,l.strip()[:130])