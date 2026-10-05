import json,glob,os
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: changes.md:3 CHG-107 PROPOSED HPA search; :4 CHG-113 APPLIED search-api cache.ttl_s=-1 (bad config?); :5 CHG-114 auth-svc no config. board empty. slow query WARNs = noise. R1 only inventory-svc db pool exhausted WARN lines 5,9,28,30,45,52 (round-01/logs/inventory-svc.log); other svcs clean.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
d='/task/fixtures/round-02/'
for i,l in enumerate(open(d+'board.md').read().splitlines(),1):print('B',i,l)
for f in sorted(glob.glob(d+'logs/*.log')):
  L=open(f).read().splitlines()
  e=[(i,l[:120]) for i,l in enumerate(L,1) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(os.path.basename(f),len(e))
  for x in e[:4]:print(' ',*x)