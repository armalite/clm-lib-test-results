import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  n=0
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or '429' in l or 'FATAL' in l) and 'slow query' not in l:
      n+=1
      if n<=3:print(p.split('/')[-1],i,l.rstrip()[:160])
  print(p.split('/')[-1],'count',n)