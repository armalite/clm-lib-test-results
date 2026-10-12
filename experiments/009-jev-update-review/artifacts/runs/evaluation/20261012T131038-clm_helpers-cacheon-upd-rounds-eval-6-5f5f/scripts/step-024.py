import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n12','role':'note','body':'R9: board round-09/board.md:3 Thread B +checkout-api; :4 Thread B mitigated; :5 Thread C still ongoing; :6 Thread D false alarm (drop MEMORY_LEAK); :7 DATA_BACKFILL CLOSED. Next: advance to R10.'})
json.dump(c,open('/task/workspace/context.json','w'))
import re
for s in ['checkout-api','payments-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-09/logs/{s}.log'),1):
    if re.search(r'disk|ERR|error',l,re.I): print(s,i,l.strip()[:120])