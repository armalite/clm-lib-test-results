import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" | R2: board.md:3 Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing. inventory-svc.log:10-19 cert errs; ledger-svc.log:20-57. CHG-117 PROPOSED. search-api no errors seen R2."
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')