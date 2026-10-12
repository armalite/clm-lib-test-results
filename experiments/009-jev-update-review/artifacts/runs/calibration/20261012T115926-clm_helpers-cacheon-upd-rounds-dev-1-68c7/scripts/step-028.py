import json,re,glob
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']+=' R9: board.md:3 Thread B mitigated; board.md:4 Thread C still restarting; CHG-164 retry budget (noise).'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  hits=[i for i,l in enumerate(open(f),1) if re.search(r'429|exhaust|max_inflight|ERROR',l)]
  print(f.split('/')[-1],len(hits),hits[:4])