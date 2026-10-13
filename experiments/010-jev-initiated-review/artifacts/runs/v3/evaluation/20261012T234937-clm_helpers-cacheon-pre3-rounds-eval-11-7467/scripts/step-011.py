import glob,re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|CRIT',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])