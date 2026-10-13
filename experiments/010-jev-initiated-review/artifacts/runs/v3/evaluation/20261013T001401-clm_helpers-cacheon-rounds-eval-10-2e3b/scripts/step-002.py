import json
n='R1: board empty. changes.md:3 CHG-113 APPLIED shipping-svc build 6.58.8 sets retry.backoff_ms=0 (suspicious BAD_CONFIG); :4 CHG-114 search-api no config. Logs: only routine slow query WARNs in all services (shipping,checkout,auth,inventory,search). No incident yet.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))
open('/task/workspace/scan.py','w').write('''import os,sys
r=sys.argv[1];b='/task/fixtures/round-'+r
for x in sorted(os.listdir(b)):
  p=b+'/'+x
  if x.endswith('.md'):
    for i,l in enumerate(open(p),1):
      if l.strip():print(x,i,l.rstrip()[:200])
for x in sorted(os.listdir(b+'/logs')):
  for i,l in enumerate(open(b+'/logs/'+x),1):
    if 'slow query' in l or ' INFO' in l or 'level=info' in l.lower():continue
    print(x,i,l.rstrip()[:160])
''')