import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip())
for i,l in enumerate(open('/task/fixtures/round-08/board.md'),1):print('b8',i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-09/logs/*')):
  for i,l in enumerate(open(p),1):
    if re.search('ERROR|429|max_inflight|certificate|SERVFAIL',l) and 'slow query' not in l:print(p[-16:],i,l.rstrip()[:110])