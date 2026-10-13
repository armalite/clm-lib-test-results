import re,glob
print(open('/task/fixtures/round-12/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-12/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|SERVFAIL|validation',l): print(f.split('/')[-1],i,l.strip()[:90])