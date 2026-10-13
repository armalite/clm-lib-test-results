import os,sys
r=sys.argv[1];b='/task/fixtures/round-'+r
for x in sorted(os.listdir(b)):
  p=b+'/'+x
  if x.endswith('.md'):
    for i,l in enumerate(open(p),1):
      if l.strip():print(x,i,l.rstrip()[:200])
for x in sorted(os.listdir(b+'/logs')):
  for i,l in enumerate(open(b+'/logs/'+x),1):
    if 'slow query' in l or ' INFO' in l or 'level=info' in l.lower():continue
    print(x,i,l.rstrip()[:160])
