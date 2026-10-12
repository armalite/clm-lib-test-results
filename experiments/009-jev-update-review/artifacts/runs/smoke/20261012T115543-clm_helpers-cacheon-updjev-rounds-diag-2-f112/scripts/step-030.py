import json,os
for f in ['board.md','changes.md']:
  p='/task/fixtures/round-09/'+f
  if os.path.exists(p):
    for i,l in enumerate(open(p).read().splitlines()):print(f,i+1,l[:160])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='notes':e['body']+=' R9 logs: inventory disk round-09/logs/inventory-svc.log:26,61; ledger disk round-09/logs/ledger-svc.log:8,64; notify pool_max errs round-09/logs/notify-worker.log:1,4,8,33; pricing/search quiet.'
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))