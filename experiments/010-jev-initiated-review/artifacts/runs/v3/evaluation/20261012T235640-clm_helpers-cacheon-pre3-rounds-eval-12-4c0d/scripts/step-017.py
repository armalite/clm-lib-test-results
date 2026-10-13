import re,glob
b='/task/fixtures/round-04/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|cert|429|dns|pool|disk|oom|memory|lag|stampede|ttl',l,re.I): print(f.split('/')[-1],i,l.strip()[:120])