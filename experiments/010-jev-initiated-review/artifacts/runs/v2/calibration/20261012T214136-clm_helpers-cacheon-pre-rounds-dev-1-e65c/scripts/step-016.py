import json
n='''Round1: board empty. r01 changes.md:3 CHG-108 PROPOSED HPA search (not applied). slow query WARN = noise.
Round2: board.md:3-5 follow-ups OPEN ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker build 8.56.0 sets http.max_inflight=0 (suspect BAD_CONFIG_ROLLOUT, watch notify-worker); changes.md:5 CHG-121 payments no config. auth-svc db pool exhausted r02 lines 1,3,15,22.
Round3: board.md:3 Thread A DB_POOL_EXHAUSTED auth-svc + search-api ongoing. changes.md:3 CHG-125 dashboards (irrelevant). auth-svc.log pool exhausted 7-63; search-api.log 1-77. notify-worker no errors r3.
Round4: board.md:3 Thread B payments-svc suspected CACHE_STAMPEDE ongoing, BUT logs show 429 upstream=fx-rates in payments-svc (lines 1,3,7..79) and checkout-api (9,19) -> real cause likely UPSTREAM_RATE_LIMIT, services payments-svc+checkout-api. changes.md:3 CHG-133 TLS ticket rotation (likely irrelevant). auth-svc pool exhausted 7-81, search-api 4. notify-worker still clean. Next: advance to round 5.'''
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')