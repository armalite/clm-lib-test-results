import json,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n13','role':'note','body':'R8: Thread D closed false alarm (round-08/board.md:3) -> drop DB_POOL; but watch checkout-api CHG-113 pool_max=-4. CHG-156 PROPOSED ignore.'})
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if any(k in l.lower() for k in ['error','certificate','exhaust','invalid','disk','429','oom']): print(f.split('/')[-1],i,l.strip()[:150])