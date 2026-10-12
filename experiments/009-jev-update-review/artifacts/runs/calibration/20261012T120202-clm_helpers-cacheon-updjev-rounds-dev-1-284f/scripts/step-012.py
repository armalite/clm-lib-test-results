import json,re
for s in ['payments-svc','checkout-api','auth-svc','search-api','notify-worker']:
    L=open(f'/task/fixtures/round-05/logs/{s}.log').read().splitlines()
    e=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error',l)]
    print(s,len(e),e[:2])
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b+=' R5: Thread A mitigated (round-05/board.md:3) via CHG-143 auth-svc (round-05/changes.md:4); Thread B +checkout-api (round-05/board.md:4); OPEN CAPACITY_REVIEW (round-05/board.md:5); CHG-138 APPLIED TLS hourly (round-05/changes.md:3).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))