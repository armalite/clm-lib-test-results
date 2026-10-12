import json,re
for f in ['auth-svc','checkout-api']:
  for i,l in enumerate(open(f'/task/fixtures/round-03/logs/{f}.log'),1):
    if re.search(r'ERROR|memory|heap|OOM|restart|pool',l,re.I): print(f,i,l.strip()[:150])
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n+='\nR3: Thread B MEMORY_LEAK auth-svc ongoing (round-03/board.md:3).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))