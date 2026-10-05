import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: Thread A resolved (round-06/board.md:3). Follow-ups OPEN ALERT_TUNING (board.md:4), RUNBOOK_UPDATE (board.md:5). CHG-142 APPLIED retry GETs=1. DNS SERVFAIL rates.internal now ledger-svc (round-06/logs/ledger-svc.log:13-29) AND pricing-svc (round-06/logs/pricing-svc.log:5-20). Next: advance to R7.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')