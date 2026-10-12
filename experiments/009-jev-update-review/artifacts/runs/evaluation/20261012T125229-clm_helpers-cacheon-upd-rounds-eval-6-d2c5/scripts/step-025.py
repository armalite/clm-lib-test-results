import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR9: board.md:3 Thread B +checkout-api; :4 Thread B mitigated; :5 Thread C ongoing; :6 Thread D false alarm (drop MEMORY_LEAK); :7 DATA_BACKFILL CLOSED.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if any(k in l for k in ['ERROR','used_pct','batch_size','429']):
      print(f.split('/')[-1],i,l.strip()[:110])