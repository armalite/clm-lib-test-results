import re,glob
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
  L=[i+1 for i,l in enumerate(open(f)) if re.search(r'certificate_expired|max_inflight|SERVFAIL|429',l)]
  print(f.split('/')[-1],L[:15])