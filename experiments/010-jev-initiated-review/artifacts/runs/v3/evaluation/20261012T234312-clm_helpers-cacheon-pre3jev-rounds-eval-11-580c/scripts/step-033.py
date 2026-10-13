import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
c['entries'].append({'id':'n8','role':'note','body':'R8: round-08/board.md:3 Thread A resolved; :4 OPEN DATA_BACKFILL. CHG-157 irrelevant. DNS SERVFAIL kms.internal continues round-08/logs/inventory-svc.log:6-72; heap high pricing-svc round-08/logs/pricing-svc.log:4-46. Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to R9.'})
json.dump(c,open(p,'w'))
print('ok')