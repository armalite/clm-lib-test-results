import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  hits=[(i,l.strip()) for i,l in enumerate(open(f),1) if re.search(r'ERROR|WARN|error|fail|exhaust|429|OOM|memory',l)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:4]: print(' ',i,l[:150])
print(open('/task/fixtures/round-05/board.md').read())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: CHG-135 APPLIED log sampling health (round-05/changes.md:3) irrelevant.'})
json.dump(c,open('/task/workspace/context.json','w'))