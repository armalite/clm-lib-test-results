import json,glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read())
print(open(b+'changes.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  n=0
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l:
      n+=1
      if n<=6:print(p.split('/')[-1],i,l.strip()[:140])
  print(p.split('/')[-1],'count',n)
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: nothing; CHG-108 PROPOSED (search HPA) not applied. R2 released; inspecting (see next obs).'}]}
json.dump(c,open('/task/workspace/context.json','w'))