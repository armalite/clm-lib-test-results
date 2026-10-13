import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board CLOSED ALERT_TUNING (round-06/board.md:3), OPEN CUSTOMER_COMMS (:4). CHG-147 APPLIED retry budget GET=1 (round-06/changes.md:3). 429s continue in checkout-api(6) & payments-svc(5); no pool WARNs; notify clean.'})
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=[i+1 for i,l in enumerate(open(f)) if '429' in l]
  if L:print(f.split('/')[-1],L)