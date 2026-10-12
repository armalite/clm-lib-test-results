import json
for s in ['checkout-api','ledger-svc','auth-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').readlines()
  h=[i+1 for i,l in enumerate(L) if 'ERROR' in l or 'WARN' in l]
  print(s,h[:8],L[h[0]-1][:160] if h else '')
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+'\nR11: Thread B adds ledger-svc (round-11/board.md:3), B MITIGATED (round-11/board.md:4). Thread C still ongoing (board:5). CUSTOMER_COMMS CLOSED (board:6). CHG-179 PROPOSED ignore.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))