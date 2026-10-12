import json,re
L=open('/task/fixtures/round-10/logs/notify-worker.log').read().splitlines()
hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'WARN|ERROR',l)]
for h in hits[:14]:print(h)
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R10: board.md:3 Thread B adds payments-svc; board.md:4 Thread C notify-worker failures cause unknown ongoing; board.md:5 OPEN DATA_BACKFILL; board.md:6 OPEN POSTMORTEM_DRAFT; CHG-173 minor.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))