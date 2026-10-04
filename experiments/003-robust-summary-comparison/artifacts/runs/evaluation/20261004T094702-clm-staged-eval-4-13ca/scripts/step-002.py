import json,re,collections
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy payments-api 6.25.3-646f at 08:14:28 (stage-1/deploy/deploys.log:1). Release notes stage-1/deploy/release-notes-6.25.3-646f.md:5 tax-engine timeout 2500->800; :17 db.pool.max_size 48->10. Repo config yaml:7 timeout 2500, :11 pool 48. ingress-a.log 503 upstream timeout from line 80. oncall suspects tax timeout (informal).'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-1/logs/payments-api.log'
c=collections.Counter();first={}
for i,l in enumerate(open(b),1):
  k=re.sub(r'\d+','N',l[25:120])
  c[k]+=1
  first.setdefault(k,i)
for k,n in c.most_common(15):print(n,first[k],k)