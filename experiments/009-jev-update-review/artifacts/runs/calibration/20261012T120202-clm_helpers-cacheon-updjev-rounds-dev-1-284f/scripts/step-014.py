import json,re
for s in ['payments-svc','checkout-api','auth-svc','search-api','notify-worker']:
    L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
    e=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR',l)]
    print(s,len(e),e[:2])
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b+=' R6: CLOSED ALERT_TUNING (round-06/board.md:3); OPEN CUSTOMER_COMMS (round-06/board.md:4); CHG-147 retry budget irrelevant.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))