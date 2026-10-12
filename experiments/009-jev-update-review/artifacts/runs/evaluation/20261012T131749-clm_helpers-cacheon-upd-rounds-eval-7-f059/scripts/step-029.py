import json,re
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1'][0]
b=e['body'].replace('ongoing round-09/board.md:4','mitigated round-10/board.md:3 (was ongoing round-09/board.md:4)').replace('RUNBOOK_UPDATE(r8:4), ','').replace('R9 done; next advance to R10.','RUNBOOK_UPDATE closed r10:5. ThreadC r10:4 still restarting. R10 done; next advance to R11.')
e['body']=b
c['entries']=[e]
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-10/logs/ledger-svc.log'),1):
  if re.search('pool_max|config|ERROR|FATAL',l): print(i,l[:150].rstrip())