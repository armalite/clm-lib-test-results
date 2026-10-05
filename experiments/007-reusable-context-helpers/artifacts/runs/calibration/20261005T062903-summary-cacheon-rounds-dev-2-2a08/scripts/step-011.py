import os,re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines();e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|error|level=err',l) and 'slow' not in l]
  print(f,len(e),[i for i,_ in e][:3],[i for i,_ in e][-1:] if e else '');
  if e: print(' ',e[0][1][:150])
  if not e: print(' first',L[0][:120])