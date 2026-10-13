import json
b=''
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):b+=f'{f}:{i} {l.rstrip()}\n'
print(b)
import collections
c=collections.Counter()
for l in open('/task/workspace/spill/s25.obs.txt'):
  p=l.split(' ',2)
  if len(p)>2 and p[0].endswith('.log'):
    c[(p[0],p[2][:60])]+=1
for k,v in c.most_common(12):print(v,k)
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
n1['body']+='\nR7 raw board/changes:\n'+b[:900]
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))