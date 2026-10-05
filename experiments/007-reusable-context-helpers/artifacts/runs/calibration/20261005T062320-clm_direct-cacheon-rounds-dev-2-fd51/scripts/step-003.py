import json,re,glob
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: CHG-107 APPLIED retry budget GETs=1 (round-01/changes.md:3). Board empty. slow query WARNs everywhere = noise. inventory-svc DNS SERVFAIL host=rates.internal round-01/logs/inventory-svc.log:7,20,50-90 (DNS_RESOLUTION candidate).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL',l) and 'dns' not in l: print(f.split('/')[-1],i,l.strip()[:140])