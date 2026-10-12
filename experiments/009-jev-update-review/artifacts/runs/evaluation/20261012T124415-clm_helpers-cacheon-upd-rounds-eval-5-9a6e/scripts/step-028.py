import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|exhaust|expired|handshake|disk|OOM|lag|invalid|config',l): print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R9 logs: auth-svc tls handshake failed bank-api round-09/logs/auth-svc.log:6,18,22,25. R10: board.md:3 Thread C checkout-api request failures cause unknown ongoing; CHG-173 PROPOSED ignore.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))