import json
c=json.load(open('/task/workspace/context.json'))
keep=('n1','n4','n5','n6','n7')
e=[x for x in c['entries'] if x['id'] in keep]
for x in e:
  if x['id']=='n1':x['body']='R1: CHG-113 APPLIED build 4.51.3 auth-svc sets cache.ttl_s=-1 (round-01/changes.md:4). Services shipping auth payments ledger search-api. slow query WARNs noise.'
e.insert(1,{'id':'n2','role':'note','body':'R2: board.md:3 Thread A QUEUE_BACKLOG payments-svc+ledger-svc. R3 nothing.'})
e.append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A resolved. board.md:4 Thread B cause CERT_EXPIRED. board.md:5 Thread C auth-svc ongoing cause unknown. board.md:6 OPEN ALERT_TUNING. auth-svc.log ERROR config validation failed cache.ttl_s=-1 build 4.51.3 lines 14,16,18,21 (13 total) -> BAD_CONFIG_ROLLOUT via CHG-113. CERT errors search-api.log:2,22,25,27 shipping-svc.log:4,11,19,31. Open followups: RUNBOOK_UPDATE, POSTMORTEM_DRAFT, DATA_BACKFILL, ALERT_TUNING. Next: advance R9.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))