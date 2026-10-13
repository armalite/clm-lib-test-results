import json,re
print(open('/task/fixtures/round-10/board.md').read())
print(open('/task/fixtures/round-10/changes.md').read())
for s in ['search-api','notify-worker','shipping-svc']:
    f='/task/fixtures/round-10/logs/%s.log'%s
    h=[i for i,l in enumerate(open(f),1) if re.search(r'ERROR|inflight|fail',l)]
    d=[i for i,l in enumerate(open(f),1) if 'disk' in l.lower()]
    print(s,h[:10],'disk',d[:2],d[-1:])
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR9: board round-09/board.md:3 Thread C pods restarting; search-api errors round-09/logs/search-api.log:2-33; disk notify r09:4-8, shipping r09:8-13.'
c['entries']=[n]
json.dump(c,open(p,'w'))