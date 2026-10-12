import os,json
d='/task/fixtures/round-03/logs/'
for s in sorted(os.listdir(d)):
  L=open(d+s).read().splitlines()
  h=[(i+1,l[:130]) for i,l in enumerate(L) if ' INFO ' not in l and 'slow query' not in l]
  print(s,len(h));[print(i,l) for i,l in h[:6]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R3 logs plain format (ts LEVEL svc msg).'
json.dump(c,open('/task/workspace/context.json','w'))