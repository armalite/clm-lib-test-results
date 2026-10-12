import json,re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'429|used_pct|cert|dns|pool|lag|oom|memory|cache|ERROR',l,re.I) and 'slow' not in l: print(f.split('/')[-1],i,l.strip()[:150])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' R7: changes.md:3 CHG-154 PROPOSED (no effect).'
json.dump(d,open('/task/workspace/context.json','w'))