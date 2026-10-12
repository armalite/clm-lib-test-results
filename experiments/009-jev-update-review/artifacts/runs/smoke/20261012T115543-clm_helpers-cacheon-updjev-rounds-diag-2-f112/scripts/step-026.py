import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R8 board: Thread B (DISK) mitigated round-08/board.md:3; Thread C still restarting board.md:4.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['inventory-svc','ledger-svc','notify-worker']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('disk|pool_max|ERROR|restart',l,re.I)]
  print(s,len(h))
  for x in h[:4]:print(x)