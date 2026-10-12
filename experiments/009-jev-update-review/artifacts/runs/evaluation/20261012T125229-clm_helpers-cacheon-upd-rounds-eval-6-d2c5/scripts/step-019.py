import json,re,glob
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR7: board.md:3 Thread A resolved; :4 OPEN DATA_BACKFILL; :5 OPEN POSTMORTEM_DRAFT.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|used_pct|rss|heap|cert|dns|lag|pool',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:130])