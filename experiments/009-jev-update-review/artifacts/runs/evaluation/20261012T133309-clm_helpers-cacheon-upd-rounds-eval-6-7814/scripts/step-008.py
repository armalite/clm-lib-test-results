import json,re
L=open('/task/fixtures/round-03/logs/payments-svc.log').read().splitlines()
print(len(L))
for i,l in enumerate(L[:5]): print(i+1,l[:160])
for i,l in enumerate(L):
    if re.search(r'WARN|cache|hit|latency',l,re.I): print(i+1,l[:160])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R3 logs: inventory 429s round-03/logs/inventory-svc.log:13-74; ledger round-03/logs/ledger-svc.log:7-68; pricing/checkout no errors.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))