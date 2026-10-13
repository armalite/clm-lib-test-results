import json
c=json.load(open('/task/workspace/context.json'))
keep={'n1','n2','n3'}
E=[e for e in c['entries'] if e['id'] in keep]
E.append({'id':'n4','role':'note','body':'Thread B UPSTREAM_RATE_LIMIT (board confirmed round-08/board.md:4) payments-svc+checkout-api ongoing. refs: round-04/logs/payments-svc.log:1,3; round-05/changes? none; round-08/logs/checkout-api.log:1,6,20,29; payments-svc.log:2,24,25,34; round-04/board.md:3, round-05/board.md:4.'})
E.append({'id':'n5','role':'note','body':'Round 8: Thread A RESOLVED (round-08/board.md:3). Thread C opened notify-worker ongoing (round-08/board.md:5); real cause BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:4): round-08/logs/notify-worker.log:5,45,50,58. CHG-159 PROPOSED. Next: advance round 9.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')