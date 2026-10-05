import ctx,os,re
d=ctx.load();d['entries']=[{'id':'n.r1','role':'note','body':'ctx.py has load/save/keep_notes(id,body) (keep_notes drops all non-note entries). R1: board empty; CHG-108 PROPOSED (HPA search) not applied.'}];ctx.save(d)
b='/task/fixtures/round-01/logs'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(os.path.join(b,f)),1):
    if not re.search(r'INFO .*(heartbeat|health ok|request ok|gc cycle)|slow query',l):print(f,i,l.strip()[:140])