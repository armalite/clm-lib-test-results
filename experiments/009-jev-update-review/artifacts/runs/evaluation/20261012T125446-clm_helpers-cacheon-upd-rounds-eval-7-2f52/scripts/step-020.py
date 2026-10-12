import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board empty, no changes.md checked? (board empty). Logs R7: checkout-api.log disk used_pct 92-98 lines 13,19,46,61; NEW payments-svc.log disk used_pct 91-98 lines 3,27,62,68 (DISK_PRESSURE spreading to payments-svc). No 429. R7 scanned; next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))
import os;print(os.path.exists('/task/fixtures/round-07/changes.md'))