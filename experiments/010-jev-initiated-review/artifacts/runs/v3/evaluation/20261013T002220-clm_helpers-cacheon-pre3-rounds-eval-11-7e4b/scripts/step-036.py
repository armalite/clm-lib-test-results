import json
e=json.load(open('/task/workspace/context.json'))['entries']
e=[x for x in e if x['id'].startswith('n')]
e.append({'id':'n9','role':'note','body':'R9: round-09/board.md:3 Thread D closed false alarm (drop MEMORY_LEAK). DNS SERVFAIL kms.internal now also shipping-svc round-09/logs/shipping-svc.log:17-57; inventory round-09/logs/inventory-svc.log:7-22. Next: advance R10.'})
json.dump({'format':'clm-context/v1','entries':e},open('/task/workspace/context.json','w'))