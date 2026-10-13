import glob,re
b='/task/fixtures/round-02/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines()
  print(f.split('/')[-1],len(L),L[0][:150])
  for i,l in enumerate(L,1):
    if re.search('ERROR|WARN|FATAL',l) and 'slow' not in l.lower(): print(i,l[:170])