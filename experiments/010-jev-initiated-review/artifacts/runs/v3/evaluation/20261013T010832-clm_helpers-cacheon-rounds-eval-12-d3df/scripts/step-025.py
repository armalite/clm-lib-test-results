import os,re
r=sorted(os.listdir('/task/fixtures'));print(r)
for d in r[8:]:
  p='/task/fixtures/'+d
  for f in ['board.md','changes.md']:
    if os.path.exists(p+'/'+f):print(d,f,open(p+'/'+f).read()[:1500])
  for f in sorted(os.listdir(p+'/logs')):
    L=[(i+1,l) for i,l in enumerate(open(p+'/logs/'+f)) if not re.search('slow query|request ok|heartbeat|gc |health ok',l)]
    print(f,len(L),L[0][0] if L else '',L[-1][0] if L else '',L[0][1][:150] if L else '')