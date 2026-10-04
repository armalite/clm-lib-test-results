import json,collections
b='/task/fixtures/stage-1/logs/'
L=open(b+'payments-api.log').readlines()
c=collections.Counter()
for i,l in enumerate(L,1):
 if 'ERROR' in l:
  k=l.split(']')[1][:50];c[k]+=1
  if c[k]<2:print(i,l.strip()[:180])
print(c)
I=open(b+'ingress-a.log').readlines()
print(I[200].strip()[:200]);print(collections.Counter(l.split()[1] for l in I))
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: RN 5.36.1-f33d line13 risk timeout 2500->800; line16 db pool 60->14. deploy deploys.log:4 08:18:43. payments-api.log:179 risk timeout 800ms; :206 db pool wait 14/14. config yaml:7 timeout 2500, :11 pool 60. oncall suspects timeout.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))