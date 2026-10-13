import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
keep.append({'id':'n6','role':'note','body':'Round6: board Thread A (UPSTREAM_RATE_LIMIT) mitigated (round-06/board.md:3); follow-up VENDOR_TICKET CLOSED (board.md:4). CHG-150 APPLIED mitigation thread A pricing-svc (round-06/changes.md:4); CHG-147 benign. No 429s in r6. inventory-svc dns lookup failed kms.internal round-06/logs/inventory-svc.log:3,8,11,19,26,31,33,34,39,59,75,81 (log format now JSON). Open follow-ups: POSTMORTEM_DRAFT, CAPACITY_REVIEW. Round 6 done; next: advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')