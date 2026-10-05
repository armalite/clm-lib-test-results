import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
d['entries'].append({'id':'n7a','role':'note','body':'R7: advanced; s20 output spilled to /task/workspace/spill/s20.obs.txt (read it summarized).'})
json.dump(d,open(p,'w'))
t=open('/task/workspace/spill/s20.obs.txt').read()
ls=t.splitlines()
for l in ls:
  if l.startswith(('board','changes')):print(l[:160])
import collections
c=collections.defaultdict(list)
for l in ls:
  s=l.split(' ',2)
  if len(s)==3 and s[0].endswith('.log'):
    k=(s[0],__import__('re').sub(r'\d+','#',s[2])[30:90]);c[k].append(s[1])
for k,v in c.items():print(k,','.join(v)[:80])