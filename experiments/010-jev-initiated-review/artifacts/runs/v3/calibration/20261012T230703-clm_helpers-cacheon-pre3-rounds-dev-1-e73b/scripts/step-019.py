import json
c=json.load(open('context.json'))
e={x['id']:x for x in c['entries']}
n5='R5: board Thread A mitigated (round-05/board.md:3) after CHG-143 APPLIED auth-svc mitigation (round-05/changes.md:4). Thread B services +checkout-api (board.md:4). Follow-up OPEN CAPACITY_REVIEW (board.md:5). CHG-138 TLS noise. Logs: no db pool errors r5; 429 fx-rates payments-svc round-05/logs/payments-svc.log:13-73, checkout-api round-05/logs/checkout-api.log:21-65. notify-worker clean.'
c['entries']=[e['n1'],e['n2'],e['n3'],e['n4'],{'id':'n5','role':'note','body':n5}]
json.dump(c,open('context.json','w'))
print('ok')