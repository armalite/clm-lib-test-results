import json,re
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
import os
for n in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+n).readlines();h=[i+1 for i,l in enumerate(L) if re.search('ERROR|429|certificate|config validation|SERVFAIL',l)]
  print(n,len(h),h[:12])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))