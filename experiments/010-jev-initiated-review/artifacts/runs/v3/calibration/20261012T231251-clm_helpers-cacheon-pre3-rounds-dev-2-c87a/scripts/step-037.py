import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']=n['body'].replace(' Next: advance to round 8.','')+' R8: board/logs in spill/s35.obs.txt (review pending).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-08/board.md'),1):print(i,l.rstrip()[:140])
import re,glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  h=[i for i,l in enumerate(open(f),1) if re.search(r'ERROR|429|SERVFAIL|cert|uptime',l) and 'slow' not in l.lower()]
  print(f.split('/')[-1],len(h),h[:6])
  if h:print(open(f).readlines()[h[0]-1].strip()[:140])