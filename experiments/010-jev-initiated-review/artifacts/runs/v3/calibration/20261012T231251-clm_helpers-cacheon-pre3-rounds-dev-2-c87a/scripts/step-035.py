import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|uptime|429|SERVFAIL|cert',l) and 'slow' not in l.lower():
      print(f.split('/')[-1],i,l.strip()[:150])