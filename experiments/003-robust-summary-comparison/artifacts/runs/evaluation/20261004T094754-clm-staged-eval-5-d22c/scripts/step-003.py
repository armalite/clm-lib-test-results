import json,re
b='/task/fixtures/stage-1/logs/'
I=open(b+'ingress-a.log').readlines()
x=[i for i,l in enumerate(I,1) if 'status=5' in l];print(len(x),x[:3])
L=open(b+'quotes-api.log').readlines()
print([i for i,l in enumerate(L,1) if 'db pool' in l][:7])
n='S1: rates timeout default 2500->600 in release-notes-7.20.4-0a00.md:8 (deploy deploys.log:4 08:16). db pool 48->12 at :16. quotes-api.log:139 first rates-svc timeout 600ms (95 such). db pool wait warns 7. oncall suspects timeout. ingress 5xx lines: '+str(x[:5])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))