import json,glob,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+='\nR8: board.md:3 Thread A resolved; board.md:4 Thread B revised DB_POOL_EXHAUSTED (supersedes CERT); board.md:5 Thread D false alarm (closed). No changes.md.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    hits=[(i,l.strip()) for i,l in enumerate(open(p),1) if re.search(r'ERROR|exhaust|dns|429|cert|disk|backlog|OOM|restart',l,re.I)]
    print(p.split('/')[-1],len(hits))
    for h in hits[:2]:print(' ',h[0],h[1][:150])