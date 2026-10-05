import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'WARN' in l:print(f.split('/')[-1],i,l.rstrip()[:150])