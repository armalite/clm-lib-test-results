import json,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  r=[str(i) for i,l in enumerate(open(p),1) if 'INFO' not in l and 'slow query' not in l]
  print(p.split('/')[-1],','.join(r))
  for i,l in enumerate(open(p),1):
    if str(i)==(r[0] if r else ''):print('  ',l.rstrip()[:150])
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'].startswith('n')]
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))