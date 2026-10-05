import re,os
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  ms={}
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'ERROR' in l or 'WARN' in l:
      m=re.search(r'"msg":"([^"]*)"',l); k=m.group(1) if m else l[:80]
      ms.setdefault(k,[]).append(i)
  print(f,{k:(v[0],v[-1],len(v)) for k,v in ms.items()})