import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
b=n1['body']
i=b.find(' Round8 released')
if i>0:b=b[:i]
b+=" Round8: round-08/board.md:3 Thread A resolved; :4 Thread B cause revised UPSTREAM_RATE_LIMIT; :5 Thread C pricing-svc failures ongoing cause unknown. No changes.md r8. r8 429 checkout-api.log:26,27,37,51,60,66; ledger-svc.log:9,12,21,30,35,45,48,58,62,76. pricing-svc 'config validation failed' key cache.ttl_s pricing-svc.log:5,17,28 (+more) -> Thread C = BAD_CONFIG_ROLLOUT from CHG-113 round-01/changes.md:4. Next: grep pricing-svc.log r8 rest, then advance round 9."
n1['body']=b
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))
import subprocess
for n,l in enumerate(open('/task/fixtures/round-08/logs/pricing-svc.log'),1):
  if 'ERROR' in l or 'WARN' in l: print(n,l[60:140].strip())