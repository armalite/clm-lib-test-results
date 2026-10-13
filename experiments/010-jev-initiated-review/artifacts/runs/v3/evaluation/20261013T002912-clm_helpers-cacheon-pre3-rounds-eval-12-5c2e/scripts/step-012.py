import json,re
t=open('/task/workspace/spill/s10.obs.txt').read()
lines=t.splitlines()
out=[l for l in lines if l.startswith(('board','changes'))]
from collections import defaultdict
d=defaultdict(list)
for l in lines:
  m=re.match(r'(\S+\.log) (\d+) (.*)',l)
  if m:
    k=(m[1],re.sub(r'\d+','#',m[3][25:95]))
    d[k].append(m[2])
for k,v in d.items():out.append(f'{k[0]} {v[:8]} n={len(v)} {k[1]}')
s='\n'.join(out)
print(s[:4000])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e.append({'id':'n3','role':'note','body':'R3 raw (to be digested):\n'+s[:3500]})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))