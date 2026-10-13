import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip()[:200])
for p in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  n=p.split('/')[-1];c=0
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|429|restart|mem|dns|kms|batch',l,re.I) and 'slow query' not in l:
      c+=1
      if c<=4:print(n,i,l.rstrip()[:160])
  print(n,'hits',c)