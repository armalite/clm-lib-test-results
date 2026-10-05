import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
d['entries'].append({'id':'n6','role':'note','body':'R6: board.md:3 Thread A resolved; board.md:4 ALERT_TUNING OPEN; board.md:5 RUNBOOK_UPDATE OPEN. changes.md:3 CHG-142 APPLIED retry GETs=1. DNS SERVFAIL rates.internal ledger-svc.log:13-29,54-68 AND pricing-svc.log:5-20,48-67 (pricing now affected, Thread B). Next: advance to round 7.'})
json.dump(d,open(p,'w'))