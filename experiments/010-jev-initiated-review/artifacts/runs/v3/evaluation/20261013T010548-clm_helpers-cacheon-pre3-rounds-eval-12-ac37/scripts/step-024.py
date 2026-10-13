import json,re
b='/task/fixtures/round-06/'
out=[]
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):out.append(f'{f}:{i} {l.rstrip()[:200]}')
import os
for f in sorted(os.listdir(b+'logs')):
  hits=[i for i,l in enumerate(open(b+'logs/'+f),1) if re.search(r'ERROR|error|429|expired|lag|fail',l)]
  if hits:
    ex=open(b+'logs/'+f).readlines()[hits[0]-1].rstrip()[:140]
    out.append(f'{f}: {len(hits)} hits lines {hits[0]}-{hits[-1]} ex: {ex}')
s='\n'.join(out);print(s)
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace('Next: advance to round 6.','R6 raw:\n'+s)
json.dump({'format':'clm-context/v1','entries':[n1]},open('/task/workspace/context.json','w'))