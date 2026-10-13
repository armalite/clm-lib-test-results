import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=c['entries'][0]['body']+"\nR3: board round-03/board.md:3 Thread A DNS_RESOLUTION ledger-svc+inventory-svc ongoing; :4 follow-up OPEN POSTMORTEM_DRAFT. inventory-svc SERVFAIL geo.internal round-03/logs/inventory-svc.log:1-19,26-54; ledger round-03/logs/ledger-svc.log:14-31,64-67. No search-api errors R3."
c['entries']=[{'id':'n1','role':'note','body':n}]
json.dump(c,open(p,'w'))
print('ok')