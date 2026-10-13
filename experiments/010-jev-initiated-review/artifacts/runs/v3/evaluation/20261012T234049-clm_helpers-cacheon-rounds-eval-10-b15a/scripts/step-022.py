import re,glob
b='/task/fixtures/round-08/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if re.search('ERROR|WARN|FATAL|fail|429',l) and 'slow' not in l]
  print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '');
  for x in L[:2]:print(' ',x[0],x[1][:160])