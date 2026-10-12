import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|expired|pool|disk|429|lag|mem',l,re.I) and 'slow' not in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]+hits[-2:]: print(h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board.md:3 Thread A mitigated; :4 OPEN DATA_BACKFILL; :5 OPEN VENDOR_TICKET; changes.md:4 CHG-136 APPLIED mitigation search-api; :3 CHG-131 PROPOSED (ignore).'})
json.dump(c,open('/task/workspace/context.json','w'))