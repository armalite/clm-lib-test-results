import re,glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|error|warn',l) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:150])