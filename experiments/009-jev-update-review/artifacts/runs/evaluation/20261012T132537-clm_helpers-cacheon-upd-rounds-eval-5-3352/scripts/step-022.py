import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+='\nR9 logs: auth cert_expired (round-09/logs/auth-svc.log:6,71); checkout/search/shipping quiet. R9 board/changes not yet checked.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  try:
    for i,l in enumerate(open('/task/fixtures/round-09/'+f),1): print(f,i,l.rstrip())
  except Exception as x: print(f,'none')