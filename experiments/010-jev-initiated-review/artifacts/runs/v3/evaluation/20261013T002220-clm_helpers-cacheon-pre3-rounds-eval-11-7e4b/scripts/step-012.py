import json
n1='Round1: board empty. changes: CHG-111 PROPOSED (not applied) round-01/changes.md:3; CHG-113 APPLIED round-01/changes.md:4 build 4.33.8 checkout-api sets feature.batch_size=0 (BAD_CONFIG_ROLLOUT candidate, no errors yet); CHG-114 APPLIED line5 inventory-svc. Baseline WARN slow query 200-450ms is noise.'
n2='Round2: board round-02/board.md:3 Follow-up OPEN VENDOR_TICKET; :4 OPEN POSTMORTEM_DRAFT. CHG-116 APPLIED log sampling (irrelevant). pricing-svc 429 upstream=sms-gateway round-02/logs/pricing-svc.log lines 4-73.'
n3='Round3: board round-03/board.md:3 Thread A UPSTREAM_RATE_LIMIT pricing-svc + search-api, ongoing. 429 sms-gateway in round-03/logs/pricing-svc.log:4-64 and search-api.log:8-79. No other errors. Next: advance to round 4.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2},{'id':'n3','role':'note','body':n3}]}
json.dump(c,open('/task/workspace/context.json','w'))