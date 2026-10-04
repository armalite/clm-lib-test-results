import json,collections
b='/task/fixtures/stage-1/logs/'
L=open(b+'payments-api.log').readlines()
c=collections.Counter(l.split()[1] for l in L);print(c)
for i,l in enumerate(L,1):
 if 'pool' in l.lower() or 'upstream latency' in l.lower():print(i,l.strip()[:160]);break
I=open(b+'ingress-a.log').readlines()
print(collections.Counter(l.split('status=')[1].split()[0] for l in I if 'status=' in l))
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: RN 5.36.1-f33d line13 risk timeout 2500->800; line16 db pool 60->14. deploy deploys.log:4 08:18:43. payments-api.log:179 first ERROR risk timeout 800ms (95 such errors, only ERROR type); :206 db pool wait 14/14. config yaml:7 timeout 2500, :11 pool 60. oncall suspects timeout.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))