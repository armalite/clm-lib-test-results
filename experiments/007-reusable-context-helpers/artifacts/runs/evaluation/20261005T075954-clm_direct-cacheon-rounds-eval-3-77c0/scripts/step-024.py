import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1':e['body']+=' | R8: board.md:3 B cause revised MEMORY_LEAK (checkout-api); :4 C pods restarting, continues; :5 CLOSED VENDOR_TICKET. search-api.log:2-76 config validation ERRORs http.max_inflight=-1. R8 done -> advance next.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))