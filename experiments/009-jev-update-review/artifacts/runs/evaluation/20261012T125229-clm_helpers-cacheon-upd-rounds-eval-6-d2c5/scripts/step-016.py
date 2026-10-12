import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|mem|rss|oom|used_pct|restart',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR6: board.md:3 Thread D MEMORY_LEAK ledger-svc ongoing; changes.md:3 CHG-147 PROPOSED (ignore).'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))