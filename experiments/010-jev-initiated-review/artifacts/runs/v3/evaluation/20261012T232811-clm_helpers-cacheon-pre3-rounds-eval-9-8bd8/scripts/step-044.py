import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'].startswith('n')]
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-09/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'disk' in l) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:110])