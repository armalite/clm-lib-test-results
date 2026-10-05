import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
d['entries'].append({'id':'n8','role':'note','body':'R8: board empty; changes.md:3 CHG-156 noise. inventory tls fail inventory-svc.log:6-78; ledger dns ledger-svc.log:2-64; pricing dns pricing-svc.log:4-51. Next: advance to round 9.'})
json.dump(d,open(p,'w'))
print('ok')