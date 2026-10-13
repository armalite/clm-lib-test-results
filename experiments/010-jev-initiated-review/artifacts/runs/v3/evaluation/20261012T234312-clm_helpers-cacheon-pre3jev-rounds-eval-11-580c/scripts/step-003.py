import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[{'id':'n1','role':'note','body':'Round1: board.md empty. Logs (shipping-svc,checkout-api,pricing-svc,inventory-svc,search-api) only WARN slow query ms 200-450 (baseline noise). changes.md not yet read.'}]
json.dump(c,open(p,'w'))
print(open('/task/fixtures/round-01/changes.md').read()[:1500])