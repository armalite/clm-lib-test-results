import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
d['entries'].append({'id':'n10','role':'note','body':'R10: board.md:3 Thread C pods still restarting (ongoing). changes CHG-170 PROPOSED noise. inventory config validation failed inventory-svc.log:13,19,32,34,41,50; ledger dns :2-81; pricing dns :1-54. Next: advance to round 11.'})
json.dump(d,open(p,'w'))