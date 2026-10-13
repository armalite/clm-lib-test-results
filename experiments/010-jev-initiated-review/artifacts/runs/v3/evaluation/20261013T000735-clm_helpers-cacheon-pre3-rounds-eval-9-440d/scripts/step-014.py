import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR3: board Thread A DNS_RESOLUTION ledger-svc+inventory-svc ongoing (round-03/board.md:3); follow-up OPEN POSTMORTEM_DRAFT (round-03/board.md:4). No changes.md. Errors SERVFAIL geo.internal: round-03/logs/ledger-svc.log:14-31,64-67; round-03/logs/inventory-svc.log:1-19,26-41,54. search-api still no errors. Next: advance to round 4."
c['entries']=[n]
json.dump(c,open(p,'w'))