import os,re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'slow query' in l or re.search(r'\bINFO\b|level=info',l):continue
    print(f,i,l.strip()[:130])
