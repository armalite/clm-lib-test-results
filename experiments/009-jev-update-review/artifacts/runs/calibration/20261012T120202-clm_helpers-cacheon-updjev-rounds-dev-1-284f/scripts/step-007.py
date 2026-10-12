import json,re
for s in ['search-api','notify-worker']:
    L=open(f'/task/fixtures/round-03/logs/{s}.log').read().splitlines()
    h=[(i+1,l[:140]) for i,l in enumerate(L) if re.search('ERROR|pool|inflight|exhaust',l)]
    print(s,len(h));[print(x) for x in h[:6]]
n='R1: board empty; CHG-108 PROPOSED. R2: follow-ups OPEN ALERT_TUNING(round-02/board.md:3), RUNBOOK_UPDATE(:4), VENDOR_TICKET(:5). CHG-120 APPLIED notify-worker 8.56.0 http.max_inflight=0 (round-02/changes.md:4) -> suspect BAD_CONFIG_ROLLOUT. auth-svc pool WARNs round-02/logs/auth-svc.log:1-25. R3: Thread A DB_POOL_EXHAUSTED auth-svc+search-api ongoing (round-03/board.md:3). CHG-125 dashboards irrelevant.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))