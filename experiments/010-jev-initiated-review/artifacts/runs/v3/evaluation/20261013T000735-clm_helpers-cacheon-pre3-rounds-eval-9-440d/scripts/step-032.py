import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR6: board Thread A mitigated (round-06/board.md:3); follow-up OPEN RUNBOOK_UPDATE (round-06/board.md:4). changes: CHG-142 retry budget (round-06/changes.md:3); CHG-150 APPLIED thread A mitigation ledger-svc (round-06/changes.md:4). Logs: no DNS errors in inventory/ledger r6; notify-worker disk high round-06/logs/notify-worker.log:12,14,48,52; shipping cert expired round-06/logs/shipping-svc.log:1,22, disk :13,17. search-api no errors. Next: advance to round 7."
c['entries']=[n]
json.dump(c,open(p,'w'))
print('ok')