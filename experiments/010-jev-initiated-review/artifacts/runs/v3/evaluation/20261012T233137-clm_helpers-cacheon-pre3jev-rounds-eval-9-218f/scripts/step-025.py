import re,glob
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERROR|WARN|error|fail|429|SERVFAIL|expired|disk|pool|OOM|lag',l)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:2]+hits[-1:]:print(' ',i,l[:150])