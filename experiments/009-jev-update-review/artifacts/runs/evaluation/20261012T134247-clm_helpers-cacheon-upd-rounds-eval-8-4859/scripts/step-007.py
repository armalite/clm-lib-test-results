import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if not re.search(r'slow query',l,re.I) and re.search(r'ERROR|WARN|error|restart|OOM|cert|x509|tls',l):
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R3 board:3 Thread A MEMORY_LEAK pricing-svc (+auth-svc) ongoing; board:4 Thread B inventory-svc suspected CERT_EXPIRED ongoing. changes:3 CHG-124 APPLIED retry budget GETs=1.'
json.dump(c,open('/task/workspace/context.json','w'))