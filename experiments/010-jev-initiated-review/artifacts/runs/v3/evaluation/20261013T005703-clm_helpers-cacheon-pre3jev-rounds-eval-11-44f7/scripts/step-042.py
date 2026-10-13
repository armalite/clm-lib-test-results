import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  n=f.split('/')[-1];c=0
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'error' in l.lower():
      c+=1
      if c<=4:print(n,i,l.rstrip()[:150])
  print(n,'errors',c)