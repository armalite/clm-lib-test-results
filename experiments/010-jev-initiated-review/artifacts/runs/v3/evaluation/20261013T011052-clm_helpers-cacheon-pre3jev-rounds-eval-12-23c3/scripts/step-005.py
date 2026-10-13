import glob,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if not re.search(r'slow query',l) and re.search(r'ERROR|WARN|error|fail|429|timeout',l,re.I): print(f.split('/')[-1],i,l.rstrip()[:160])