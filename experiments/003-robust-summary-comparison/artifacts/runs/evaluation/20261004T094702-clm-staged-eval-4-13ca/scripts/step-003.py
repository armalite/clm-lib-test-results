import json,re
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy payments-api 6.25.3-646f at 08:14:28 (stage-1/deploy/deploys.log:1). Release notes stage-1/deploy/release-notes-6.25.3-646f.md:5 tax-engine timeout 2500->800; :17 db.pool.max_size 48->10. Repo config yaml:7 timeout 2500, :11 pool 48. ingress-a.log 503 upstream timeout from line 80. payments-api.log: tax-engine timed out errors first at line 153 (~95 total); no pool errors in top15. oncall suspects tax timeout (informal).'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-1/logs/payments-api.log'
L=open(b).read().splitlines()
for i in (153,154,196):print(i,L[i-1][:200])
for i,l in enumerate(L,1):
  if re.search(r'pool|latency|took',l,re.I):print(i,l[:160]);break