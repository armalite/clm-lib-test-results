import json,collections,re
b='/task/fixtures/stage-1/logs/payments-api.log'
c=collections.Counter();first={}
for i,l in enumerate(open(b),1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[50:140]);c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(8):print(v,first[k],k)
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy 6.25.3-646f at 08:14 (stage-1/deploy/deploys.log:1). Release notes: tax-engine timeout 2500->800 (release-notes:5), db.pool.max_size 48->10 (release-notes-6.25.3-646f.md:17). Config yaml: timeout 2500 line7, pool 48 line11. ingress-a 503 upstream timeout from line 80. Oncall suspects tax timeout (oncall-notes.md:5-6, informal).'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))