import json,os
n=open('/task/workspace/context.json').read()
c=json.loads(n)
note=[e for e in c['entries'] if e['id']=='n1'][0]
note['body']+='\nR3: board.md:3 Thread B MEMORY_LEAK auth-svc ongoing.'
c['entries']=[note]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-03/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:print(f,i,l.rstrip()[:120])
