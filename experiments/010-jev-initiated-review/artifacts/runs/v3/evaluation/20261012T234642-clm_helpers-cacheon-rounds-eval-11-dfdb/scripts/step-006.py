import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'].append({'id':'n2','role':'note','body':'R2: board: follow-ups OPEN VENDOR_TICKET (round-02/board.md:3), POSTMORTEM_DRAFT (:4). changes CHG-116 log sampling (noise). pricing-svc 429 upstream=sms-gateway ERRORs round-02/logs/pricing-svc.log:4,6,12,21,34,37,53,54,67,68,72,73 -> UPSTREAM_RATE_LIMIT candidate. No board incident yet. Next: advance to R3.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')