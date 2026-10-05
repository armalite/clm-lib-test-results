import os,re
b='/task/fixtures/round-01/'
skip=re.compile(r'request ok|health ok|heartbeat|gc cycle|slow query')
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if not skip.search(l):print(f,i,l.strip()[:150])
open('/task/workspace/notes.md','a').write('R1: CHG-113 APPLIED search-api cache.ttl_s=-1 (round-01/changes.md:4); inventory db pool exhausted round-01/logs/inventory-svc.log:5,9\n')