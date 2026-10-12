import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|memory|rss|oom|pool|restart',l,re.I) and n<6:
      n+=1;print(f.split('/')[-1],i,l.strip()[:140])
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2')]
keep.append({'id':'n3','role':'note','body':'R2 logs: disk warnings search-api & shipping-svc 91-98% throughout. R3: Thread B opened MEMORY_LEAK auth-svc ongoing (round-03/board.md:3).'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))