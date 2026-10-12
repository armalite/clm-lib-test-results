import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+='\nR7 logs: inventory-svc.log:1 db pool exhausted 9 hits (continues); notify-worker.log:7 dns SERVFAIL geo.internal 6 hits. others slow query noise.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import os
for f in ['board.md','changes.md']:
    p='/task/fixtures/round-07/'+f
    if os.path.exists(p):
        for i,l in enumerate(open(p),1):print(f,i,l.rstrip())