import json,re
b='/task/fixtures/round-05/logs/'
for f in ['auth-svc.log','search-api.log']:
  L=open(b+f).read().splitlines()
  print(f,[i for i,l in enumerate(L,1) if re.search('pool',l)])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=" R5: board A mitigated (round-05/board.md:3) after CHG-143 APPLIED auth-svc (round-05/changes.md:4). Board B adds checkout-api (board.md:4). 429 fx-rates payments-svc.log:13,19; checkout-api.log:21,23,30. Follow-up OPEN CAPACITY_REVIEW (board.md:5). CHG-138 TLS irrelevant."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))