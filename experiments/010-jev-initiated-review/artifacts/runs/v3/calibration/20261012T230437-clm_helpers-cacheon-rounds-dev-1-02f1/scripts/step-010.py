import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  n=f.split('/')[-1];hits=[]
  for i,l in enumerate(open(f),1):
    if 'INFO' not in l and 'slow query' not in l: hits.append((i,l.rstrip()[:150]))
  print(n,len(hits))
  for h in hits[:4]:print(' ',h)
  if hits:print('  lines',[h[0] for h in hits])