import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R10: board.md:3 CLOSED DATA_BACKFILL. CHG-174 PROPOSED only. search-api config validation failed ttl -1 search-api.log:2,6,11,12,39. 429 auth-svc.log:1,32; shipping-svc.log:8,27. No pool WARNs. Next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))