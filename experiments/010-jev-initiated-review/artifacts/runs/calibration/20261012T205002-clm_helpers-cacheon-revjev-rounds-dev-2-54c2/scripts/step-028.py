import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: board.md:3 Thread C pods still restarting, continues. changes.md:3 CHG-166 retry budget (noise). search-api errs 429 + config (round-09/logs/search-api.log:1-40). CERT errs round-09/logs/auth-svc.log:22,55 shipping-svc.log:28,56. No errs checkout/inventory. Next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))