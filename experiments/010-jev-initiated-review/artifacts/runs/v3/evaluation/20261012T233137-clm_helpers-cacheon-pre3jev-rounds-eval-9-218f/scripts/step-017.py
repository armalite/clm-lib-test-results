import re,glob
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|fail|SERVFAIL|429|pool|timeout|mem|disk|lag',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:3]+hits[-1:]: print(i,l[:160])