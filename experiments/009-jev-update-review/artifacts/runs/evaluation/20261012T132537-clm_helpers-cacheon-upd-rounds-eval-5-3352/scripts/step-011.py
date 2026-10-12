import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR4 logs: auth-svc cert_expired continues (round-04/logs/auth-svc.log:3,55); others quiet.\nR5: board.md:3 OPEN CAPACITY_REVIEW.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|disk|certif|pool|429|memory|oom',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]+hits[-2:]: print(' ',h)