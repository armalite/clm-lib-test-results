import json,re,glob
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  hits={}
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search(r'WARN|ERROR|FATAL|restart|cert|pool|heap|OOM|429|dns',l,re.I):
      k=re.sub(r'[0-9]+','#',l)[:90]
      hits.setdefault(k,[]).append(i)
  print(f.split('/')[-1])
  for k,v in hits.items(): print(' ',v,k.strip())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace(' Next: advance to R5.','')+' R5 changes:3 CHG-135 APPLIED health log sampling (irrelevant).'
json.dump(c,open('/task/workspace/context.json','w'))