import json
p='/task/workspace/context.json'
n=json.load(open(p))['entries'][0]['body']
n+=' R7: board round-07/board.md:3 Thread B revised CERT_EXPIRED; :4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing. search-api 429 upstream=tax-provider round-07/logs/search-api.log:4-66 (note CHG-120 search-api max_inflight=-1 may be real cause later). CERT continues round-07/logs/auth-svc.log:1-64, round-07/logs/shipping-svc.log:10-66. checkout/inventory no errs.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open(p,'w'))