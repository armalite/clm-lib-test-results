import re,glob
r='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(r+'logs/*')):
  ls=[(i,l) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL|429|fail|exhaust',l)]
  print(f.split('/')[-1],len(ls),[i for i,_ in ls][:12]);
  if ls:print(ls[0][1][:200])