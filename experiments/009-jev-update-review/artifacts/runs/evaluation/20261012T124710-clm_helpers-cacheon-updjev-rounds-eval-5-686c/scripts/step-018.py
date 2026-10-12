import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace(' NEXT: advance to R7.','')
n+="\nR7: Thread A RESOLVED (round-07/board.md:3). Thread B cause revised CERT_EXPIRED auth-svc (round-07/board.md:4). OPEN ALERT_TUNING (board:5)."
for s in ['checkout-api','auth-svc','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-07/logs/{s}.log'),1):
    if re.search(r'ERROR|exhaust|certif|429|disk|lag',l,re.I): print(s,i,l.strip()[:110])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))