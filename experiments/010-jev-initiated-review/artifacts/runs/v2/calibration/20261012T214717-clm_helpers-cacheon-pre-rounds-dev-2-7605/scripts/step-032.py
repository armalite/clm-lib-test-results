import re
print(open('/task/fixtures/round-07/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|error|fail|expired|429|SERVFAIL|max_inflight',l) and 'heartbeat' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])