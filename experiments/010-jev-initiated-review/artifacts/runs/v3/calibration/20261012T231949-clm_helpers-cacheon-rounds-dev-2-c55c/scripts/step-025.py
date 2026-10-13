import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
b='/task/fixtures/round-08/logs/search-api.log'
A=[];B=[]
for i,l in enumerate(open(b),1):
  if '429' in l:A.append(i)
  if 'max_inflight' in l:B.append(i)
c['entries'].append({'id':'n8','role':'note','body':'R8: board Thread A resolved (round-08/board.md:3); Thread B mitigated (board.md:4); Thread C search-api request failures cause unknown ongoing (board.md:5); Follow-up OPEN DATA_BACKFILL (board.md:6); CLOSED VENDOR_TICKET (board.md:7). CERT errors few: auth round-08/logs/auth-svc.log:8,61; shipping round-08/logs/shipping-svc.log:50,60. search-api 429 lines %s; config validation max_inflight=-1 (CHG-120 BAD_CONFIG) lines %s. Next: advance to R9.'%(A,B)})
json.dump(c,open('/task/workspace/context.json','w'))
print(A,B)