import json
t=open('/task/workspace/spill/s5.obs.txt').read()
ls=t.splitlines()
print(len(ls))
for l in ls[:12]:print(l[:150])
import collections
c=collections.Counter(' '.join(l.split()[:2]+l.split()[4:7]) for l in ls[12:])
for k,v in c.most_common(25):print(v,k[:120])
n1=[e for e in json.load(open('/task/workspace/context.json'))['entries'] if e['id']=='n1'][0]
json.dump({'format':'clm-context/v1','entries':[n1,{'id':'n2','role':'note','body':'Round2 raw filtered output in /task/workspace/spill/s5.obs.txt (being analysed step7).'}]},open('/task/workspace/context.json','w'))