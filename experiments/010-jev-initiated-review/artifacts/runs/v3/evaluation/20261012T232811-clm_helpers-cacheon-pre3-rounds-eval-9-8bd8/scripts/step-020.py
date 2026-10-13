import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'] in('n1','n2','n3','n4')]
keep.append({'id':'n5','role':'note','body':'Round5: released; raw filtered output in /task/workspace/spill/s18.obs.txt (not yet analysed). Next: read round-05/board.md and summarize spill.'})
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-05/board.md').read())
import collections
c=collections.Counter()
for l in open('/task/workspace/spill/s18.obs.txt'):
  p=l.split()
  if len(p)>4: c[(p[0],' '.join(p[4:7]))]+=1
for k,v in c.most_common(15): print(k,v)