import json
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace(' Round 2 reviewed; next: advance.','')
n+=' R3: board.md:3 Thread B auth-svc suspected DB_POOL_EXHAUSTED ongoing, BUT logs show CERT_EXPIRED peer=sso.example.net round-03/logs/auth-svc.log:6,9,72 (board cause likely wrong). checkout+inventory DNS still failing r3 checkout-api.log:33-74, inventory-svc.log:3-50. CHG-126 PROPOSED (ignore). search-api no errors yet. Round 3 reviewed; next: advance.'
c['entries']=[{'id':'notes','role':'note','body':n}]
json.dump(c,open('/task/workspace/context.json','w'))