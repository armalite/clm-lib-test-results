import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|error|exhaust|expired|handshake|disk|429|OOM|lag',l): print(f.split('/')[-1],i,l.strip()[:110])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace('Next: advance R9.','R9: no board lines.')
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))