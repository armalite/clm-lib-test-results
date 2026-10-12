import json,re
for s in ['ledger-svc','checkout-api','payments-svc']:
    L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search(r'pool_max|used_pct=9|ERROR',l)]
    print(s,h[:8])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' R10: board.md:3 Thread B MITIGATED; :4 Thread C still ongoing (restarting); :5 RUNBOOK_UPDATE CLOSED.'
json.dump(d,open('/task/workspace/context.json','w'))