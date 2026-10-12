import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR5 logs: auth cert_expired continues (round-05/logs/auth-svc.log:1,75); others quiet.\nR6: board.md:3 Thread D DB_POOL_EXHAUSTED checkout-api ongoing (likely root BAD_CONFIG CHG-113 pool_max=-4). changes:3 CHG-147 irrelevant.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|disk|certif|pool|429|memory|oom|config',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]+hits[-2:]: print(' ',h)