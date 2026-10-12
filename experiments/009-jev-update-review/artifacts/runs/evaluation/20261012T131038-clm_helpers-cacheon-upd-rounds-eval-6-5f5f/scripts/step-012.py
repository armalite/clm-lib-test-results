import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|429|FATAL|stampede|batch_size|miss',l): print(f.split('/')[-1],i,l.strip()[:140])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: board round-05/board.md:3 follow-up OPEN VENDOR_TICKET.'})
json.dump(c,open('/task/workspace/context.json','w'))