import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l.lower()) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board.md:3 Thread A UPSTREAM_RATE_LIMIT shipping-svc (+search-api impact) ongoing. board.md:4 OPEN DATA_BACKFILL; :5 OPEN CAPACITY_REVIEW. changes.md:3 CHG-124 APPLIED TLS ticket rotation hourly.'})
json.dump(c,open('/task/workspace/context.json','w'))