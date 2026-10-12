import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|429|cache|batch|pool|expir',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]+hits[-2:]: print(' ',h[0],h[1][:150])
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R3: board.md:3 Thread B payments-svc CACHE_STAMPEDE ongoing (suspected). changes.md:3 CHG-124 APPLIED retry budget GETs=1.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))