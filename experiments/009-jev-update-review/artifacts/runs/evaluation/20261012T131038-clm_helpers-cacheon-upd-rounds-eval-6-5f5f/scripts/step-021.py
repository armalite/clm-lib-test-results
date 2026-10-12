import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R8: board round-08/board.md:3 Thread B cause revised to DISK_PRESSURE (supersedes CACHE_STAMPEDE); :4 Thread C pricing-svc failures cause unknown ongoing (suspect CHG-120 batch_size=0 round-02/changes.md:4).'})
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['pricing-svc','payments-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-08/logs/{s}.log'),1):
    if re.search(r'disk|space|ENOSPC|batch|config|ERROR|error',l,re.I): print(s,i,l.strip()[:150])