import json,glob,re
c=json.load(open('/task/workspace/context.json'))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
E.append({'id':'n6','role':'note','body':'Round06: round-06/board.md:3 Thread A mitigated; :4 OPEN ALERT_TUNING. changes.md:3 CHG-150 APPLIED mitigation search-api. 429 tax-provider now also checkout-api round-06/logs/checkout-api.log:21,30,49,50,60,74; ledger-svc.log:17,24,28,34,38,50,53,76. No cert errors r6. Round07 released.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f).read().splitlines(),1):print(f,i,l[:200])
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'certificate|429|ttl|stampede|lag|oom|disk|dns|pool|ERROR',l,re.I)]
  print(f.split('/')[-1],h[:15])
  if h: print(L[h[0]-1][:150])