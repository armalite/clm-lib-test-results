import json,re
L=open('/task/fixtures/round-08/logs/search-api.log').read().splitlines()
a=[i+1 for i,l in enumerate(L) if '429' in l];b=[i+1 for i,l in enumerate(L) if 'max_inflight' in l]
print(a,b)
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'].startswith('n')]
keep.append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api failures cause unknown ongoing (logs: config validation failed http.max_inflight=-1 build 8.59.8 -> BAD_CONFIG_ROLLOUT from R2 CHG-120); :6 OPEN DATA_BACKFILL; :7 CLOSED VENDOR_TICKET. search-api 429 lines %s; config lines %s. CERT errs still round-08/logs/auth-svc.log:8,61 shipping-svc.log:50,60. No errs checkout/inventory. Next: advance.'%(a,b)})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))