import json,glob,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
for p in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(p).read().splitlines(),1):
    if re.search(r'ERROR|FATAL|CRIT',l) or ('WARN' in l and 'slow' not in l.lower()):print(p.split('/')[-1],i,l[:160])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))