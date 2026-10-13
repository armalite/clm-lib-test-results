import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[{'id':'n1','role':'note','body':'Round1: board.md empty (2 lines header). changes.md 3 lines (see below). Logs notify-worker,shipping-svc,ledger-svc,inventory-svc,search-api: only routine WARN slow query ms 200-450 across all; no errors. Nothing incident-like yet.'}]
json.dump(c,open(p,'w'))
print(open('/task/fixtures/round-01/changes.md').read())