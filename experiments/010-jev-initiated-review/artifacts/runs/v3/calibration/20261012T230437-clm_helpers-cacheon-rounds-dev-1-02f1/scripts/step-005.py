import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'].append({'id':'n2','role':'note','body':'R2: board follow-ups OPEN ALERT_TUNING(board.md:3),RUNBOOK_UPDATE(:4),VENDOR_TICKET(:5). changes: CHG-120 APPLIED notify-worker http.max_inflight=0 (round-02/changes.md:4) - possible BAD_CONFIG_ROLLOUT, no notify errors yet; CHG-121 payments no config. auth-svc db pool exhausted WARNs round-02/logs/auth-svc.log:1-69 (lines 1,3,15,22,23,25,44,65,69) -> DB_POOL_EXHAUSTED candidate, no board thread yet.'})
json.dump(c,open('/task/workspace/context.json','w'))