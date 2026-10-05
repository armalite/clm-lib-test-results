import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5','n6','n7')]
e.append({'id':'n8','role':'note','body':'R8: Thread A RESOLVED (round-08/board.md:3). Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4); 429 fx-rates round-08/logs/checkout-api.log:1, payments-svc.log:2. Thread C opened notify-worker ongoing cause unknown (round-08/board.md:5); log round-08/logs/notify-worker.log:5 config validation failed http.max_inflight=0 -> BAD_CONFIG_ROLLOUT via CHG-120 (round-02/changes.md:4). CHG-159 PROPOSED ignore. Next: advance R9.'})
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
print('ok')