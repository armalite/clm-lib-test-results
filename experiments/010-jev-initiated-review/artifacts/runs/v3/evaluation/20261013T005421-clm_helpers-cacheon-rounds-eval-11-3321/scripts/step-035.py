import re,glob
print(open('/task/fixtures/round-12/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-12/logs/*.log')):
  hits=[i for i,l in enumerate(open(f),1) if re.search(r'429|dns|config validation|heap|cert|ERROR',l,re.I) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits),hits[:1],hits[-1:])