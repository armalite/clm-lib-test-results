import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] not in('s1.obs','s1.act')]
c['entries'].insert(0,{'id':'n1','role':'note','body':'R1: board empty; logs (notify-worker,shipping-svc,ledger-svc,inventory-svc,search-api) only routine WARN slow query ms 200-450, no errors. changes.md exists (check).'})
json.dump(c,open(p,'w'))
print(open('/task/fixtures/round-01/changes.md').read()[:1500])