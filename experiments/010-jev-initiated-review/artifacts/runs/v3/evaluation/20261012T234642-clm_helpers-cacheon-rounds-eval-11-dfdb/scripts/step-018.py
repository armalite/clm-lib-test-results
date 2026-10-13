import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board Thread A mitigated (round-06/board.md:3); VENDOR_TICKET CLOSED (:4). changes CHG-150 APPLIED mitigation thread A pricing-svc (round-06/changes.md:4); CHG-147 noise. 429 gone in pricing/search. DNS kms.internal still failing round-06/logs/inventory-svc.log:3,8,11,19,26,31,33,34,39,59,75,81. Open follow-ups: POSTMORTEM_DRAFT, CAPACITY_REVIEW. Next: advance to R7.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')