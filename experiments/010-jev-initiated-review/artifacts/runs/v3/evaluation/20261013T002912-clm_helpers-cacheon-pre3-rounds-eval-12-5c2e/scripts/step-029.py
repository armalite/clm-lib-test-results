import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5','n6')]
e.append({'id':'n7','role':'note','body':'R7: board Thread B adds checkout-api, cause/status unchanged (round-07/board.md:3) - board still says QUEUE_BACKLOG ongoing but logs show 429 tax-provider. CHG-152 PROPOSED only. Logs: checkout-api 429 n=10 (round-07/logs/checkout-api.log:4,14,15,19); ledger-svc 429 n=8 (round-07/logs/ledger-svc.log:13,20,34,47); others clean. Next: advance R8.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')