import glob
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p),1):
    if ('WARN' in l or 'ERROR' in l) and 'slow query' not in l: print(p.split('/')[-1],i,l.strip()[:120])