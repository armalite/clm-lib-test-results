import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R7: board round-07/board.md:3 Thread A resolved; :4 OPEN DATA_BACKFILL; :5 OPEN POSTMORTEM_DRAFT.'})
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'heap|rss|429|ERROR|OOM|restart',l,re.I): print(f.split('/')[-1],i,l.strip()[:110])