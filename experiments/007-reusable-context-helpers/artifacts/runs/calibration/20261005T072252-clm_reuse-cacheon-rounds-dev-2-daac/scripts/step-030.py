import re,glob
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=[(i+1,l) for i,l in enumerate(open(f)) if re.search('ERROR|error|429|fail',l)]
  print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '')
  for i,l in L[:2]: print(' ',i,l.strip()[:150])