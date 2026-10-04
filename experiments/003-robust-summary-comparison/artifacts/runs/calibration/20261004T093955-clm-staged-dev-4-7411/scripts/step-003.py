import json,re
b='/task/fixtures/stage-1/'
L=open(b+'logs/profile-svc.log').read().splitlines()
t=[i+1 for i,l in enumerate(L) if 'timed out' in l];p=[i+1 for i,l in enumerate(L) if 'pool wait' in l]
print(len(t),t[:3],t[-3:],len(p),p)
lat=[l for l in L if 'ledger' in l and 'ms' in l and 'timed out' not in l][:3];print(lat)
G=open(b+'logs/api-gateway.log').read().splitlines()
print([ (i+1,l[:150]) for i,l in enumerate(G) if ' 5' in l and 'profile' in l][:3])
note=open('/task/workspace/context.json').read()
c=json.loads(note);c['entries']=[e for e in c['entries'] if e['id']=='n1'];json.dump(c,open('/task/workspace/context.json','w'))