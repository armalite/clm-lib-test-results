import json,os
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n11','role':'note','body':'R11: Thread B mitigated (round-11/board.md:3). inventory config ERRORs (round-11/logs/inventory-svc.log:1,5,32). DNS ledger (round-11/logs/ledger-svc.log:2,40) pricing (round-11/logs/pricing-svc.log:8,30). Next: advance to R12.'})
json.dump(c,open(p,'w'))
f='/task/fixtures/round-11/changes.md'
print(open(f).read() if os.path.exists(f) else 'nochg')