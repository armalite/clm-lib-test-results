import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:print(f.split('/')[-1],i,l.rstrip()[:150])