open('/task/workspace/notes.md','a').write('R1: CHG-107 APPLIED retry budget GETs=1 (round-01/changes.md:3). inventory-svc DNS SERVFAIL rates.internal lines 7-90 (round-01/logs/inventory-svc.log:7,85-90). board empty. slow query WARN noise everywhere.\n')
L=open('/task/fixtures/round-01/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'slow query' not in l and ('ERROR' in l or 'WARN' in l): print(i,l[:150])
print(open('/task/fixtures/round-01/changes.md').read().splitlines())