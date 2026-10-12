import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']=e['body'].replace('Next: advance to R8.','R7 board/changes empty. R8 board:3 Thread A resolved; board:4 Thread B cause revised DB_POOL_EXHAUSTED (inventory-svc); board:5 Thread D false alarm (drop). Next: R8 logs then advance R9.')
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
    hits={}
    for i,l in enumerate(open(f),1):
        if re.search('WARN|ERROR',l):
            k=re.sub(r'[0-9]+','#',l)[-60:].strip()
            hits.setdefault(k,[]).append(i)
    for k,v in hits.items(): print(f.split('/')[-1],v,k)