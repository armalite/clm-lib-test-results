import re,glob
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=[(i+1,l) for i,l in enumerate(open(f)) if re.search(r'ERROR|error|fail|429',l)]
  print(f.split('/')[-1],len(L),[i for i,_ in L][:20])
  for i,l in L[:2]:print(' ',i,l.strip()[:200])