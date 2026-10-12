import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|pool|cert|disk|config',l,re.I) and 'slow' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board.md:3 Thread D DB_POOL_EXHAUSTED checkout-api ongoing (likely really BAD_CONFIG_ROLLOUT via CHG-113 pool_max=-4, round-01/changes.md:4); changes.md:3 CHG-147 dashboards noise.'})
json.dump(c,open('/task/workspace/context.json','w'))