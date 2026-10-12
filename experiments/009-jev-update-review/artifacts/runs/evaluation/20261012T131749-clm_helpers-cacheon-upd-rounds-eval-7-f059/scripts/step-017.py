import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  n=0;h=[]
  for i,l in enumerate(open(f),1):
    if ('slow query' in l):continue
    if re.search('WARN|ERROR|429|disk|pool',l):
      n+=1
      if len(h)<4:h.append((i,l.strip()[:110]))
  print(f.split('/')[-1],n,h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R6: board.md:3 Thread A mitigated; changes.md:3 CHG-150 APPLIED mitigation shipping-svc.'
json.dump(c,open('/task/workspace/context.json','w'))