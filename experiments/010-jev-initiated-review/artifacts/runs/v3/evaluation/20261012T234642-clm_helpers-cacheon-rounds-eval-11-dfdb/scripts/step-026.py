import re
b=open('/task/fixtures/round-09/board.md').read();print(b)
import glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|429|dns|heap|mem|OOM|restart',l,re.I) and 'slow' not in l]
  print(f.split('/')[-1],len(h),h[:15]);
  if h:print(L[h[0]-1][:200])
import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))