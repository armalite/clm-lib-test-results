import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5','n6')]
e.append({'id':'n7','role':'note','body':'R7: board empty (no changes). 429 fx-rates still: round-07/logs/checkout-api.log:11, payments-svc.log:1. No db pool errs. No changes.md. Next: advance R8.'})
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
print('ok')