import json,collections
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy payments-api 5.36.1-f33d at 08:18:43 (stage-1/deploy/deploys.log:4). Release notes stage-1/deploy/release-notes-5.36.1-f33d.md:13 risk-score timeout 2500->800; :16 db.pool.max_size 60->14. config yaml: timeout 2500 (line7), pool 60 (line11). ingress-a 503 upstream timeout from line 91 (08:20). oncall suspects risk-score timeout (informal).'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-1/logs/payments-api.log'
c=collections.Counter();first={}
import re
for i,l in enumerate(open(b),1):
  p=l.split()
  if len(p)<3 or 'INFO' in l:continue
  k=re.sub(r'\d+','N',' '.join(p[2:])[:80])
  c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(15):print(v,first[k],k)