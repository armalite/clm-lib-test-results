import json
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
b=n1['body']
b=b[:b.find('\nR7 raw')]
b+='\nR7: board Thread B cause revised to DNS_RESOLUTION (round-07/board.md:3); Thread D opened MEMORY_LEAK pricing-svc ongoing (round-07/board.md:4). CHG-153 PROPOSED only. Logs: inventory-svc dns SERVFAIL kms.internal (round-07/logs/inventory-svc.log:1,3,21,29,31). Next: advance to R8.'
n1['body']=b
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')