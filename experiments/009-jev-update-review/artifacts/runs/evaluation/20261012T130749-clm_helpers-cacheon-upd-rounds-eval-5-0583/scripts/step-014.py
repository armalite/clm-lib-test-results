import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R5: OPEN CAPACITY_REVIEW (round-05/board.md:3).'})
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|certificate|pool|disk|429|dns|oom|lag',l,re.I) and 'slow' not in l.lower():
      print(f.split('/')[-1],i,l.strip()[:150])