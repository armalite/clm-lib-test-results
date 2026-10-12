import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R7: board.md:3 Thread A resolved; board.md:4 DATA_BACKFILL open; board.md:5 POSTMORTEM_DRAFT open.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines();hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|429|disk|heap|cache',l,re.I) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits),hits[0] if hits else '',hits[-1][0] if hits else '')