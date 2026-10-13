import re,glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
k=re.compile(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert|inflight',re.I)
for f in sorted(glob.glob(b+'logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if 'slow query' in l:continue
    if k.search(l):
      n+=1
      if n<=4:print(f.split('/')[-1],i,l.rstrip()[:160])
  print(f.split('/')[-1],'hits',n)