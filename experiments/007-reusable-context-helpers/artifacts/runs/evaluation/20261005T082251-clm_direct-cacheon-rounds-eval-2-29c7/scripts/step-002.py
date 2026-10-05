import os,json,re
b='/task/fixtures/round-01/logs/'
skip=re.compile(r'request ok|heartbeat|gc cycle|slow query|health ok')
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if not skip.search(l):print(f,i,l.strip()[:140])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes CHG-112 APPLIED log sampling /v1/health 1% (noise). Logs routine: request ok/heartbeat/gc/slow query. auth-svc heap warn rss_mb=3330 r01 auth-svc.log:3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))