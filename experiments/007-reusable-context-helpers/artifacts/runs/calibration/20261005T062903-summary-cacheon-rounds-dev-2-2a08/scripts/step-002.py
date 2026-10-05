open('/task/workspace/notes.md','a').write('R1: CHG-107 APPLIED retry budget GET=1 (round-01/changes.md:3). inventory-svc DNS SERVFAIL rates.internal lines 7-90 of round-01/logs/inventory-svc.log. Board empty. slow query WARN noise everywhere.\n')
L=open('/task/fixtures/round-01/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'ERROR' in l: print(i,l[:140])