import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open(p,'w'))
for i,l in enumerate(open('/task/fixtures/round-05/logs/shipping-svc.log'),1):
  s=l.lower()
  if any(k in s for k in ['cert','pool','disk','error','tls','x509']): print(i,l.strip()[:100])
