import json
n='R1: board empty; CHG-108 PROPOSED (HPA search, not applied). No incidents.\nR2: board follow-ups OPEN ALERT_TUNING(b:3),RUNBOOK_UPDATE(b:4),VENDOR_TICKET(b:5). changes: CHG-120 APPLIED notify-worker 8.56.0 sets http.max_inflight=0 (round-02/changes.md:4); CHG-121 payments no cfg. auth-svc db pool exhausted WARNs lines 1,3,15,22,23,25,44,65,69 (no board incident yet). notify-worker no errors by keyword scan.'
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))
L=open('/task/fixtures/round-02/logs/notify-worker.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'INFO' not in l or 'inflight' in l: print(i,l[:140])