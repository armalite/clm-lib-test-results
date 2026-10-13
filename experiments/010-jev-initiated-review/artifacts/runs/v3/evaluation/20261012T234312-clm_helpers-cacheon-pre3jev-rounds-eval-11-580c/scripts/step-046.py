import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n11','role':'note','body':'R11: round-11/board.md:3 Thread B mitigated (DNS_RESOLUTION inventory-svc+shipping-svc). :4 Thread C still ongoing (pods restarting). checkout-api config validation failed batch_size=0 round-11/logs/checkout-api.log:2-64. DNS SERVFAIL round-11/logs/inventory-svc.log:68-70, round-11/logs/shipping-svc.log:35-41. No changes.md R11. Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to R12.'})
json.dump(c,open(p,'w'))