import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|mem|rss|restart|disk|batch|miss',l,re.I) and not re.search(r'slow query',l,re.I):
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']=e['body'].replace(' Next: advance to R6.','')+"\nR6: board Thread D MEMORY_LEAK ledger-svc ongoing (round-06/board.md:3). CHG-147 PROPOSED (ignore)."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))