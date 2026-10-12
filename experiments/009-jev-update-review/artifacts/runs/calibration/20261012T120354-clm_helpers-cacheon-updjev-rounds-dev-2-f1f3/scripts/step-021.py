import json,re
L=open('/task/fixtures/round-08/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if re.search(r'(?i)error|inflight|429|fail',l): print(i,l[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A (DNS) RESOLVED. board.md:4 Thread B (CERT) MITIGATED. board.md:5 Thread C search-api pod failures, cause unknown, ongoing. board.md:6 DATA_BACKFILL OPEN. board.md:7 VENDOR_TICKET CLOSED.'})
json.dump(c,open('/task/workspace/context.json','w'))