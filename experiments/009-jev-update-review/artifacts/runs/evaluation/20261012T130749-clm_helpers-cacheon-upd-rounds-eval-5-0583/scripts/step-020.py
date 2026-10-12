import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n11','role':'note','body':'R7: Thread A resolved (round-07/board.md:3). Thread B revised CERT_EXPIRED auth-svc (round-07/board.md:4). OPEN ALERT_TUNING (:5).'})
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['checkout-api','auth-svc','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-07/logs/{s}.log'),1):
    if re.search(r'ERROR|exhaust|invalid|pool_max|certificate|429|lag',l): print(s,i,l.strip()[:150])