import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  hits=[(i,l.strip()) for i,l in enumerate(open(f),1) if re.search(r'WARN|ERROR|expired|exhaust|disk',l) and 'slow' not in l]
  print(f.split('/')[-1],len(hits),[h[0] for h in hits][:40])
  for h in hits[:2]: print(' ',h[0],h[1][:200])
print(open('/task/fixtures/round-09/board.md').read())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))