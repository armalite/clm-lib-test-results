import json,collections
t=open('/task/workspace/spill/s28.obs.txt').read().splitlines()
c=collections.Counter()
for l in t:
  if l.startswith('search-api.log'):
    try:
      j=json.loads(l.split(' ',2)[2]);c[j.get('msg')]+=1
    except Exception: c[l[20:90]]+=1
print(c)
for l in t:
  if l.startswith('search-api.log') and 'config' in l:print(l[:200]);break
x=json.load(open('/task/workspace/context.json'))
x['entries']=[e for e in x['entries'] if e['id']=='notes']
x['entries'][0]['body']+=' R9: board.md:3 Thread C still restarting; changes.md:3 CHG-166 noise. CERT auth-svc.log:22 shipping-svc.log:28; search-api 429 search-api.log:1.'
json.dump(x,open('/task/workspace/context.json','w'))