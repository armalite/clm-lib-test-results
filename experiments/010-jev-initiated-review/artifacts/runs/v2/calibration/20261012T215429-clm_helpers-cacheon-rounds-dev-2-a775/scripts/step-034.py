import json
x=json.load(open('/task/workspace/context.json'))
x['entries']=[e for e in x['entries'] if e['id']=='notes']
x['entries'][0]['body']+=' R10: board.md:3 Thread D FALSE ALARM (drop UPSTREAM_RATE_LIMIT); board.md:4 CLOSED DATA_BACKFILL. changes CHG-175 noise. CERT auth-svc.log:10,17 shipping-svc.log:3,60. search-api config failed http.max_inflight=-1 round-10/logs/search-api.log:1,4. No DNS. Round 10 reviewed; next: advance.'
json.dump(x,open('/task/workspace/context.json','w'))
print('ok')