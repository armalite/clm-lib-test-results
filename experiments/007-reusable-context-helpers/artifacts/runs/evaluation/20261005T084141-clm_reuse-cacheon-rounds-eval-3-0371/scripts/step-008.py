import re,glob
for f in ['board.md','changes.md']:
  print(f);print(open('/task/fixtures/round-03/'+f).read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|WARN',l) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:150])