import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))
s=open('/task/workspace/spill/s22.obs.txt').read()
l=s.splitlines()
print('\n'.join(l[:12]))
import collections
d=collections.defaultdict(list)
for x in l[12:]:
  p=x.split(' ',2)
  if len(p)>2:
    k=p[0]+' '+('429' if '429' in p[2] else p[2][:60]);d[k].append(p[1])
for k,v in d.items():print(k,','.join(v)[:200])