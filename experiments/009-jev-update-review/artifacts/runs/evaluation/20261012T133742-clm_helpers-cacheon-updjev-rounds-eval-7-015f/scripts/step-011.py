import re,glob,json
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|cache|pool|cert|tls',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])
b=open('/task/workspace/context.json').read()
d=json.loads(b)
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' R4: board.md:3 Thread B CACHE_STAMPEDE checkout-api ongoing (verify logs); changes.md:3 CHG-128 log sampling (irrelevant).'
json.dump(d,open('/task/workspace/context.json','w'))