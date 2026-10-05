import re,glob
b='/task/fixtures/round-09/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|429|heap|rss',l)]
  print(f.split('/')[-1],len(hits),hits[:4])