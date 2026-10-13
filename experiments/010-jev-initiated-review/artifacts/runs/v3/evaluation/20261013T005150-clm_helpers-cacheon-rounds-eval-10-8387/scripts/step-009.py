import json
n=open('notes.md').read()+"R3: board A DNS_RESOLUTION auth-svc+checkout-api ongoing (round-03/board.md:3). B search-api suspected DB_POOL ongoing (:4) but logs show 429 upstream=fx-rates round-03/logs/search-api.log:16-62 -> likely UPSTREAM_RATE_LIMIT. DNS errs auth-svc.log:2-59, checkout-api.log:14-63. CHG-123 dashboards irrelevant.\n"
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))
print('ok')