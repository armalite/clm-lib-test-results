import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f).read().splitlines(),1):print(f,i,l[:200])
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f).read().splitlines(),1):
    if re.search(r'ERROR|FATAL|WARN',l) and 'slow' not in l.lower():print(f.split('/')[-1],i,l[:150])