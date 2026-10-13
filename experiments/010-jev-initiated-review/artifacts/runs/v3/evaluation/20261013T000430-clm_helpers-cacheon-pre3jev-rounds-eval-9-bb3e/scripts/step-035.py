import json,re
B=open('/task/fixtures/round-09/board.md').read()
print(B)
for s in ['search-api','shipping-svc','notify-worker']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search('max_inflight|disk',l)]
  print(s,h[:12])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R9 released; board text printed at step 35 obs. Next: advance to R10.'})
json.dump(c,open('/task/workspace/context.json','w'))