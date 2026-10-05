import os,re
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search('ERROR|FATAL|fail|expired',l)]
  print(f,len(h),h[:10])
  if h:print('  ',L[h[0]-1][:200])