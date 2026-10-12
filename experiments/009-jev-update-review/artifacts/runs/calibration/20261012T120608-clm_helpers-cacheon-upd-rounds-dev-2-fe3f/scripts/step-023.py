import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR9: board.md:3 Thread C pods restarting; changes.md:3 CHG-166 retry budget (noise?).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|cert|SERVFAIL|max_inflight|OOM|restart',l,re.I): hits.append((i,l.strip()[:110]))
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]: print(' ',h)