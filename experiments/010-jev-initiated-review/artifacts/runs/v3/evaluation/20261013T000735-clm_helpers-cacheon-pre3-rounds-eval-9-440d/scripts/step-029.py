import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR5 shipping-svc: tls cert expired peer=bank-api round-05/logs/shipping-svc.log:1,7,11,17,37-65 (CERT_EXPIRED confirmed); disk high shipping too :4,18,56,60. Round 6 released."
c['entries']=[n]
json.dump(c,open(p,'w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1): print(f,i,l.strip())
