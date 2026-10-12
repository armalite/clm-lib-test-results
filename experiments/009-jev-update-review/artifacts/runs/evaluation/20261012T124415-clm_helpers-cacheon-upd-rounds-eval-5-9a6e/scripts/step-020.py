import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R7: board.md:3 Thread A RESOLVED; :4 Thread B cause CERT_EXPIRED (auth-svc); :5 OPEN ALERT_TUNING.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|exhaust|certif|disk|429|lag|oom|memory',l,re.I) and 'slow query' not in l: hits.append((i,l.strip()[:110]))
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h)