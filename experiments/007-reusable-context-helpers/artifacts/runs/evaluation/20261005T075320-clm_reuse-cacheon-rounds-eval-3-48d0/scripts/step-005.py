import ctx
ctx.keep_only(['n1'])
import json
d=json.load(open('context.json'))
d['entries'].append({'id':'n2','role':'note','body':'R2: board.md:3 Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing. changes.md:3 CHG-117 PROPOSED. inventory-svc.log:10-13 cert errors; ledger-svc.log:20,23,28,43.'})
json.dump(d,open('context.json','w'))