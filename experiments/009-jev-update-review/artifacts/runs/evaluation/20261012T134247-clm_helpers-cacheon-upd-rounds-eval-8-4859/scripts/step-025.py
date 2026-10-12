import json,re,glob,collections
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']=e['body'].replace('Next: advance R9.','R9 board:3 follow-up OPEN RUNBOOK_UPDATE.')
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    d=collections.defaultdict(list)
    for i,l in enumerate(open(f),1):
        if 'slow query' in l: continue
        if re.search('WARN|ERROR|FATAL|warn|error',l):
            k=re.sub(r'[0-9]+','N',l)[:90]
            d[k].append(i)
    for k,v in d.items(): print(f.split('/')[-1],v,k.strip())