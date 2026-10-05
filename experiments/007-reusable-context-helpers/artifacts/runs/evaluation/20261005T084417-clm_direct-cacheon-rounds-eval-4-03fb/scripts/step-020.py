import re,glob
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|pool|miss|memory|OOM|cert|dns|disk|lag',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:110])