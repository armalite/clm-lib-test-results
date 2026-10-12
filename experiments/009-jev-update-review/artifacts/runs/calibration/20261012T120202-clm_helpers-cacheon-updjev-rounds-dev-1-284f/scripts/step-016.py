import json,re
for s in ['payments-svc','checkout-api','auth-svc','search-api','notify-worker']:
    L=open(f'/task/fixtures/round-07/logs/{s}.log').read().splitlines()
    e=[(i+1,l[:100]) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l)]
    print(s,len(e),e[:2])
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b+=' R6 logs: 429 fx-rates payments-svc round-06/logs/payments-svc.log:3, checkout-api round-06/logs/checkout-api.log:19. R7: board/changes nothing new.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))