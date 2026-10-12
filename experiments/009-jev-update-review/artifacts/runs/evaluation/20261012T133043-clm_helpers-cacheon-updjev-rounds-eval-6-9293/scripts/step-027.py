import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace(' Next: advance to R9.','')+' R9: board.md:3 Thread B +checkout-api; board.md:4 B mitigated; board.md:5 C ongoing; board.md:6 Thread D FALSE ALARM (drop); board.md:7 CLOSED DATA_BACKFILL.'
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  n=[i+1 for i,l in enumerate(open(f)) if re.search('ERROR|WARN',l) and 'slow' not in l.lower()]
  print(f.split('/')[-1],len(n),n[:8])
  if n: print(open(f).read().splitlines()[n[0]-1][:150])