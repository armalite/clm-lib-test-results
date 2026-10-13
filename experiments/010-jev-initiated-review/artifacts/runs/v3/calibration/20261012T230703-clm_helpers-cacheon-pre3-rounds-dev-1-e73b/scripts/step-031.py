import json
c=json.load(open('context.json'))
e={x['id']:x for x in c['entries']}
n8='R8: board Thread A resolved (round-08/board.md:3); Thread B cause revised UPSTREAM_RATE_LIMIT (board.md:4); Thread C opened notify-worker ongoing cause unknown (board.md:5). CHG-159 PROPOSED noise. Logs: notify-worker config validation failed http.max_inflight=0 build 8.56.0 round-08/logs/notify-worker.log:5,45,50..72 (BAD_CONFIG via CHG-120 round-02/changes.md:4); 429 fx-rates checkout-api round-08/logs/checkout-api.log:1-54, payments-svc round-08/logs/payments-svc.log:2-83. auth/search clean.'
c['entries']=[e[k] for k in ['n1','n2','n3','n4','n5','n6','n7']]+[{'id':'n8','role':'note','body':n8}]
json.dump(c,open('context.json','w'))
print('ok')