import json,os
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith('s23')]
c['entries'].append({'id':'n9','role':'note','body':'R9 logs: inventory pool exhausted continues; slow queries inventory/notify/auth; notify-worker no pool_max errors seen.'})
json.dump(c,open('/task/workspace/context.json','w'))
for r in sorted(os.listdir('/task/fixtures')):
  if int(r[-2:])>=9:
    for f in ['board.md','changes.md']:
      p=f'/task/fixtures/{r}/{f}'
      if os.path.exists(p):
        for i,l in enumerate(open(p),1):
          if l.strip(): print(r,f,i,l.rstrip()[:160])