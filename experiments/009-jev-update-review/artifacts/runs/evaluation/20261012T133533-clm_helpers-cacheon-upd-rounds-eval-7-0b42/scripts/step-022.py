import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
n=c['entries'][0]
n['body']=n['body'].replace(' Board r7 empty.','')+' R8 logs disk checkout(r8 checkout-api.log:48) payments(r8 payments-svc.log:7). R9: A resolved (round-09/board.md:3); B cause DISK_PRESSURE (r9 board.md:4); Thread C ledger-svc failures ongoing cause unknown (r9 board.md:5) - suspect CHG-113 pool_max=0; OPEN VENDOR_TICKET (r9 board.md:6); CHG-163 noise.'
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-09/logs/ledger-svc.log'),1):
  if 'INFO' not in l and 'slow query' not in l: print(i,l.strip()[:140])
