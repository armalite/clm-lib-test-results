import json,glob,re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.strip()[:130]) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL',l)]
  print(f.split('/')[-1],len(L),L[:1],L[-1:])
c=json.load(open('/task/workspace/context.json'))
e=c['entries'][0]
e['body']+='\nR7 disk WARN notify-worker.log:2-56 95-98%, shipping-svc.log:18-80.'
c['entries']=[e]
json.dump(c,open('/task/workspace/context.json','w'))