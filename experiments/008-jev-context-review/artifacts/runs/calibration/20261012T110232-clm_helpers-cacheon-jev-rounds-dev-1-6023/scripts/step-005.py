import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; CHG-108 PROPOSED (HPA search) round-01/changes.md:3. Helper: python3 /task/workspace/scan.py NN prints board/changes + non-slow-query WARN/ERROR lines.'},{'id':'n2','role':'note','body':'R2: board opens follow-ups ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET (round-02/board.md:3-5). CHG-120 APPLIED notify-worker sets http.max_inflight=0 (round-02/changes.md:4) suspect BAD_CONFIG. CHG-121 payments no config. auth-svc db pool exhausted WARNs round-02/logs/auth-svc.log:1-69 (lines 1,3,15,22,23,25,44,65,69) -> DB_POOL_EXHAUSTED candidate, not on board yet.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
l=open('/task/fixtures/round-02/logs/notify-worker.log').read().splitlines()
for i,x in enumerate(l,1):
  if 'INFO' not in x or 'inflight' in x: print(i,x[:150])
print(l[:3])