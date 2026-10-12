import json
c=json.load(open('/task/workspace/context.json'))
s=c['entries'][0]['body'].replace(' Next: advance to R11.','')+' R11: Thread B +ledger-svc (round-11/board.md:3), status mitigated (round-11/board.md:4); Thread C still ongoing (round-11/board.md:5); CUSTOMER_COMMS CLOSED (round-11/board.md:6); CHG-179 PROPOSED only. Next: advance to R12.'
c['entries']=[{'id':'sum1','role':'summary','body':s}]
json.dump(c,open('/task/workspace/context.json','w'))
import re
for f in ['checkout-api','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-11/logs/{f}.log'),1):
    if re.search('pool_max|certificate|ERROR|error',l):print(f,i,l.strip()[:150])