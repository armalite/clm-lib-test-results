import json
E=json.load(open('/task/workspace/context.json'))['entries']
E=[e for e in E if e['id'] in ('n1','n2','n3','n6','n7','n8','n9')]
E.append({'id':'n10','role':'note','body':'Round10: Thread C note pods still restarting (round-10/board.md:3); config validation failed retry.backoff_ms=0 round-10/logs/shipping-svc.log:3-74. CLOSED ALERT_TUNING (round-10/board.md:4). 429 still r10 search-api.log:13,31 inventory-svc.log:36,59. Next: advance to round 11.'})
json.dump({'format':'clm-context/v1','entries':E},open('/task/workspace/context.json','w'))