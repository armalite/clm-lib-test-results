import os,re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip():print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+s).read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search('ERROR|cert|ttl|lag|429|pool',l)]
  print(s,len(h),h[:8])
  if h:print('  ',L[h[0]-1][:220])