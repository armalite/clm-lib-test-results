import json
n=open('/task/workspace/context.json').read()
d=json.loads(n)
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b=b.replace(' Next: advance to round 5.','')
b+='\nRound5: board.md:3 Thread A mitigated (auth-svc DB pool); board.md:4 Thread B adds checkout-api; board.md:5 OPEN CAPACITY_REVIEW. changes.md:4 CHG-143 APPLIED thread A mitigation auth-svc; CHG-138 TLS hourly (irrelevant?). checkout-api 429 fx-rates r05 lines 21,23. notify-worker r5 only slow-query WARNs so far (check lines 26-70 for errors). Next: inspect r5 non-slow-query errors, then advance.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))
import re
for s in ['auth-svc','notify-worker','payments-svc','search-api']:
  L=open('/task/fixtures/round-05/logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[21:120]) for i,l in enumerate(L) if re.search('ERROR|error|fail|429|exhaust',l) and 'slow query' not in l]
  print(s,[x[0] for x in e]);[print(x) for x in e[:2]]