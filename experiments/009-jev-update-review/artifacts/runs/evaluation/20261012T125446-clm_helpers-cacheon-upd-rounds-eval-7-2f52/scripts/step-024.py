import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n8': x['body']='R8: board.md:3 Thread B (CACHE_STAMPEDE per board) now also payments-svc, ongoing. board.md:4 OPEN RUNBOOK_UPDATE. No changes.md. Logs R8: checkout-api.log disk used_pct lines 1,5,19,23; payments-svc.log disk lines 2,7,9,14. No 429. R8 scanned; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))