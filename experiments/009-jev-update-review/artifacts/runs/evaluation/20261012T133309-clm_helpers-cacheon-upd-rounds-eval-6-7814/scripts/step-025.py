import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R9: board.md:3 B adds checkout-api; board.md:4 B mitigated; board.md:5 C ongoing; board.md:6 D false alarm (drop); board.md:7 DATA_BACKFILL closed.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=[i+1 for i,l in enumerate(open(f)) if re.search('ERROR|WARN|error|warn',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(L),L[:1],L[-1:])
  if L: print(open(f).readlines()[L[0]-1][:200])