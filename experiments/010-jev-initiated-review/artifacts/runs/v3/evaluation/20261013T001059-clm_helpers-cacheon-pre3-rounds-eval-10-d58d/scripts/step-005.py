import glob
r='/task/fixtures/round-02/'
print(open(r+'board.md').read())
for f in sorted(glob.glob(r+'logs/*')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or ('WARN' in l and 'slow query' not in l): print(f.split('/')[-1],i,l.strip()[:160])