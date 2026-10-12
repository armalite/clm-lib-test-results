import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board no updates, no changes.md. 429 fx-rates continues: payments round-07/logs/payments-svc.log:1,7,13; checkout round-07/logs/checkout-api.log:11,19,25. auth/notify quiet. Next: advance R8.'})
json.dump(c,open('/task/workspace/context.json','w'))
import os;print(os.listdir('/task/fixtures/round-07'))