import json,glob
for i,l in enumerate(open('/task/fixtures/round-11/board.md'),1):print(i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
    L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'INFO' not in l and 'slow query' not in l]
    print(f.split('/')[-1],len(L),L[:1],L[-1:] if L else '')
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open(p,'w'))