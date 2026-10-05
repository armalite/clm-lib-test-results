import re,glob,ctx
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f).read().splitlines(),1):print(f,i,l[:200])
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  L=open(p).read().splitlines();h=[i for i,l in enumerate(L,1) if re.search(r'cert|lag|ttl|429|pool|ERROR|WARN',l,re.I) and 'slow query' not in l]
  print(p.split('/')[-1],len(h),h[:1],h[-1:])
  if h:print(' ',L[h[0]-1][:160])
n=[e for e in ctx.load()['entries'] if e['id']=='notes'][0]['body']
ctx.prune(keep=())
ctx.setnote('notes',n)
