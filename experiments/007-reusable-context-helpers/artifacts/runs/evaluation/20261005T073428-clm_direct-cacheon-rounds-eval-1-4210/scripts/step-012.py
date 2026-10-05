import re,glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|cert|dns|ttl|stamped|miss|oom|disk|pool',l,re.I):print(f.split('/')[-1],i,l.rstrip()[:150])
