import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']=e['body'].replace(' Next: advance to R9.','')+" R9: board B mitigated (round-09/board.md:3); C still restarting (board.md:4). notify config validation failed notify-worker.log:3,5,12,14,15. 429 fx-rates checkout-api.log:34,55; payments-svc.log:34,42. CHG-164 irrelevant. Next: advance to R10."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')