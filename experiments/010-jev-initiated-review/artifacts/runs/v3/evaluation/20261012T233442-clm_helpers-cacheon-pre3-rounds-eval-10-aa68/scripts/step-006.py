import re,glob
print(open('/task/fixtures/round-02/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if not re.search(r'slow query',l) and re.search(r'ERROR|WARN|FATAL|error',l): print(f.split('/')[-1],i,l.strip()[:150])