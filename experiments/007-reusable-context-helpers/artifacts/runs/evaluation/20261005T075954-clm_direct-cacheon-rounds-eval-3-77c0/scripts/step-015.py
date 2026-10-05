import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" | R5: board.md:3 OPEN DATA_BACKFILL. no ERRORs, no 429 seen in checkout (only heap WARN checkout-api.log:6-77, possible MEMORY_LEAK). search-api.log:14-76 disk high 91-98%. R5 done -> advance next."
json.dump(c,open('/task/workspace/context.json','w'))