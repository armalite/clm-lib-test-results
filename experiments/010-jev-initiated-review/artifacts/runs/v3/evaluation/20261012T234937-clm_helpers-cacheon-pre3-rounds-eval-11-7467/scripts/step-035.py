import glob,re
b='/task/fixtures/round-09/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|FATAL|OOM|restart',l,re.I)]
  print(f.split('/')[-1],len(e),e[:2],e[-1:] if e else '')