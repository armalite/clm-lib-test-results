import re,os
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f'{f}:{i} {l.rstrip()[:200]}')
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).readlines()
  hits=[i for i,l in enumerate(L,1) if re.search(r'ERROR|error|429|expired|lag|fail',l)]
  if hits:print(f'{f}: {len(hits)} hits {hits[0]}-{hits[-1]} ex: {L[hits[0]-1].rstrip()[:140]}')