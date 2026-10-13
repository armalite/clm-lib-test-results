import json,re,glob
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  hits=[(i,l.strip()[:110]) for i,l in enumerate(open(f),1) if re.search('ERROR|error|fail|429|heap|mem',l)]
  print(f.split('/')[-1],len(hits));[print(i,l) for i,l in hits[:3]]
  print('lines',[i for i,_ in hits])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))