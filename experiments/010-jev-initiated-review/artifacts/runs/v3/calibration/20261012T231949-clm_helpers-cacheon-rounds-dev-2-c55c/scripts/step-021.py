import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board Thread B cause revised CERT_EXPIRED (round-07/board.md:3). Thread D UPSTREAM_RATE_LIMIT search-api ongoing (round-07/board.md:4). search-api upstream errors round-07/logs/search-api.log:4,5,20,22,25 (verify 429 vs max_inflight CHG-120). CERT continues auth round-07/logs/auth-svc.log:1,16,24; shipping round-07/logs/shipping-svc.log:10,11,23.'})
json.dump(c,open('/task/workspace/context.json','w'))
L=open('/task/fixtures/round-07/logs/search-api.log').read().splitlines()
for i in (4,5,20):print(i,L[i-1][:300])
import os;print(os.listdir('/task/fixtures/round-07'))