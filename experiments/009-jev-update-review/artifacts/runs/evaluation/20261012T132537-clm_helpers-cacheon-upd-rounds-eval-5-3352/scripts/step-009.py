import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR4: board.md:3 Thread A mitigated; :4 OPEN DATA_BACKFILL; :5 OPEN VENDOR_TICKET. changes:4 CHG-136 APPLIED mitigation A search-api; :3 CHG-131 PROPOSED (ignore).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|disk|certif|pool|429|memory|oom',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]+hits[-2:]: print(' ',h)