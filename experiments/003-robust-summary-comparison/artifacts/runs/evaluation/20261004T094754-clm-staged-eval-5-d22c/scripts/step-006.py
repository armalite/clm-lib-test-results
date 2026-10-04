import json
b='/task/fixtures/stage-2/logs/quotes-api.log'
L=open(b).readlines();print(L[284].rstrip());print(L[300].rstrip())
I=open('/task/fixtures/stage-2/logs/ingress-a.log').readlines()
x=[i for i,l in enumerate(I,1) if 'status=5' in l];print(x[:3],I[x[0]-1].rstrip())
n=open('/task/workspace/context.json').read()
c=json.loads(n)
c['entries']=[c['entries'][0],{'id':'n2','role':'note','body':'S2: CHG-5489 APPLIED timeout=3500 changes.log:2 fixed timeouts. Now db pool errors quotes-api.log (stage-2) first line 285; metrics pool in_use 12 (max 12 from release notes :16). ingress-a stage2 5xx: '+str(x[:3])}]
json.dump(c,open('/task/workspace/context.json','w'))