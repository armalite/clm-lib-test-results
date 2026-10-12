import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']+=' R10: board.md:3 CLOSED CAPACITY_REVIEW; CHG-171 retry budget noise.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
for f in ['auth-svc','checkout-api','payments-svc','notify-worker','search-api']:
  L=open(f'/task/fixtures/round-10/logs/{f}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if ('ERROR' in l or '429' in l or 'fail' in l or 'exhaust' in l)]
  print(f,len(h),h[:8])
  if h: print(L[h[-1]-1][:200])