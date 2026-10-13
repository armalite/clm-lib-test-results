import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=c['entries'][0]['body']+"\nR6: board round-06/board.md:3 Thread A mitigated; :4 follow-up OPEN RUNBOOK_UPDATE. round-06/changes.md:4 CHG-150 APPLIED mitigation thread A to ledger-svc; :3 CHG-142 retry budget. DNS errors gone R6 (inventory, ledger clean). shipping cert_expired round-06/logs/shipping-svc.log:1 (+disk WARNs, lines 1,13,17,22,23,26,30,40,42,48,58,65,69,70,77,86 mixed). notify disk WARNs round-06/logs/notify-worker.log:12,14,48,52,72,78. search-api clean."
c['entries']=[{'id':'n1','role':'note','body':n}]
json.dump(c,open(p,'w'))
print('ok')