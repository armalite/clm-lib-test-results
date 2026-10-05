import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if not x['id'].startswith('s29')]
e.append({'id':'n10','role':'note','body':'R10: board.md:3 DATA_BACKFILL CLOSED. changes.md:3 CHG-174 PROPOSED. search-api.log ttl_s/err 2,6,11,12,39,43,50,52,70; 429 auth-svc.log 1,32; shipping-svc.log 8,27. Next: advance R11.'})
c['entries']=e
json.dump(c,open(p,'w'))