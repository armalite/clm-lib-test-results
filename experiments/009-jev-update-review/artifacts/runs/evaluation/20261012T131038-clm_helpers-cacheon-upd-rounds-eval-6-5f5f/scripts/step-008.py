import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'][-1]['body']+=' R3 logs: 429 fx-rates continues inventory-svc.log:13,74 ledger-svc.log:7,68; no payments-svc/pricing errors in R3 (stampede unconfirmed). Next: advance to R4.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')