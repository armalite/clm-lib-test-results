import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7','n8')]
keep.append({'id':'n9','role':'note','body':'Round9: board Thread D (MEMORY_LEAK pricing-svc) closed false alarm (round-09/board.md:3). No changes.md. DNS_RESOLUTION kms.internal now also shipping-svc: round-09/logs/shipping-svc.log:17,38,57,58,66,78; inventory-svc.log:7,13,22,44,66,75,80. Round 9 done; next: advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')