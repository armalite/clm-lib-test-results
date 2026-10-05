import re,glob
print(open('/task/fixtures/round-01/changes.md').read())
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'WARN|ERROR|FATAL|error|fail',l): print(f.split('/')[-1],i,l.strip()[:160])