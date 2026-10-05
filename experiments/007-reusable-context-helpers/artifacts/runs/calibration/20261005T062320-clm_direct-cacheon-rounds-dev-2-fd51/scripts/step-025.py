import json,re
L=open('/task/fixtures/round-08/logs/search-api.log').readlines()
a=[i for i,l in enumerate(L,1) if '429' in l];b=[i for i,l in enumerate(L,1) if 'config validation' in l]
print(a,b)
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']+="\nR8: board (round-08/board.md): Thread A resolved :3; Thread B mitigated :4; Thread C search-api failures cause unknown ongoing :5; Follow-up OPEN DATA_BACKFILL :6; CLOSED VENDOR_TICKET :7. search-api config validation failed http.max_inflight=-1 (CHG-120 BAD_CONFIG) lines %s; 429 lines %s. CERT auth round-08/logs/auth-svc.log:8,61; shipping round-08/logs/shipping-svc.log:50,60. No DNS. Next: advance R9."%(b,a)
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))