import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
keep.append({'id':'n7','role':'note','body':'Round7: board Thread B cause revised to DNS_RESOLUTION inventory-svc (round-07/board.md:3). Thread D opened MEMORY_LEAK pricing-svc ongoing (round-07/board.md:4) - verify in logs later (no memory errors in r7 ERROR grep; check WARN/restart lines). CHG-153 PROPOSED (ignore). dns kms.internal SERVFAIL round-07/logs/inventory-svc.log:1,3,21,29,31,59,65. Round 7 done; next: advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')