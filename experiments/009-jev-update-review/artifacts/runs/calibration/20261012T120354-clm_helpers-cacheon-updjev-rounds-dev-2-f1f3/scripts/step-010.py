import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|SERVFAIL|certificate|pool|429|OOM|disk|lag|invalid',l,re.I) and 'slow query' not in l: hits.append((i,l.strip()[:110]))
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h)
print(open('/task/fixtures/round-04/board.md').read())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
json.dump(c,open('/task/workspace/context.json','w'))