import json,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f).read().splitlines()):print(f,i+1,l)
for s in ['auth-svc','inventory-svc','notify-worker','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    d={}
    for i,l in enumerate(L):
        if re.search('WARN|ERROR',l):
            k=re.sub(r'[0-9]','',l)[20:80]
            d.setdefault(k,[]).append(i+1)
    for k,v in d.items():print(s,v[:6],len(v),k)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
json.dump(c,open('/task/workspace/context.json','w'))