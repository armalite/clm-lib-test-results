import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:160])
import re,os
for f in sorted(os.listdir(b+'logs')):
  hits=[i for i,l in enumerate(open(b+'logs/'+f),1) if re.search(r'ERROR|SERVFAIL|expired|429|OOM|backoff',l)]
  print(f,hits[:12])
  if hits:print(open(b+'logs/'+f).readlines()[hits[0]-1][:160])