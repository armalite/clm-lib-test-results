import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8','role':'note','body':'R8: Thread A RESOLVED (round-08/board.md:3). Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4); 429 fx-rates continue checkout-api round-08/logs/checkout-api.log:1-29, payments-svc round-08/logs/payments-svc.log:2-34. Thread C opened notify-worker ongoing cause unknown (round-08/board.md:5); logs show config validation failed http.max_inflight=0 round-08/logs/notify-worker.log:5,45,50,58 => BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:4). CHG-159 PROPOSED noise. Next: advance R9.'})
json.dump(c,open(p,'w'))
print('ok')