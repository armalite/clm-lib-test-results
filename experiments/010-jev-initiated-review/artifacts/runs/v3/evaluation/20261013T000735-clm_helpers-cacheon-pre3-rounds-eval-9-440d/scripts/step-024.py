import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR5: board Thread B services += notify-worker (round-05/board.md:3); Thread D CERT_EXPIRED shipping-svc ongoing (round-05/board.md:4) - verify, no cert errors seen; follow-up OPEN VENDOR_TICKET (round-05/board.md:5). DNS errors continue: round-05/logs/inventory-svc.log:22-75 (22,32,33,35,38,49,54,55,66,72,75), ledger-svc.log:17-68. notify-worker disk usage high round-05/logs/notify-worker.log:2-21,45,53 (DISK_PRESSURE candidate). Next: check shipping-svc r5 log then advance to round 6."
c['entries']=[n]
json.dump(c,open(p,'w'))
import subprocess
for i,l in enumerate(open('/task/fixtures/round-05/logs/shipping-svc.log'),1):
  if 'slow query' not in l: print(i,l.strip()[:110])