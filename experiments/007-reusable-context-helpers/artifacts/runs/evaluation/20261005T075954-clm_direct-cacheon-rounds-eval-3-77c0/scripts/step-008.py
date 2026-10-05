import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" | R3: board empty. CHG-125 APPLIED retry budget (irrelevant). cert errs continue: inventory-svc.log:9-71, ledger-svc.log:23-69. no other errors."
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')