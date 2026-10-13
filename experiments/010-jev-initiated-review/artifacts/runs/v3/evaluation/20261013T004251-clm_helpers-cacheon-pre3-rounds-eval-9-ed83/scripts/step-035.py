import json,re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    hits=[i for i,l in enumerate(open(f),1) if re.search(r'ERROR|429|fail|expired|OOM|lag|pool|inflight|SERVFAIL',l)]
    d=[i for i,l in enumerate(open(f),1) if 'disk' in l.lower()]
    print(f.split('/')[-1],'err',hits[:15],'disk',d[:3],d[-1:] )
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open(p,'w'))