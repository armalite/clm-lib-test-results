import json
b='/task/fixtures/round-10/logs/'
for n in ['search-api.log','auth-svc.log','shipping-svc.log']:
  L=open(b+n).read().split('\n')
  for i in {'search-api.log':[1,4,7,8,20,30,50,54,60],'auth-svc.log':[10,17],'shipping-svc.log':[3,60]}[n]:print(n,i,L[i-1][:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R10: board Thread D closed false alarm (round-10/board.md:3) -> drop UPSTREAM_RATE_LIMIT; DATA_BACKFILL CLOSED (board.md:4). CHG-175 noise. Thread C search-api likely BAD_CONFIG CHG-120 (round-02/changes.md). Next: advance to R11.'})
json.dump(c,open('/task/workspace/context.json','w'))