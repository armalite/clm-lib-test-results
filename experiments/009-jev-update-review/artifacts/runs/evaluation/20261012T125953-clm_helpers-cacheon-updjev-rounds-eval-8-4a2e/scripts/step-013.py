import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log'))+['/task/fixtures/round-05/board.md']:
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|heap|pool|cert|429|OOM|restart|disk|dns|lag|Thread|Follow',l,re.I): hits.append((i,l.strip()[:110]))
  print(f.split('round-05/')[1],len(hits))
  for h in hits[:5]: print(' ',h)
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace(' Next: advance to r5.',' R5: changes.md:3 CHG-135 log sampling (minor).')
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))