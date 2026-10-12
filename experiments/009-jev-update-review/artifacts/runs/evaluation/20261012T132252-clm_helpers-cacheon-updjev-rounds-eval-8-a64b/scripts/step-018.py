import json,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'WARN' in l or 'ERROR' in l or 'error' in l.lower(): print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3','n4','n5','n6')]
json.dump(c,open('/task/workspace/context.json','w'))