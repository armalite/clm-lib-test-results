import json,re,collections
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']=e['body'].replace(' NEXT: advance to R11.','')+' R11 board:3 Thread B mitigated; :4 Thread C pods restarting ongoing. changes:3 CHG-182 irrelevant.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
    d=collections.defaultdict(list)
    for i,l in enumerate(open(f),1):
        if 'WARN' in l or 'ERROR' in l:
            m=re.search(r'msg\W+([^"]+)',l); k=m.group(1)[:40] if m else l[:60]
            if 'slow' not in k: d[k].append(i)
    print(f.split('/')[-1],dict(d))