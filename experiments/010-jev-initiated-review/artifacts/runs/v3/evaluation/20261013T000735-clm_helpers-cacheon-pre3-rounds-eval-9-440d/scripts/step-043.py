import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR9 released (board 3 lines). Next: inspect r9 board/logs."
c['entries']=[n]
json.dump(c,open(p,'w'))
print(open('/task/fixtures/round-09/board.md').read())
import re
for s in ['search-api','notify-worker','shipping-svc','ledger-svc','inventory-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|error|fail|disk|SERVFAIL|expired',l,re.I)]
  print(s,len(h),h[:15]);
  if h: print(L[h[0]-1][:200])