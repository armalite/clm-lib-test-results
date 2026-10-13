import json
c=json.load(open('context.json'))
e={x['id']:x for x in c['entries']}
n9='R9: board Thread B mitigated (round-09/board.md:3); Thread C pods still restarting (board.md:4). CHG-164 APPLIED retry GETs noise. Logs: notify-worker config validation failed round-09/logs/notify-worker.log:3-67; 429 fx-rates checkout-api round-09/logs/checkout-api.log:34-55, payments-svc round-09/logs/payments-svc.log:34-42. auth/search clean.'
c['entries']=[e[k] for k in ['n1','n2','n3','n4','n5','n6','n7','n8']]+[{'id':'n9','role':'note','body':n9}]
for x in c['entries']:
  if x['id'] in('n1','n6','n7'):x['body']=x['body'][:200]
json.dump(c,open('context.json','w'))
print('ok')