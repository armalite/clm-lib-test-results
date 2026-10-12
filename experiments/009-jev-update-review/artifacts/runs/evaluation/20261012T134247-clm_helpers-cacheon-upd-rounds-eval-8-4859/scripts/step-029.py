import json,re,collections
d=collections.defaultdict(list)
for l in open('/task/workspace/spill/s28.obs.txt'):
    p=l.split(' ',2)
    if len(p)<3: continue
    m=re.search(r'(db pool exhausted|heap usage high|dns lookup failed|certificate|cert|429|rate limit|disk|queue|cache|config|pool_max|invalid)',p[2],re.I)
    d[(p[0],m.group(1) if m else p[2][:70])].append(p[1])
for k,v in d.items(): print(k,','.join(v))
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))