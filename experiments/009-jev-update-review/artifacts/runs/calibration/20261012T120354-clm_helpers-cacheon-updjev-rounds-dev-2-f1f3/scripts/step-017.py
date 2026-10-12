import json,re
L=open('/task/fixtures/round-07/logs/search-api.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|max_inflight|WARN',l)]
print(len(h),h[:15])
for i in h[:3]:print(L[i-1][:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n3':e['body']=e['body'].replace('BUT logs show','(R7 board revised to CERT_EXPIRED, round-07/board.md:3) logs:')
  if e['id']=='n5':e['body']=e['body'].replace('(board cause still DB_POOL, logs say CERT_EXPIRED)','(cause now CERT_EXPIRED per round-07/board.md:3)')
c['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B cause=CERT_EXPIRED. board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing (verify vs CHG-120 max_inflight=-1 BAD_CONFIG). R7 auth/shipping cert errors continue.'})
json.dump(c,open('/task/workspace/context.json','w'))