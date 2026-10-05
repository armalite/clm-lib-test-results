import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: Thread B cause revised DNS_RESOLUTION (round-09/board.md:3). Thread C inventory-svc failures cause unknown ongoing (board.md:4). Thread D closed false alarm (board.md:5). Follow-up OPEN POSTMORTEM_DRAFT (board.md:6). inventory-svc config validation ERRORs (round-09/logs/inventory-svc.log:2,15,28) -> likely BAD_CONFIG_ROLLOUT from CHG-120 (round-02/changes.md:3). DNS continues ledger (round-09/logs/ledger-svc.log:3,9) pricing (round-09/logs/pricing-svc.log:3,14).'})
json.dump(c,open('/task/workspace/context.json','w'))
l=open('/task/fixtures/round-09/logs/inventory-svc.log').read().splitlines()
print(l[1][:300])
import os;print(os.listdir('/task/fixtures/round-09'))