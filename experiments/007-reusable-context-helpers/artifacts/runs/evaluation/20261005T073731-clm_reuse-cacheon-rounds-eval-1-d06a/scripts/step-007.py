import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  n=p.split('/')[-1];c=0
  for i,l in enumerate(open(p),1):
    if 'INFO' in l or 'slow' in l.lower():continue
    c+=1
    if c<=6:print(n,i,l.rstrip()[:150])
  print(n,'nonnoise',c)