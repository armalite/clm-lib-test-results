import ctx,json
d=json.load(open('context.json'))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance.','')+'\nR06: board.md:3 Thread A RESOLVED; board.md:4 ALERT_TUNING OPEN; board.md:5 RUNBOOK_UPDATE OPEN. changes.md:3 CHG-142 retry budget (noise). DNS SERVFAIL rates.internal ledger-svc.log:13-68 AND now pricing-svc.log:5-67. Next: advance.'
ctx.replace_all(n)
print('ok')