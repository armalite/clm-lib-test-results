import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  n=0
  for i,l in enumerate(open(f),1):
    if 'INFO' in l or 'slow query' in l:continue
    n+=1
    if n<=3:print(f.split('/')[-1],i,l.rstrip()[:160])
  print(f.split('/')[-1],'count',n)