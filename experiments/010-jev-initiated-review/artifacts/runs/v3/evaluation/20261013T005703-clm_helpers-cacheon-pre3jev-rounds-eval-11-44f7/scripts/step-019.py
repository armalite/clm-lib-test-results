import json,re
t=open('/task/workspace/spill/s17.obs.txt').read().splitlines()
for l in t:
  if l.startswith(('board','changes')):print(l[:200])
from collections import defaultdict
d=defaultdict(list);s={}
for l in t:
  m=re.match(r'(\S+\.log) (\d+) (.*)',l)
  if m:
    d[m[1]].append(m[2]);s.setdefault(m[1],m[3][:140])
for k in d:print(k,','.join(d[k]),'|',s[k])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'].append({'id':'n2','role':'note','body':'R5 raw obs in /task/workspace/spill/s17.obs.txt (board, changes, error lines of round-05).'})
json.dump(c,open('/task/workspace/context.json','w'))