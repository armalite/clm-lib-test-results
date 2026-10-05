import json,re,os
R='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(R+f),1):print(f,i,l.rstrip())
for s in os.listdir(R+'logs'):
    L=open(R+'logs/'+s).readlines()
    d={}
    for i,l in enumerate(L,1):
        if re.search(r'ERROR|error|429|SERVFAIL|cert|config validation',l,re.I):
            k=re.sub(r'\d+','N',l[30:110]);d.setdefault(k,[]).append(i)
    for k,v in d.items():print(s,v[:6],len(v),k)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))