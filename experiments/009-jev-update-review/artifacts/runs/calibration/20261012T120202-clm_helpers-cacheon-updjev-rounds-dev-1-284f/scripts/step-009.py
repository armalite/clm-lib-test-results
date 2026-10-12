import json,re
L=open('/task/fixtures/round-04/logs/payments-svc.log').read().splitlines()
h=[(i+1,l[:130]) for i,l in enumerate(L) if re.search('ERROR|cache|miss|429|cert|tls',l,re.I)]
print(len(h));[print(x) for x in h[:8]]
L=open('/task/fixtures/round-04/logs/notify-worker.log').read().splitlines()
h=[(i+1,l[:130]) for i,l in enumerate(L) if re.search('ERROR|inflight',l)]
print('nw',len(h));[print(x) for x in h[:4]]
n='R1: board empty; CHG-108 PROPOSED. R2: follow-ups OPEN ALERT_TUNING(round-02/board.md:3), RUNBOOK_UPDATE(:4), VENDOR_TICKET(:5). CHG-120 APPLIED notify-worker 8.56.0 http.max_inflight=0 (round-02/changes.md:4) -> suspect BAD_CONFIG_ROLLOUT but no notify-worker errors in R3. auth-svc pool WARNs round-02/logs/auth-svc.log:1-25. R3: Thread A DB_POOL_EXHAUSTED auth-svc+search-api ongoing (round-03/board.md:3); search-api pool exhausted round-03/logs/search-api.log:1-53. CHG-125 dashboards irrelevant. R4: Thread B CACHE_STAMPEDE payments-svc ongoing (round-04/board.md:3). CHG-133 APPLIED TLS ticket rotation hourly (round-04/changes.md:3) - watch for CERT issues.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))