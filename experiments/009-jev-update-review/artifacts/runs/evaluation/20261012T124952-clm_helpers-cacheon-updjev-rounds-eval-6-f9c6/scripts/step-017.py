import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[i+1 for i,l in enumerate(L) if re.search(r'memory|heap|oom|restart|disk|used_pct|429|batch|cache|ERROR',l,re.I)]
    print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] if hits else '')
    if hits: print('  ',L[hits[0]-1][:200])
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R6: board.md:3 Thread D MEMORY_LEAK ledger-svc ongoing; changes.md:3 CHG-147 PROPOSED (ignore).'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))