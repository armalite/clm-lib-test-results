import re,glob
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i+1,l) for i,l in enumerate(open(f)) if re.search('ERROR|FATAL|SERVFAIL|429',l)]
  print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '',L[0][1][:150] if L else '')