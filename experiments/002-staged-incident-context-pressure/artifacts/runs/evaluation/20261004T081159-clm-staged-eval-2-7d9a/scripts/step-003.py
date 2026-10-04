import json,re
b='/task/fixtures/stage-1/logs/payments-api.log'
L=open(b).read().splitlines()
for i in (179,191,222):print(i,L[i-1][:200])
print(sum('pool' in l for l in L))
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy payments-api 5.36.1-f33d at 08:18:43 (stage-1/deploy/deploys.log:4). Release notes stage-1/deploy/release-notes-5.36.1-f33d.md:13 risk-score timeout 2500->800; :16 db.pool.max_size 60->14. config yaml: timeout 2500 (line7), pool 60 (line11). ingress-a 503 upstream timeout from line 91 (08:20). payments-api.log: risk-score timed out errors start line 179 (95 total); noise: gc, tls expire warnings, disk, dns retry ok.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))