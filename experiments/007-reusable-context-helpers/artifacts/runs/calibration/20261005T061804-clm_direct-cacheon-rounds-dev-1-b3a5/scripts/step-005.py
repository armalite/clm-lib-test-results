import json
n1='R1: board empty; changes.md:3 CHG-108 PROPOSED (HPA search). Logs only slow-query noise. Services: notify-worker, checkout-api, auth-svc, payments-svc, search-api.'
n2='R2: board.md:3-5 follow-ups OPEN ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker 8.56.0 sets http.max_inflight=0 (suspect BAD_CONFIG, no errors yet); :5 CHG-121 payments no config. auth-svc.log:1,3,15,22,23,25,44,65,69 db pool exhausted WARN (DB_POOL_EXHAUSTED candidate, not on board yet). Filter used: skip lines with slow query/INFO.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))