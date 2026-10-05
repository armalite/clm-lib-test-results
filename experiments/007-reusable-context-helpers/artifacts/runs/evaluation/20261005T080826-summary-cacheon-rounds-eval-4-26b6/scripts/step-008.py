import glob,os
r='/task/fixtures/round-03/'
print(open(r+'board.md').read())
for f in sorted(glob.glob(r+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('WARN' in l or 'ERROR' in l) and 'slow query' not in l: print(os.path.basename(f)[:6],i,l.strip()[20:110])