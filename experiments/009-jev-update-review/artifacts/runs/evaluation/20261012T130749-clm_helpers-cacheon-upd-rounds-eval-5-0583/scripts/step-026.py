import json,glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    for i,l in enumerate(open(f),1):
        s=l.lower()
        if any(k in s for k in ['error','invalid','exhaust','certificate','disk','pool_max','fatal']) and 'slow' not in s:
            print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))