import json
c=json.load(open('/task/workspace/context.json'))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
E.append({'id':'n5','role':'note','body':'Round05: round-05/board.md:3 OPEN CUSTOMER_COMMS. r5 429 ledger round-05/logs/ledger-svc.log:7,35,39,42,47,61; cert search-api.log:6,35,48,62,64,66,70; inventory-svc.log has cert hits ~9-73 (unverified). Round06 released; next: read r6 board/changes, grep logs.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f).read().splitlines(),1):print(f,i,l[:200])
import glob,re
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'certificate|429|ttl|stampede|lag|oom|disk|dns|pool',l,re.I)]
  print(f.split('/')[-1],h[:15])
  if h: print(L[h[0]-1][:150])