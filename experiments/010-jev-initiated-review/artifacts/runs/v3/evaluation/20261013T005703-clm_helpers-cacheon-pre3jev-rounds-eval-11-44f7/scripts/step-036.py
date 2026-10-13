import json
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
b=n1['body'].replace('\nR8: released; raw obs in /task/workspace/spill/s32.obs.txt (summarize next step).','')
b+='\nR8: board Thread A resolved (round-08/board.md:3); follow-up OPEN DATA_BACKFILL (board.md:4). CHG-157 log sampling only. inventory dns SERVFAIL kms.internal continues (round-08/logs/inventory-svc.log:6,21). pricing-svc heap usage high rss 3048 (round-08/logs/pricing-svc.log:4). Open follow-ups: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to R9.'
n1['body']=b
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')