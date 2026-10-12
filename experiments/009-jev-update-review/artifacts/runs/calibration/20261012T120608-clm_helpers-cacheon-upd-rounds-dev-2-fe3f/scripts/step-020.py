import json
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+='\nR8: board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api failures cause unknown ongoing; :6 OPEN DATA_BACKFILL; :7 CLOSED VENDOR_TICKET.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if any(k in l.lower() for k in ['error','429','cert','inflight','servfail','fail']):print(f.split('/')[-1],i,l.strip()[:150])