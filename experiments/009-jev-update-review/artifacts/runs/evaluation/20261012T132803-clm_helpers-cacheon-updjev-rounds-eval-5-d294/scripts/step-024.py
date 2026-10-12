import re,json,collections
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:120]) for i,l in enumerate(L) if re.search('WARN|ERROR|error|warn|exhaust|certif|disk',l) and 'slow' not in l]
  print(s,len(h));[print(x) for x in h[:3]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+='\nR9: no board/changes lines.'
json.dump(c,open('/task/workspace/context.json','w'))