import json,collections
L=open('/task/workspace/spill/s10.obs.txt').read().splitlines()
c=collections.Counter()
ex={}
for l in L:
    p=l.split(' ',2)
    if len(p)<3: continue
    k=(p[0],' '.join(p[2].split()[2:5])[:50])
    c[k]+=1; ex.setdefault(k,(p[1],p[2][:120]))
for k,v in c.items(): print(k[0],v,ex[k][0],ex[k][1])
n='R1: board empty; CHG-108 PROPOSED (ignore). slow-query WARNs = noise. R2: board.md:3-5 follow-ups OPEN ALERT_TUNING,RUNBOOK_UPDATE,VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker sets http.max_inflight=0 (suspect BAD_CONFIG); CHG-121 payments no cfg. R2 auth-svc.log:1-69 db pool exhausted. R3: board.md:3 Thread A DB_POOL_EXHAUSTED auth-svc+search-api ongoing; changes.md:3 CHG-125 dashboards (noise). R3 non-slow lines in spill/s10.obs.txt.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))