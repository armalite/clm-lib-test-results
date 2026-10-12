import json
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']=n['body'].replace(' R9 logs: see step26 obs.',' R9 logs: checkout-api disk used_pct=92 checkout-api.log:31-53; payments disk 95 payments-svc.log:11-38; pricing batch_size=0 errors pricing-svc.log:7-56; ledger no heap, no 429. NEXT: advance to R10.')
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')