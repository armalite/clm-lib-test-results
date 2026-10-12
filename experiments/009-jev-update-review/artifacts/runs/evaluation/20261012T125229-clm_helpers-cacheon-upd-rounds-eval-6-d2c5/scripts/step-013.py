import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|429|disk|used_pct|cache|miss|WARN',l,re.I) and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:110])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR5: board.md:3 follow-up OPEN VENDOR_TICKET.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))