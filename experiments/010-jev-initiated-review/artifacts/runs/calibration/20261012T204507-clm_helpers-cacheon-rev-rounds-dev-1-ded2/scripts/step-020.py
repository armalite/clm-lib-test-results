import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board: CLOSED ALERT_TUNING; OPEN CUSTOMER_COMMS (round-06/board.md:3-4). CHG-147 retry budget irrelevant. payments 429 fx-rates round-06/logs/payments-svc.log:3,10,11. No notify errors. Next: advance R7.'})
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-06/logs/'
for n in ['checkout-api','auth-svc','search-api','notify-worker']:
  L=open(b+n+'.log').readlines()
  print(n,[i for i,l in enumerate(L,1) if re.search(r'429|ERROR|pool|inflight',l)][:10])