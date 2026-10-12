import json,re
b='/task/fixtures/round-08/logs/notify-worker.log'
L=[i for i,l in enumerate(open(b),1) if 'config validation failed' in l]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board: Thread A resolved (round-08/board.md:3); Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4); Thread C notify-worker failures ongoing, cause unknown (round-08/board.md:5). notify config validation failed http.max_inflight=0 build 8.56.0 -> BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:4); lines round-08/logs/notify-worker.log:'+','.join(map(str,L))+'. 429 fx-rates: checkout round-08/logs/checkout-api.log:1,6; payments round-08/logs/payments-svc.log:2. CHG-159 PROPOSED irrelevant. Next: advance R9.'})
json.dump(c,open('/task/workspace/context.json','w'))
print(L)