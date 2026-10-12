import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'error|ERROR|WARN|expired|disk|mem|pool|429',l):
      print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+=' R4: board.md:3 Thread A mitigated (CHG-136 APPLIED to search-api changes.md:4); :4 OPEN DATA_BACKFILL; :5 OPEN VENDOR_TICKET; CHG-131 PROPOSED ignore.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))