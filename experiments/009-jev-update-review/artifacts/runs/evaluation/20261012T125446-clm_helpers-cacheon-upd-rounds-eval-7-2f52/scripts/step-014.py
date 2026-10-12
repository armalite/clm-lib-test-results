import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: board empty. changes.md:3 CHG-137 PROPOSED (irrelevant). Logs R5: checkout-api.log disk used_pct 91-97 lines 1,7,56,70 (DISK_PRESSURE continues). 429 tax-provider search-api.log 18,25,77; shipping-svc.log 26,38,71. R5 scanned; next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))