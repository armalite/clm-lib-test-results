import json,glob,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace(' R2 done; next: advance to R3.','')+' R3: board.md:3 Thread A UPSTREAM_RATE_LIMIT shipping-svc+search-api ongoing; :4 OPEN DATA_BACKFILL; :5 OPEN CAPACITY_REVIEW; changes.md:3 CHG-124 TLS ticket rotation (irrelevant?).'
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search('WARN|ERROR|error',l) and 'slow query' not in l:
      n+=1
      if n<=4: print(f.split('/')[-1],i,l.strip()[:150])
  print(f.split('/')[-1],'count',n)