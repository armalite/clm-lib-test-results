import json
p='/task/workspace/context.json'
c=json.load(open(p))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
keep.append({'id':'n6','role':'note','body':'R6: round-06/board.md:3 Thread A mitigated (CHG-150 APPLIED round-06/changes.md:4 pricing-svc mitigation); board.md:4 CLOSED VENDOR_TICKET. No 429s in pricing/search R6. DNS SERVFAIL kms.internal continues round-06/logs/inventory-svc.log:3-81. Open follow-ups: POSTMORTEM_DRAFT, CAPACITY_REVIEW. Next: advance to R7.'})
c['entries']=keep
json.dump(c,open(p,'w'))