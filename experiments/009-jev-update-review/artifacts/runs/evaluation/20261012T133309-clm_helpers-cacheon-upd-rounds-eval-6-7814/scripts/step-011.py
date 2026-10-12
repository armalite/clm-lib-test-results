import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R4: board.md:3 Thread A mitigated; board.md:4 RUNBOOK_UPDATE open. changes.md:4 CHG-136 APPLIED mitigation A ledger-svc; CHG-128 retry GETs=1.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|disk|429',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits))
  if hits: print(hits[0][0],hits[0][1][:150]);print(hits[-1][0],hits[-1][1][:150])