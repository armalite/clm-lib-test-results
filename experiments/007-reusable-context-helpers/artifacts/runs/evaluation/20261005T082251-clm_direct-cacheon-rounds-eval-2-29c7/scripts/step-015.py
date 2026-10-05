import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'] in('n1','n2','n3','n4')]
d['entries'].append({'id':'n5','role':'note','body':'R5: board empty; DNS SERVFAIL rates.internal continues ledger-svc.log:14,19,36,38,40,49 (Thread B still ongoing). Next: advance to round 6.'})
json.dump(d,open(p,'w'))