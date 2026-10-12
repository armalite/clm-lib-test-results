import json,re,glob
b=open('/task/fixtures/round-07/board.md').read();print(b)
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|WARN|429|disk|pool|error',l) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))