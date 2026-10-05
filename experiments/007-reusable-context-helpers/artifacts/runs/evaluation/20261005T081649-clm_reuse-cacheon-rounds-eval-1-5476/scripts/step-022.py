import re,glob,ctx
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(p).read().splitlines();h=[i for i,l in enumerate(L,1) if re.search(r'cert|lag|ttl|429|pool|ERROR',l,re.I) and 'slow query' not in l]
  print(p.split('/')[-1],len(h),h[:1],h[-1:])
  if h:print(' ',L[h[0]-1][:160])
n=[e for e in ctx.load()['entries'] if e['id']=='notes'][0]['body']
ctx.prune(keep=())
ctx.setnote('notes',n+' R7: board.md:3 POSTMORTEM_DRAFT OPEN, :4 DATA_BACKFILL OPEN; CHG-154 APPLIED retry budget (noise?).')
