import json,re
t=open('/task/fixtures/round-07/logs/search-api.log').read().splitlines()
l=[i+1 for i,x in enumerate(t) if '429' in x]
print('429',l[:40])
import os
for f in os.listdir('/task/fixtures/round-07/logs'):
  s=open('/task/fixtures/round-07/logs/'+f).read().splitlines()
  e=[i+1 for i,x in enumerate(s) if 'certificate_expired' in x or 'cert' in x and 'tls' in x]
  print(f,len(s),e[:3],e[-1:] if e else '')
print(os.path.exists('/task/fixtures/round-07/changes.md'))
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B cause revised CERT_EXPIRED (auth-svc+shipping-svc). board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing; search-api 429 upstream=tax-provider lines '+str(l[:12])+' (round-07/logs/search-api.log). cert_expired auth-svc 1-64 continues. Next: advance to round 8.'})
json.dump(c,open('/task/workspace/context.json','w'))