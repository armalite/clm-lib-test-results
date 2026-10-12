import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8','role':'note','body':'R8: Thread A RESOLVED (round-08/board.md:3). Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4), 429 continue round-08/logs/checkout-api.log:1-54, payments-svc.log:2+. Thread C opened notify-worker ongoing cause unknown (round-08/board.md:5); logs config validation failed http.max_inflight=0 round-08/logs/notify-worker.log:5-72 -> BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:4). CHG-159 PROPOSED irrelevant. Next: advance, scan 09.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')