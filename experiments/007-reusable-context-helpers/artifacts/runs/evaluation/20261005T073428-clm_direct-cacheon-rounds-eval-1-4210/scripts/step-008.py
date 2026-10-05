import json,re
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s7.obs.txt').read().splitlines()
for l in t:
  if 'board' in l[:6] or 'changes' in l[:8] or not re.search('lag',l):print(l[:130])
print(len([l for l in t if 'lag' in l]),'lag lines')