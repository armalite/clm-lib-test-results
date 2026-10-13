import os,re
R='/task/fixtures/round-02'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(f'{R}/{f}'),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(R+'/logs')):
  for i,l in enumerate(open(f'{R}/logs/{f}'),1):
    if not re.search(r'heartbeat|health ok|gc cycle|slow query|request ok',l):print(f'{f}:{i} {l.strip()[:140]}')