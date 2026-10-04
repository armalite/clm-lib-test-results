import json
b='/task/fixtures/stage-1/logs/billing-svc.log'
L=open(b).readlines()
for i,l in enumerate(L,1):
 if 'db pool' in l:print(i,l.strip()[:200])
idx=[i for i,l in enumerate(L,1) if 'timed out' in l];print(idx[0],idx[-1])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: billing-svc 6.24.0-4314 deployed 08:15:41 (stage-1/deploy/deploys.log:5). Release notes: pricing-core timeout_ms 2500->800 (release-notes-6.24.0-4314.md:9); db.pool.max_size 48->10 (line 18). Repo config timeout 2500 (config:7), pool 48 (config:11). billing log: 95 ERROR pricing-core timed out after 800ms first at stage-1/logs/billing-svc.log:152; 7 WARN db pool wait. Oncall suspects timeout. Noise: gc, disk, tls, dns warns.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))