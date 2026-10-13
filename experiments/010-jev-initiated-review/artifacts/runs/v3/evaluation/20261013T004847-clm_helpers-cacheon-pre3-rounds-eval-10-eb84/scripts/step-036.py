import json
E=json.load(open('/task/workspace/context.json'))['entries']
E=[e for e in E if e['id'] in ('n1','n2','n3','n6','n7','n8')]
E.append({'id':'n9','role':'note','body':'Round9: Thread C opened shipping-svc failures ongoing (round-09/board.md:3); likely BAD_CONFIG_ROLLOUT from CHG-113 retry.backoff_ms=0 config validation failed round-09/logs/shipping-svc.log:15-69. OPEN RUNBOOK_UPDATE (round-09/board.md:4), OPEN CUSTOMER_COMMS (round-09/board.md:5). 429 still r9 inventory-svc.log:66-67, search-api.log:12-14. Next: advance to round 10.'})
json.dump({'format':'clm-context/v1','entries':E},open('/task/workspace/context.json','w'))