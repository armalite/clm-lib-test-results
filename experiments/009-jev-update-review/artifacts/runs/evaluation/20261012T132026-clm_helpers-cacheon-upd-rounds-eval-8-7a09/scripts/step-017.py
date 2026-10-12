import json,glob,re,collections
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    c=collections.Counter();first={}
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|WARN|FATAL',l):
            k=re.sub(r'\d+','#',l.strip())[-90:]
            c[k]+=1;first.setdefault(k,i)
    print(f.split('/')[-1])
    for k,v in c.most_common(4):print(' ',first[k],v,k)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))