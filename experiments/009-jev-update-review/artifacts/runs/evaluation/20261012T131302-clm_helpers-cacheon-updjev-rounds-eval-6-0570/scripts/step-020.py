import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|disk|heap|batch|miss|pool|cert|dns|lag',l,re.I) and 'slow query' not in l.lower(): hits.append((i,l.strip()[:110]))
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(h)
  print([h[0] for h in hits])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+="\nR7: Thread A resolved (round-07/board.md:3). Follow-ups OPEN DATA_BACKFILL (board.md:4), POSTMORTEM_DRAFT (board.md:5)."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))