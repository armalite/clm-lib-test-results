import json,re,collections
b='/task/fixtures/stage-1/'
note='''S1 facts: release-notes-8.15.4-7744.md:11 ledger timeout 2500->600; :17 db pool 48->14. deploys.log:5 profile-svc 8.15.4-7744 at 08:13:01. config yaml:7 timeout 2500, :11 pool 48. profile-svc.log:131 ledger timed out 600ms; :132 db pool wait in_use 14/14. oncall suspects ledger timeout (informal).'''
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))
for f in ['logs/profile-svc.log','logs/api-gateway.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or 'pool' in l or 'ledger' in l:
      k=re.sub(r'\d+','N',l[60:140]);c[k]+=1;first.setdefault(k,i)
  for k,v in c.most_common(8):print(f,first[k],v,k)