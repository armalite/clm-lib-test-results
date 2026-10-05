import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
d['entries'].append({'id':'n11','role':'note','body':'R11: board.md:3 Thread B mitigated. inventory config validation failed inventory-svc.log:1,5,32-73 (Thread C ongoing); ledger dns :2,40; pricing dns :8,30,58. Next: advance to round 12.'})
json.dump(d,open(p,'w'))
print('ok')