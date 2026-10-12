import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|exhaust|certificate|disk|tls|429|oom|memory',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:110])
n['body']+=' R8: board.md:3 Thread D closed FALSE ALARM per board (but checkout logs showed pool exhausted; verify R8 logs); CHG-156 PROPOSED ignore.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))