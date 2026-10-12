import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  hits=[(i+1,l.strip()[:110]) for i,l in enumerate(open(f)) if re.search(r'error|exhaust|SERVFAIL|429|cert|oom|memory|lag|disk',l,re.I)]
  print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] if hits else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))