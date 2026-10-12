import json,re
for s in ['notify-worker','payments-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'exhaust|dns|pool|config|invalid|error',l,re.I)]
  print(s,len(h),h[:4],h[-2:])
  for i in h[:2]: print(i,L[i-1][:220])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+=' R10: Thread B adds payments-svc (round-10/board.md:3); Thread C notify-worker request failures cause unknown ongoing (round-10/board.md:4) - likely CHG-113 pool_max=-4; DATA_BACKFILL OPEN (round-10/board.md:5); POSTMORTEM_DRAFT OPEN (round-10/board.md:6); CHG-173 irrelevant.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))