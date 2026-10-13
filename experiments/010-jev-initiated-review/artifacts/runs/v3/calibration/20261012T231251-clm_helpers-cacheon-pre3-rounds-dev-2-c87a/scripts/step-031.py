import re,os
b='/task/fixtures/round-07/'
for i,l in enumerate(open(b+'board.md'),1): print('board',i,l.rstrip()[:200])
if os.path.exists(b+'changes.md'):
  for i,l in enumerate(open(b+'changes.md'),1): print('chg',i,l.rstrip()[:200])
cnt={}
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|FATAL|OOM|429|disk|max_inflight|restart|fail|servfail',l,re.I):
      k=(f,re.sub(r'\d','',l)[40:110]);cnt.setdefault(k,[]).append(i)
for k,v in cnt.items(): print(k[0],v[:5],len(v),k[1])