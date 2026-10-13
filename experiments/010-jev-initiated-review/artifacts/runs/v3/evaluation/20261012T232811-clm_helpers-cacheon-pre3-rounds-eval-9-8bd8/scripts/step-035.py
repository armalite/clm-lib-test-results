import json,re
b=open('/task/fixtures/round-08/board.md').read().splitlines()
c=open('/task/fixtures/round-08/changes.md').read().splitlines()
out=[]
for i,l in enumerate(b,1):out.append(f'board:{i}:{l}')
for i,l in enumerate(c,1):out.append(f'chg:{i}:{l}')
import os
for f in sorted(os.listdir('/task/fixtures/round-08/logs')):
  L=[i for i,l in enumerate(open('/task/fixtures/round-08/logs/'+f),1) if 'INFO' not in l and 'slow query' not in l]
  ex=[l.strip()[:110] for i,l in enumerate(open('/task/fixtures/round-08/logs/'+f),1) if i in L[:1]]
  out.append(f'{f}:{L} ex:{ex}')
s='\n'.join(out);print(s)
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'].startswith('n')]
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))