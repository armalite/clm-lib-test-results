import json,re
L=open('/task/fixtures/round-09/logs/inventory-svc.log').readlines()
for i,l in enumerate(L,1):
    if 'ERROR' in l:print(i,l.strip()[40:200])
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
d['entries'].append({'id':'n9','role':'note','body':'R9: board.md:3 Thread B cause DNS_RESOLUTION confirmed; board.md:4 Thread C inventory-svc ongoing cause unknown (likely BAD_CONFIG_ROLLOUT CHG-120 r02 changes.md:3); board.md:5 Thread D false alarm; board.md:6 POSTMORTEM_DRAFT OPEN. ledger/pricing dns errors continue (ledger :3-, pricing :3-).'})
json.dump(d,open(p,'w'))