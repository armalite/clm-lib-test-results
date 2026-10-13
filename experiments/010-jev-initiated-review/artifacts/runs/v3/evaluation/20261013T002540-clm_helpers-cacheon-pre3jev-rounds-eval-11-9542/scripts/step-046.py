import re,glob
print(open('/task/fixtures/round-12/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-12/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|dns|batch|resolv',l,re.I) and 'slow query' not in l: print(f[-20:],i,l.strip()[:120])