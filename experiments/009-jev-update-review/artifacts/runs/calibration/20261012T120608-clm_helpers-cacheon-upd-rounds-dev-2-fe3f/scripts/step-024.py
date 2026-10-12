import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR9 logs: cert auth round-09/logs/auth-svc.log:22,55; shipping round-09/logs/shipping-svc.log:28,56; search-api 429 :1,5 + config :2; no DNS.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  try:
    for i,l in enumerate(open('/task/fixtures/round-09/'+f),1): print(f,i,l.rstrip()[:200])
  except Exception as e: print(e)