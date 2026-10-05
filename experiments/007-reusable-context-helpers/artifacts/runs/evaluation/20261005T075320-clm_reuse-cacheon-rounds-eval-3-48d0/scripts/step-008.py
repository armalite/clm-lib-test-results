import ctx,json
ctx.keep_only(['n1','n2'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n3','role':'note','body':'R3: board empty. changes.md:3 CHG-125 APPLIED retry budget=1. cert errors continue inventory-svc.log:9-18,39-57,71; ledger-svc.log:23-43,61-69. no other errors.'})
json.dump(d,open('context.json','w'))