import re,collections,json
b='/task/fixtures/stage-1/logs/payments-api.log'
c=collections.Counter();lat=[]
for i,l in enumerate(open(b),1):
  m=re.search(r'(ERROR|WARN)\s+\S+\s+(.{0,40})',l)
  if m:c[re.sub(r'\d+','N',m.group(2))]+=1
  m2=re.search(r'tax-engine.*?(\d+)ms',l)
  if m2 and 'timed out' not in l:lat.append(int(m2.group(1)))
print(c.most_common(6));print(len(lat),sorted(lat)[len(lat)//2] if lat else None)
for i,l in enumerate(open(b),1):
  if 'timed out' in l:print(i,l[:160]);break
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))