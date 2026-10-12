import json,re
for s in ['inventory-svc','notify-worker']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'exhaust|dns|SERVFAIL|error|pool',l,re.I)]
  print(s,len(h),h[:3],h[-3:])
  if h: print(L[h[0]-1][:200])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']=e['body'].replace(' Next: advance to R9.','')+' R9: RUNBOOK_UPDATE follow-up OPEN (round-09/board.md:3).'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))