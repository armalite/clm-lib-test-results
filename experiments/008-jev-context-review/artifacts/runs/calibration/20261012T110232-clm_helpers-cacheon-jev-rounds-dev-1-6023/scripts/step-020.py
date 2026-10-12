import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board no updates, no changes.md. 429 fx-rates continue round-07/logs/payments-svc.log:1-82, round-07/logs/checkout-api.log:11-66. auth/search/notify quiet. Next: advance, scan 08.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')