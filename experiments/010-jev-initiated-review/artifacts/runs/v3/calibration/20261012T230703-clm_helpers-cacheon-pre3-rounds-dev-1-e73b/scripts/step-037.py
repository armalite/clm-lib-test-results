import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  L=[i for i,l in enumerate(open(f),1) if re.search('ERROR|429|exhaust|validation|fail',l)]
  print(f[-20:],len(L),L[:3],L[-2:])
for i,l in enumerate(open('/task/fixtures/round-06/board.md'),1):print(i,l.rstrip())