import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if not re.search('slow query|INFO|/v1/health',l)]
  print(p.split('/')[-1],len(ls),ls[0] if ls else '',ls[-1] if ls else '')
  ks={}
  for i,l in ls:
    k=re.sub(r'\d+','#',l)[30:110];ks.setdefault(k,i)
  for k,i in list(ks.items())[:4]:print('  ',i,k)