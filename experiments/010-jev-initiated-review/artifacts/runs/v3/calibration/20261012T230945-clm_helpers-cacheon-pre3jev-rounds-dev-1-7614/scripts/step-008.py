import json
n1='Round 1: services auth-svc, checkout-api, notify-worker, payments-svc, search-api. Background WARN slow query noise (ignore). CHG-108 PROPOSED (HPA search tier, not applied).'
n2='Round 2: board opens follow-ups ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET (round-02/board.md:3-5). changes: CHG-116 APPLIED log sampling (noise); CHG-120 APPLIED build 8.56.0 to notify-worker sets http.max_inflight=0 (round-02/changes.md:4) -> possible BAD_CONFIG_ROLLOUT, watch notify-worker; CHG-121 APPLIED payments-svc no config. auth-svc WARN db pool exhausted lines 1,3,15,22,23,25,44,65,69 (round-02/logs/auth-svc.log) -> DB_POOL_EXHAUSTED candidate, no board thread yet. Filter used: skip slow query and INFO/DEBUG unless keywords error|fail|429|expire|pool|lag|mem|disk|dns|cert. Next: advance round 3.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')