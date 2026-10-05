import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s22.obs.txt').read().splitlines()
for l in t:
  if l.startswith(('board','changes')) or '429' not in l:print(l[:120])
print('429 lines:',[ (l.split()[0][:4],l.split()[1]) for l in t if '429' in l])