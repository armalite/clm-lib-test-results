import re,glob
b='/task/fixtures/round-08/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines();e=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|FATAL|level=E',l)]
  print(f[-20:],len(e),e[:1],e[-1:],L[e[0]-1][:160] if e else '')