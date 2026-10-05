import json,os
b='/task/fixtures/round-08/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  s=open(b+'logs/'+f).read().splitlines()
  for k in ['certificate_expired','429','SERVFAIL','pool','OOM','disk','lag','config']:
    e=[i+1 for i,x in enumerate(s) if k in x]
    if e: print(f,k,len(e),e[:4],e[-1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))