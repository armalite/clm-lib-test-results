import json,re
for s in ['auth-svc','search-api','shipping-svc']:
  try:
    for i,l in enumerate(open(f'/task/fixtures/round-08/logs/{s}.log'),1):
      if re.search('(?i)cert|tls|disk|ERROR',l):print(s,i,l.strip()[:120])
  except Exception as e:print(e)
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+"\nR8 logs: checkout-api has 75 lines with no pool/error lines, so Thread D false alarm is consistent (round-08/board.md:3); drop D unless it recurs. NEXT: advance to R9."
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))