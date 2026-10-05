import json,re
p='/task/workspace/context.json'
n1='R1: quiet; only slow-query WARNs in 5 svcs (auth-svc, checkout-api, notify-worker, payments-svc, search-api). CHG-108 PROPOSED (ignore). Scan: grep WARN|ERROR|fail|429|timeout, dedupe.'
n2='R2: board follow-ups OPEN: ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET (round-02/board.md:3-5). changes: CHG-120 APPLIED notify-worker http.max_inflight=0 (round-02/changes.md:4) suspect BAD_CONFIG; CHG-121 payments no cfg. auth-svc.log:1 db pool exhausted (single?).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]},open(p,'w'))
for f in ['auth-svc','notify-worker']:
  for i,l in enumerate(open('/task/fixtures/round-02/logs/'+f+'.log'),1):
    if re.search('pool|inflight|config|ERROR',l,re.I):print(f,i,l.strip()[:160])