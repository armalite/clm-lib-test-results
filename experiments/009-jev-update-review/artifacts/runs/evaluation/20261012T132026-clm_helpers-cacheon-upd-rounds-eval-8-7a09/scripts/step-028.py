import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+='\nR11: board.md:3 Thread B mitigated; board.md:4 Thread C still restarting ongoing; changes.md:3 CHG-182 noise.'
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|exhaust|pool_max|dns|429|disk',l,re.I):
      n+=1
      if n<=2: print(f.split('/')[-1],i,l.strip()[:140])
  print(f.split('/')[-1],'hits',n)