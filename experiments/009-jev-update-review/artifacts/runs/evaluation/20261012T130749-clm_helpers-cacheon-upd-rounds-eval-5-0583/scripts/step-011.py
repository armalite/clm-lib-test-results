import json,re
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
keep.append({'id':'n5','role':'note','body':'R4: Thread A -> mitigated (round-04/board.md:3) after CHG-136 APPLIED to search-api (round-04/changes.md:4). OPEN DATA_BACKFILL (:4), VENDOR_TICKET (:5). CHG-131 PROPOSED ignore.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|error|fail|expired|pool|disk',l):
      print(f.split('/')[-1],i,l.strip()[:110]);
