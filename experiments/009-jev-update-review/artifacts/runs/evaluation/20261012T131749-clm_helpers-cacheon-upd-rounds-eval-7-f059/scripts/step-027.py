import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1'][0]
b=e['body']
i=b.find('R1:')
b="KEY: CHG-113 round-01/changes.md:3 ledger pool_max=0. ThreadA UPSTREAM_RATE_LIMIT shipping+search resolved R9 board.md:3 (R6 mitigated board:3, CHG-150 round-06/changes.md:3). ThreadB DISK_PRESSURE checkout-api+payments-svc ongoing round-09/board.md:4, round-08/board.md:3; logs round-09/logs/checkout-api.log:17,19 payments-svc.log:3,4. ThreadC ledger-svc board round-09/board.md:5 ongoing cause unknown; logs show BAD_CONFIG_ROLLOUT config validation failed db.pool_max=0 build 7.35.5 round-09/logs/ledger-svc.log:13,20,23,24. Follow-ups OPEN: POSTMORTEM_DRAFT(r2:3), DATA_BACKFILL(r3:4), CAPACITY_REVIEW(r3:5), RUNBOOK_UPDATE(r8:4), VENDOR_TICKET(r9:6). R9 done; next advance to R10."
e['body']=b
c['entries']=[e]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')