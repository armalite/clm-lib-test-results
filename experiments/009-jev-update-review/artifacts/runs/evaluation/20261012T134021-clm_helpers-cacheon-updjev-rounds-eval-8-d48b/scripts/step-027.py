import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']=e['body'].replace(' NEXT: advance to R11.','')+' R11: Thread B MITIGATED (round-11/board.md:3); Thread C still restarting, ongoing (round-11/board.md:4); CHG-182 retry budget irrelevant.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['notify-worker','payments-svc','inventory-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('pool|config|dns|error',l,re.I)]
  print(s,len(h),h[:8])
  if h: print(L[h[0]-1][:200])