import re,glob
print(open('/task/fixtures/round-10/board.md').read());print(open('/task/fixtures/round-10/changes.md').read())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|CRIT|SERVFAIL|429|refused|exhaust|OOM|expired|lag|disk|invalid|validation',l) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:110])