import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: board empty; changes none? auth-svc cert_expired continues (round-09/logs/auth-svc.log:6-71); checkout clean; others clean. R9 done; next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))
import os;print(os.path.exists('/task/fixtures/round-09/changes.md'))