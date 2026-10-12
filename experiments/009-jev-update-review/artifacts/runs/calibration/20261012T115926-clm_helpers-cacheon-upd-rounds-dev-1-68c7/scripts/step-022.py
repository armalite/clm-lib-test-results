import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|exhaust|429|cert|dns|max_inflight|OOM|disk',l,re.I):
      print(f.split('/')[-1],i,l.strip()[:150]);break
print(open('/task/fixtures/round-07/board.md').read())
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']+=' R7: no board/changes lines.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))