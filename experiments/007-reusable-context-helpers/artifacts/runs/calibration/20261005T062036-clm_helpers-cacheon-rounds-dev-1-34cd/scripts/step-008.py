import json,re
b='/task/fixtures/round-03/logs/'
for f in ['notify-worker.log','search-api.log','auth-svc.log']:
  L=open(b+f).read().splitlines()
  h=[i for i,l in enumerate(L,1) if 'pool exhausted' in l or re.search(r'ERROR|inflight',l)]
  print(f,h[:25])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: nothing; CHG-108 PROPOSED (search HPA) not applied. R2: auth-svc db pool exhausted WARNs (round-02/logs/auth-svc.log:1,3,15,22,23,25). CHG-120 APPLIED notify-worker http.max_inflight=0 (round-02/changes.md:4, possible BAD_CONFIG_ROLLOUT). Board R2 follow-ups OPEN: ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET. R3: board Thread A DB_POOL_EXHAUSTED auth-svc+search-api ongoing (round-03/board.md:3); pool WARNs auth-svc.log:7,12,13,15; search-api.log:1,14. CHG-125 dashboards irrelevant.'}]}
json.dump(c,open('/task/workspace/context.json','w'))