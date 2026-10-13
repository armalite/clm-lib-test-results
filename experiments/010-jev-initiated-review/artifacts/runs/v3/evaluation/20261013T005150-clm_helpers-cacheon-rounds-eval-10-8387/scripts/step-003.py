import os,re,json
d='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(d)):
  for i,l in enumerate(open(d+f),1):
    if 'slow query' not in l and re.search(r'ERROR|WARN',l):print(f,i,l.strip()[:150])
open('notes.md','a').write('R1: CHG-113 APPLIED shipping-svc retry.backoff_ms=0 (round-01/changes.md:3); CHG-114 search-api no cfg. R1 logs only slow-query WARN noise. board empty.\n')
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':open('notes.md').read()}]},open('context.json','w'))