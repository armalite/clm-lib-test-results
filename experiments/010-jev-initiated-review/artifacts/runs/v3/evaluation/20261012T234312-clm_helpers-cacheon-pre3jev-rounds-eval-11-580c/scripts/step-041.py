import json
p='/task/workspace/context.json'
c=json.load(open(p))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7','n8','n9')]
E.append({'id':'n10','role':'note','body':'R10: round-10/board.md:3 Thread B services now inventory-svc+shipping-svc (DNS_RESOLUTION ongoing). board.md:4 Thread C opened checkout-api request failures, cause unidentified, ongoing. Logs: checkout-api config validation failed feature.batch_size=0 build 4.33.8 round-10/logs/checkout-api.log:1-61 (=> BAD_CONFIG_ROLLOUT, cite round-01/changes.md:4 CHG-113). DNS SERVFAIL round-10/logs/inventory-svc.log:2-75, round-10/logs/shipping-svc.log:1-68. CHG-174 PROPOSED irrelevant. Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to R11.'})
c['entries']=E
json.dump(c,open(p,'w'))
print('ok')