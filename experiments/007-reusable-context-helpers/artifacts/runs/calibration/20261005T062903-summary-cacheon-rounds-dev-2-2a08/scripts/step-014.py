import os,re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines();e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|error|level=err',l) and 'slow' not in l]
  print(f,len(e),[i for i,_ in e][:2],[i for i,_ in e][-1:])
  if e: print(' ',e[0][1][:140])
  else: print(' first',L[0][:120])