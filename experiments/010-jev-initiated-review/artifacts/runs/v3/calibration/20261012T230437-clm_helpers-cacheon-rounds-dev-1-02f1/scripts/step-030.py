import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R10: board CLOSED CAPACITY_REVIEW (round-10/board.md:3). CHG-171 APPLIED retry GET=1 (round-10/changes.md:3). 429 fx-rates checkout-api.log:6,11.'})
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-10/logs/'
for f in ['notify-worker.log','payments-svc.log','checkout-api.log','auth-svc.log','search-api.log']:
  r=[i for i,l in enumerate(open(b+f),1) if ('ERROR' in l or 'pool' in l or 'max_inflight' in l)]
  print(f,r[:12])