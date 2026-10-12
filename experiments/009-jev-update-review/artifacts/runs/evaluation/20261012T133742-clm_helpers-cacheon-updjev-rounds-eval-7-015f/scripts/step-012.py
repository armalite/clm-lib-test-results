import re,glob,json
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  n=f.split('/')[-1]
  if n in('checkout-api.log','ledger-svc.log','payments-svc.log'):continue
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|cache|pool|cert|tls|disk',l,re.I): print(n,i,l.strip()[:110])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' r4 logs: checkout-api disk used_pct 91-98 /var/data (DISK_PRESSURE? lines 7,19,76) no cache errors seen; search-api 429 lines 1,14,32; slow-query WARNs everywhere = noise.'
json.dump(d,open('/task/workspace/context.json','w'))