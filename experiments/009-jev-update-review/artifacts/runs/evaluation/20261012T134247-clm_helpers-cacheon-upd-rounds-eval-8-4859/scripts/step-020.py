import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']=e['body'].replace('Next: advance to R7.','R7 (board/changes not yet checked separately; logs): inventory db pool exhausted 1,9,19,22,25,27,46,56,57; notify dns lookup failed 7,18,31,34,35,41; no pricing/auth WARNs. Next: advance to R8.')
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
    try:
        for i,l in enumerate(open('/task/fixtures/round-07/'+f),1): print(f,i,l.rstrip())
    except Exception as x: print(f,'none')