import json,re
r='/task/fixtures/round-09/'
for s in ['notify-worker','payments-svc','checkout-api']:
  L=[i for i,l in enumerate(open(r+'logs/'+s+'.log'),1) if re.search('429|max_inflight|validation',l)]
  print(s,L[:8])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: board Thread B mitigated (round-09/board.md:3); Thread C still ongoing (round-09/board.md:4). CHG-164 retry budget irrelevant. Next: advance R10.'})
json.dump(c,open('/task/workspace/context.json','w'))