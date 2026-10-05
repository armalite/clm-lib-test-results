import ctx,os,re
d=ctx.load();d['entries']=[e for e in d['entries'] if e['role']=='note'];ctx.save(d)
r='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
b=r+'logs'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(os.path.join(b,f)),1):
    if not re.search(r'(heartbeat|health ok|request ok|gc cycle|slow query)',l):print(f,i,l.strip()[:140])