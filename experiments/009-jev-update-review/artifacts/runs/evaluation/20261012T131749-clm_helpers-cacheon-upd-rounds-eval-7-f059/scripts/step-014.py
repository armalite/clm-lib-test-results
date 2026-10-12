import json,glob,re,collections
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    cnt=collections.Counter();ex={}
    for i,l in enumerate(open(f),1):
        if ('WARN' in l or 'ERROR' in l or 'error' in l.lower()) and 'slow query' not in l:
            k=re.sub(r'\d+','N',l)[:90];cnt[k]+=1;ex.setdefault(k,[]).append(i)
    print(f.split('/')[-1])
    for k,v in cnt.items():print(' ',v,ex[k][:4],k)
print(open('/task/fixtures/round-05/board.md').read())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R5: changes.md:3 CHG-137 PROPOSED (not applied, ignore).'
json.dump(c,open('/task/workspace/context.json','w'))