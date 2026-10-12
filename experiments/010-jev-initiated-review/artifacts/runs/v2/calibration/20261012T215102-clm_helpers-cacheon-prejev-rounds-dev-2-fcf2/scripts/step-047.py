import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|CRIT|SERVFAIL|429|refused|exhaust|OOM|expired|lag|disk|invalid|validation',l) and 'slow query' not in l:print(f.split('/')[-1],i,l.strip()[:110])