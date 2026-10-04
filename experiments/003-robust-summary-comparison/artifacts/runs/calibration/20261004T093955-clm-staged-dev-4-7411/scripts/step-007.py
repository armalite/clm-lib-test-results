import json
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log').read().splitlines()):print(i+1,l[:220])
L=open(b+'logs/profile-svc.log').read().splitlines()
x=[(i+1,l[:150]) for i,l in enumerate(L) if 'pool' in l];print(len(x),x[:2])
G=open(b+'logs/api-gateway.log').read().splitlines()
g=[(i+1,l[:160]) for i,l in enumerate(G) if '503' in l];print(len(g),g[:1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']+[{'id':'n2','role':'note','body':'S2: changes.log:4 CHG-5482 APPLIED ledger timeout=4000 (fixed timeouts). S2 profile-svc.log:234 db pool exhausted 14/14. Stage3 released.'}]
json.dump(c,open('/task/workspace/context.json','w'))