import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: Thread A resolved (round-08/board.md:3). Follow-up OPEN DATA_BACKFILL (:4). CHG-157 noise. pricing heap high lines round-08/logs/pricing-svc.log:4,33,40,44,46,56,67,72,75,80. DNS kms.internal continues round-08/logs/inventory-svc.log:6,21,22,27,49,59. Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to R9.'})
json.dump(c,open('/task/workspace/context.json','w'))