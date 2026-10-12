import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|cache|miss|pool|expir',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR3: board.md:3 Thread B CACHE_STAMPEDE payments-svc ongoing; changes.md:3 CHG-124 APPLIED retry budget GETs=1.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))