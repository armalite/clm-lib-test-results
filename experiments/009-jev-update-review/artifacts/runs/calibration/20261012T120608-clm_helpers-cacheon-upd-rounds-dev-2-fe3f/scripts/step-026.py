import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR10: board.md:3 Thread D closed FALSE ALARM (but 429s seen in logs? verify); :4 CLOSED DATA_BACKFILL; CHG-175 noise.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
import re
for s in ['search-api','auth-svc','shipping-svc','checkout-api','inventory-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[(i,l[:150]) for i,l in enumerate(L,1) if re.search('429|config|cert|SERVFAIL|ERROR',l,re.I)]
  print(s,len(h));[print(x) for x in h[:4]]