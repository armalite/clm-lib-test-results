import json
e=json.load(open('/task/workspace/context.json'))['entries']
n1=e[0];n2=e[1]
n3={'id':'n3','role':'note','body':'Round3: board: Thread A opened DNS_RESOLUTION ledger-svc, impact also inventory-svc, ongoing (round-03/board.md:3). Follow-up OPEN POSTMORTEM_DRAFT (round-03/board.md:4). Logs: inventory-svc DNS SERVFAIL geo.internal round-03/logs/inventory-svc.log:1,10,11,16,19,26,28,34,41,54; ledger-svc round-03/logs/ledger-svc.log:14,17,25,31,64,67. No search-api errors yet.'}
json.dump({'format':'clm-context/v1','entries':[n1,n2,n3]},open('/task/workspace/context.json','w'))
print('ok')