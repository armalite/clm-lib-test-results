import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
keep.append({'id':'n8','role':'note','body':'Round8: board Thread A resolved (round-08/board.md:3); follow-up OPEN DATA_BACKFILL (board.md:4). CHG-157 benign. No memory/restart lines in r8 for pricing-svc (MEMORY_LEAK thread D unverified, maybe false alarm). dns kms.internal round-08/logs/inventory-svc.log:6,21,22,27,49,59,60,62,72. Round 8 done; next: advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')