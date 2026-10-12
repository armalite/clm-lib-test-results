import json,re
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for s in ['auth-svc','shipping-svc','search-api','checkout-api','inventory-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    e=[(i+1,l[:140]) for i,l in enumerate(L) if re.search('ERROR|error|429|fail|cert|expired',l,re.I)]
    print(s,len(e),[x[0] for x in e]);
    for x in e[:2]: print(x)
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
json.dump(d,open(p,'w'))