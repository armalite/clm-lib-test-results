import json
c=json.load(open('/task/workspace/context.json'))
keep={'n1','n2','n3'}
E=[e for e in c['entries'] if e['id'] in keep]
E.append({'id':'n4','role':'note','body':'Thread B UPSTREAM_RATE_LIMIT payments-svc+checkout-api (fx-rates 429). r9 MITIGATED (round-09/board.md:3). refs: round-04/logs/payments-svc.log:1,3; round-08/board.md:4; round-09/logs/checkout-api.log:34,55; payments-svc.log:34,42. CHG-164 APPLIED retry GETs=1 (round-09/changes.md:3).'})
E.append({'id':'n5','role':'note','body':'Thread A RESOLVED (round-08/board.md:3). Thread C notify-worker ongoing (round-08/board.md:5, round-09/board.md:4); cause BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:4): round-08/logs/notify-worker.log:5,45,50,58; round-09/logs/notify-worker.log:3,5,12. CHG-159 PROPOSED. Next: advance round 10.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')