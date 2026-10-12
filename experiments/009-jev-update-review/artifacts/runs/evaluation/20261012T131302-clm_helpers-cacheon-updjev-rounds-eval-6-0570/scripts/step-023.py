import json,re
L=open('/task/fixtures/round-08/logs/pricing-svc.log').read().splitlines()
for i,l in enumerate(L,1):
  if re.search(r'ERROR|batch|config|429|fail',l,re.I): print(i,l[:160])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']=e['body'].replace(' Next: advance to R8.','')+"\nR8: board Thread B revised DISK_PRESSURE payments-svc (round-08/board.md:3) confirms. Thread C pricing-svc failures cause unknown ongoing (round-08/board.md:4) -> suspect CHG-120 BAD_CONFIG_ROLLOUT."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))