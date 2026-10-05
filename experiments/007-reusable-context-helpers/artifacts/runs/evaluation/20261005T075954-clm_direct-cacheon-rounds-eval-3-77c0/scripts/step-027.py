import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1':e['body']+=' | R9: board.md:3 B services +payments-svc; :4 B mitigated. CHG-164 irrelevant. payments-svc.log:45,55 heap WARN; checkout-api.log:27,56 heap; search-api.log:5,11,14,22 config ERR. R9 done -> advance next.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))