import json,glob,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|FATAL|SERVFAIL|429|OOM|restart|expired|backoff',l):print(p.split('/')[-1],i,l.rstrip()[:150])