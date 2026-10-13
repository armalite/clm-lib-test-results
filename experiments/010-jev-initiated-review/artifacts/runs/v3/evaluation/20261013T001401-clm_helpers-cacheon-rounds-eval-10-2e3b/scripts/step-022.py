import json,re,glob,os
d=json.load(open('/task/workspace/context.json'))
for e in d['entries']:
  if e['id']=='notes': e['body']+="\nR7: board.md:3 Thread B adds inventory-svc, cause/status unchanged."
d['entries']=[e for e in d['entries'] if e['id']=='notes']
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'INFO|\binfo\b',l): continue
    hits.append((i,l.strip()[:110]))
  print(os.path.basename(f),len(hits),[h[0] for h in hits][:40])
  for h in hits[:2]: print(' ',h)