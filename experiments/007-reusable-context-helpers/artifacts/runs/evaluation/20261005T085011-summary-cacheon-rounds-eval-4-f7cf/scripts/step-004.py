import os,re
b='/task/fixtures/round-02/'
print(open(b+'board.md').read())
skip=re.compile(r'request ok|health ok|heartbeat|gc cycle|slow query')
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if not skip.search(l):print(f,i,l.strip()[:140])