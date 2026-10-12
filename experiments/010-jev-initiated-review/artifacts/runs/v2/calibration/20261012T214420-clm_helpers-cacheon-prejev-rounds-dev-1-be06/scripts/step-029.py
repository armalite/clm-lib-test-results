import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board empty (no changes). No changes.md. 429 fx-rates continue: checkout-api round-07/logs/checkout-api.log:11-66; payments-svc round-07/logs/payments-svc.log:1-36,71-82. auth/search/notify clean. Next: advance R8.'})
json.dump(c,open(p,'w'))
print('ok')