import json
for i,l in enumerate(open('/task/fixtures/round-02/logs/payments-svc.log'),1):
    if '429' in l: print(i,l.strip()[:160])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; CHG-108 PROPOSED (ignore). Background slow-query WARNs = noise in all 5 svcs. R2: board.md:3-5 follow-ups OPEN ALERT_TUNING,RUNBOOK_UPDATE,VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker 8.56.0 sets http.max_inflight=0 (suspect BAD_CONFIG, but no notify errors in R2 logs yet); :5 CHG-121 payments 8.56.0 no cfg; :3 CHG-116 log sampling. R2 auth-svc.log:1-69 db pool exhausted WARNs in_use=10/10 (DB_POOL_EXHAUSTED candidate). Other svcs R2: only slow-query WARNs; payments 1x 429 line checked step 8.'}]}
json.dump(c,open('/task/workspace/context.json','w'))