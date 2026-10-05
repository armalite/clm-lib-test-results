import json
b='/task/fixtures/round-08/logs/search-api.log'
s=open(b).read().splitlines()
for i,x in enumerate(s):
  if 'config' in x or '429' in x: print(i+1,x[:160])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A resolved; board.md:4 Thread B mitigated; board.md:5 Thread C search-api failures cause unknown ongoing; board.md:6 OPEN DATA_BACKFILL; board.md:7 CLOSED VENDOR_TICKET. search-api 429 lines 1,12,14,20..66; config lines 2,5,10,26..72 (round-08/logs/search-api.log) likely CHG-120 BAD_CONFIG. cert lines few (auth 8,61; shipping 50,60).'})
json.dump(c,open('/task/workspace/context.json','w'))