import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|WARN',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits),hits[:2],hits[-1:])
  if hits: print('  ',L[hits[0]-1][:160])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))