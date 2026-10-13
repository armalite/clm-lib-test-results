import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'error' in l.lower() and 'slow' not in l:print(f.split('/')[-1],i,l.rstrip()[:150])