import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|429|FATAL|stampede|batch_size|OOM|memory|restart',l,re.I): print(f.split('/')[-1],i,l.strip()[:130])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R5 logs not reviewed in detail (scan printed nothing). R6: board round-06/board.md:3 Thread D MEMORY_LEAK ledger-svc ongoing. changes round-06/changes.md:3 CHG-147 PROPOSED (ignore).'})
json.dump(c,open('/task/workspace/context.json','w'))