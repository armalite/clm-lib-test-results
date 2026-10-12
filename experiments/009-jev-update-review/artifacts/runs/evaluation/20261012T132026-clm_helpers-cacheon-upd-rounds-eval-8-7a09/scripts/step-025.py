import json,re
for s in ['notify-worker','payments-svc','inventory-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|FAIL|exhaust|invalid|pool',l,re.I)]
  print(s,len(h));[print(x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+='\nR10: board.md:3 Thread B adds payments-svc; board.md:4 Thread C notify-worker request failures cause unknown ongoing; board.md:5 OPEN DATA_BACKFILL; board.md:6 OPEN POSTMORTEM_DRAFT; changes.md:3 CHG-173 noise.'
json.dump(c,open('/task/workspace/context.json','w'))